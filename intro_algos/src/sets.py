import numpy as np
import string
from lnkdlst import LinkedList

np.random.seed(0)


class Item():
    ''' Item class to store key val pair '''

    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return f'Item(key={self.key}, val={self.val})'


class DirectAccessArray():
    ''' Direct Access Array implementation for Set '''

    def __init__(self, items: zip, array_size: int):
        # Iterate through elements until the end, default
        # Build direct access array
        self.array_size = array_size  # Size of array
        # Initial direct access set using tuple because it is immutable
        self.set = [None] * array_size
        # Build direct access set with items, O(n)
        for item in items:
            print(item, end=" ")
            self.set[item.key] = item
        print('\n', self)

    def __str__(self):
        str_buffer = ['Set: [']
        for item in self.set:
            if item is None:
                str_buffer.append(',')
            else:
                str_buffer.append('\n\t\t' + str(item) + ',')
        str_buffer.append(']')
        join_str = ''.join(str_buffer)
        return join_str  # textwrap.fill(join_str, 100)

    def find(self, key):
        # O(1)
        return self.set[key]

    def insert(self, item):
        # O(1)
        # keys must be unique, will replace value if key already exists
        self.set[item.key] = item

    def delete(self, key):
        # O(1)
        item = self.set[key]
        self.set[key] = None
        return item

    def find_min(self):
        # O(array_size)
        min_val = None
        i = 0
        # Find first item to intitialize min_val
        while i < self.array_size:
            if self.set[i] is not None:
                return self.set[i]
            i += 1
        return None

    def find_max(self):
        # O(array_size)
        max_val = None
        i = self.array_size - 1
        # Find first item to intitialize min_val
        while i >= 0:
            if self.set[i] is not None:
                return self.set[i]
            i -= 1
        return None

    def find_prev(self, key):
        # O(array_size)
        i = key - 1
        # Find first item to prior to key
        while i >= 0:
            if self.set[i] is not None:
                return self.set[i]
            i -= 1
        return None

    def find_next(self, key):
        # O(array_size)
        i = key + 1
        # Find first item to prior to key
        while i < self.array_size:
            if self.set[i] is not None:
                return self.set[i]
            i += 1
        return None

    @staticmethod
    def run():
        # Get random integer keys
        max_key = 100
        num_items = 10
        key_data = np.random.randint(0, high=max_key, size=num_items)
        # Get random values for items data
        val_data = [string.ascii_letters[i] for i in range(num_items)]
        print('key data', key_data, '\nval_data', val_data)
        # Create item list
        items = [Item(k, v) for k, v in zip(key_data, val_data)]
        direct_access_set = DirectAccessArray(items, 2 * max_key)
        # find key
        key = key_data[2]
        item = direct_access_set.find(key)
        print(f'\tLooking for key={key}, Found {item}')
        # insert key val pair
        keys = np.random.randint(0, high=max_key, size=3)
        val = 'U'
        for key in keys:
            direct_access_set.insert(Item(key, val))
            print(f'\tInserting val {val} at {key}')
        print('\t\t', direct_access_set)
        # delete item with keys
        for key in keys:
            item = direct_access_set.delete(key)
            print(f'\tDeleted item {item}')
        print('\t\t', direct_access_set)
        # find item with min key
        min_item = direct_access_set.find_min()
        print(f'\tFound item at min key {min_item}')
        # find item with max key
        max_item = direct_access_set.find_max()
        print(f'\tFound item at max key {max_item}')
        # find item after min key
        next_item = direct_access_set.find_next(min_item.key)
        print(f'\tFound item after to min key, {next_item}')
        # find item before max key
        prev_item = direct_access_set.find_prev(max_item.key)
        print(f'\tFound item before max key, {prev_item}')
        # find item before min key
        prev_item = direct_access_set.find_prev(min_item.key)
        print(f'\tFound item before min key, {prev_item}')
        # find item after max key
        next_item = direct_access_set.find_next(max_item.key)
        print(f'\tFound item before max key, {next_item}')


def division_hash(key: int, base: int) -> int:
    ''' Map key to hash table, hash key using universal has function
    Divison hash function '''
    return key % base

class HashTable():
    def __init__(self, items: zip, array_size: int):
        # Iterate through elements until the end, default
        # Build hash table
        self.array_size = array_size  # Size of array
        # Initialize hashtable set using tuple because it is immutable
        self.set = [None] * self.array_size
        self.num_items = len(items)

        # Build hash table set with items, O(n)
        for item in items:
            self.insert(item)
        print(self)

    def get_fill_prcnt(self):
        fill_prcnt = self.num_items / self.array_size
        print('Fill prcnt is %{p:3.2f}'.format(p=fill_prcnt * 100))
        return fill_prcnt

    def __str__(self):
        str_buffer = ['Set: [']
        for item in self.set:
            if item is None:
                str_buffer.append(',')
            else:
                str_buffer.append('\n\t\t' + str(item) + ',')
        str_buffer.append(']')
        join_str = ''.join(str_buffer)
        return join_str  # textwrap.fill(join_str, 100)

    def find(self, key):
        # O(1)
        hash_key = division_hash(key, self.array_size)
        # If there was a collision there is a linked list
        # at the hash_key location
        # Find the correct key, assume there are no duplicate keys
        if isinstance(self.set[hash_key], LinkedList):
            indx = self.set[hash_key].len
            curr_node = self.set[hash_key].head
            while indx > 0:
                item = curr_node.data
                if item.key == key:
                    return item
                curr_node = curr_node.next_node
                indx -= 1
        return self.set[hash_key]

    def insert(self, item):
        # O(1)
        # keys must be unique, will replace value if key already exists
        hash_key = division_hash(item.key, self.array_size)
        # print(hash_key)
        # print(item, end=" ")
        # If there is already a linked list at hash_key
        # then append the new item
        if isinstance(self.set[hash_key], LinkedList):
            # print('Collision, Appending to linked list')
            self.set[hash_key].insert_last(item)
        # If this is the first collision
        # add a linked list at index hash key
        elif self.set[hash_key] is not None:
            # print('Collision, Initializing with linked ' \
            # 'list for items {o}, {t}'.format(o=self.set[hash_key], t=item))
            self.set[hash_key] = LinkedList([self.set[hash_key], item])
        else:
            # else add item to the index hash key
            self.set[hash_key] = item

    def delete(self, key):
        # O(1)
        item = self.find(key)
        hash_key = division_hash(item.key, self.array_size)
        if isinstance(self.set[hash_key], LinkedList):
            self.set[hash_key].delete_at(item)
            return item
        item = self.set[hash_key]
        self.set[hash_key] = None
        return item

    def find_min(self):
        # O(array_size)
        min_val = None
        i = 0
        # Find first item to intitialize min_val
        while i < self.array_size:
            if self.set[i] is not None:
                return self.set[i]
            i += 1
        return None

    def find_max(self):
        # O(array_size)
        max_val = None
        i = self.array_size - 1
        # Find first item to intitialize min_val
        while i >= 0:
            if self.set[i] is not None:
                return self.set[i]
            i -= 1
        return None

    def find_prev(self, key):
        # O(array_size)
        i = key - 1
        # Find first item to prior to key
        while i >= 0:
            if self.set[i] is not None:
                return self.set[i]
            i -= 1
        return None

    def find_next(self, key):
        # O(array_size)
        i = key + 1
        # Find first item to prior to key
        while i < self.array_size:
            if self.set[i] is not None:
                return self.set[i]
            i += 1
        return None

    @staticmethod
    def run():
        # Get random integer keys
        max_key = 10000
        num_items = 50
        key_data = np.random.randint(0, high=max_key, size=num_items)
        # Get random values for items data
        val_data = [string.ascii_letters[i] for i in range(num_items)]
        print('key data', key_data, '\nval_data', val_data)
        # Create item list
        items = [Item(k, v) for k, v in zip(key_data, val_data)]
        array_size = 30
        hash_table = HashTable(items, array_size)
        # Get fill prcnt
        hash_table.get_fill_prcnt()
        # find key
        key = 7012 #key_data[2]
        print(f'\tLooking for key={key}', end="")
        item = hash_table.find(key)
        print(f', Found {item}')

        # insert key val pair
        keys = [0, 1, 2, array_size-1] #np.random.randint(0, high=max_key, size=3)
        val = 'U'
        for key in keys:
            hash_table.insert(Item(key, val))
            print(f'\tInserting val {val} at {key}')
        print('\t\t', hash_table)

        # delete item with keys
        for key in keys:
            item = hash_table.delete(key)
            print(f'\tDeleted item {item}')
        print('\t\t', hash_table)
        # find item with min key
        min_item = hash_table.find_min()
        print(f'\tFound item at min key {min_item}')
        import sys;
        sys.exit()
        # todo implement find_max, ....
        # find item with max key
        max_item = hash_table.find_max()
        print(f'\tFound item at max key {max_item}')
        # find item after min key
        next_item = hash_table.find_next(min_item.key)
        print(f'\tFound item after to min key, {next_item}')
        # find item before max key
        prev_item = hash_table.find_prev(max_item.key)
        print(f'\tFound item before max key, {prev_item}')
        # find item before min key
        prev_item = hash_table.find_prev(min_item.key)
        print(f'\tFound item before min key, {prev_item}')
        # find item after max key
        next_item = hash_table.find_next(max_item.key)
        print(f'\tFound item before max key, {next_item}')



