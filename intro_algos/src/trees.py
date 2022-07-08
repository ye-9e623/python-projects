import numpy as np
import string
from sets import Item, custom_next, SetInterface
np.random.seed(0)

class BinaryTree(SetInterface):

    class Node():
        ''' Node class
        Attributes:
            item: key, val
            parent: pointer to parent
            left: pointer to left child
            right: pointer to right child
            '''
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.left = None
            self.right = None

        def __str__(self):
            if self.right is not None:
                r = self.right.item
            else:
                r = ''
            if self.left is not None:
                l = self.left.item
            else:
                l = ''
            if self.parent is not None:
                p = self.parent.item
            else:
                p = ''
            return ('Node(Item={i}, parent={p}, left={l}, right={r})'.
                    format(i=self.item, p=p, l=l, r=r))

    #def preorder_traversal(self, node: Node):
    #    while node is not None:
    #        preorder_traversal(node)

    def __init__(self, items: zip):
        # Iterate through elements until the end
        # Build direct access set with items, O(n)
        self.num_items = 0
        item = custom_next(items)
        self.root = BinaryTree.Node(item)
        print(f'root node {self.root}')
        while item is not None:
            self.num_items += 1
            item = custom_next(items)
            if item is not None:
                self.insert(item)
        print('\n', self)
        self.preorder_traversal(self.root)
        return

    @classmethod
    def preorder_traversal(cls, node):
        if node is not None:
            print(node)
            cls.preorder_traversal(node.left)
            cls.preorder_traversal(node.right)
        return
    def __str__(self):
        return ''
    #     str_buffer = ['Set: [']
    #     while node is not None:
    #         if item is None:
    #             str_buffer.append(',')
    #         else:
    #             str_buffer.append('\n\t\t' + str(item) + ',')
    #     str_buffer.append(']')
    #     join_str = ''.join(str_buffer)
    #     return join_str

    def find(self, key):
        return

    def insert(self, item):
        node = self.root
        print(f'root node {node}')

        while node.left is not None:
            if node.right is None:
                node.right = BinaryTree.Node(item)
                node.right.parent = node
                print(f'right node {node.right}')
                return
            node = node.left
        node.left = BinaryTree.Node(item)
        node.left.parent = node
        print(f'left node {node.left}')
        return

        # Visit right recursive until reach node None
        # If left node is None, insert new node, return
        return

    def delete(self, key):
        return

    def find_min(self):
        return

    def find_max(self):
        return

    def find_prev(self, key):
        return

    def find_next(self, key):
        return

    @staticmethod
    def validate():
        # Get random integer keys
        max_key = 10000
        num_items = 50
        key_data = np.random.randint(0, high=max_key, size=num_items)
        # Get random values for items data
        val_data = [string.ascii_letters[i] for i in range(num_items)]
        print('key data', key_data, '\nval_data', val_data)
        # Create item list
        items = [Item(k, v) for k, v in zip(key_data, val_data)]
        binary_tree = BinaryTree(iter(items))
        import sys; sys.exit()
        # Get fill prcnt
        hash_table.get_fill_prcnt()
        # find key
        key = 7012  # key_data[2]
        print(f'\tLooking for key={key}', end="")
        item = hash_table.find(key)
        print(f', Found {item}')

        # insert key val pair
        keys = [0, 1, 2, array_size - 1]  # np.random.randint(0, high=max_key, size=3)
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
