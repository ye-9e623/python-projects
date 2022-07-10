import numpy as np

class LinkedList:
    ''' Linked List class
    Attributes:
    Methods: '''
    class Node:
        ''' Node class
        Attributes:
            data: object store in node
            next: pointer to next Node '''
        def __init__(self, data):
            self.data = data
            self.next_node = None
        def __str__(self):
            return ('Node(data={d}, next_node = {nn})'.format(d=self.data, nn=self.next_node))

    def __init__(self, data_array: list=[], debug_flg=False):
        self.len = 0
        if data_array:
            if debug_flg: print('Build linked list with data array', data_array)
            self.head = LinkedList.Node(data_array[0])
            curr_node = self.head
            self.len += 1
            # Build linked list by initializing the current node with a data element
            # and assigning the prior nodes' next_node to point to the current node
            for data in data_array[1:]: #O(n)
                curr_node.next_node = LinkedList.Node(data)
                curr_node = curr_node.next_node
                self.len += 1
            self.tail = curr_node
        else:
            self.head = None
            self.tail = None
        if debug_flg: print('Built Linked List: ', self.head)
    def __str__(self):
        return 'Linked list: len={l}, head data={h}, tail data={t}'.format(l=self.len, h=self.head.data, t=self.tail.data)

    def insert_last(self, data):
        ''' Append data to the tail of the linked list '''
        new_node = LinkedList.Node(data) # O(1)
        self.tail.next_node = new_node
        self.tail = new_node
        self.len += 1

    def get_at(self, indx):
        ''' Get the node  at position indx '''
        # O(n)
        curr_node = self.head
        print_str = '\tData at {i}: '.format(i=indx)
        while indx > 0:
            curr_node = curr_node.next_node
            indx -= 1
        print(print_str, '{d}'.format(d=curr_node.data))
        return curr_node

    def insert_first(self, data):
        new_node = LinkedList.Node(data) #O(1)
        new_node.next_node = self.head
        self.head = new_node
        self.len += 1

    def insert_at(self, indx, data):
        ''' Insert data at index '''
        if indx > self.len-1:
            raise ValueError('\t\tindx must be less than {l}, user provided index={i}'.format(l=self.len, i=indx))
        if indx == 0:
            self.insert_first(data)
            return
        elif indx == self.len-1:
            self.insert_last(data)
            return
        curr_node = self.head
        new_node = LinkedList.Node(data)
        while indx > 0: # O(n)
            curr_node = curr_node.next_node
            indx -= 1
        curr_node.next_node, curr_node.next_node.next_node = new_node, curr_node.next_node
        self.len += 1

    def delete_first(self):
        # O(1)
        self.head = self.head.next_node
        self.len -= 1

    def delete_last(self):
        # O(n)
        curr_node = self.head
        while curr_node.next_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = None
        self.tail = curr_node
        self.len -= 1

    def delete_at(self, data):
        ''' Delete all occurences of data '''
        num_deletes = 0
        # Check is data is at head, if so reassign head to head's nex tnode
        if self.head.data == data:
            num_deletes += 1
            self.delete_first()
        curr_node = self.head
        # While the next node exists
        while curr_node.next_node is not None:
            # print('Curr node data:', curr_node.data, 'Next node data:', curr_node.next_node.data)
            # Check if the next nodes data matches
            if curr_node.next_node.data == data:
                num_deletes += 1
                # If the next node is tail, replace tail with the current node
                if curr_node.next_node.next_node is None:  # Deleting tail
                    self.delete_last()
                # else delete the curr nodes's next node
                # by setting the curr node's next node, to the next node's next node
                else:
                    curr_node.next_node = curr_node.next_node.next_node
                    self.len -= 1
            # else if there is no match to data go to the next node
            else:
                curr_node = curr_node.next_node
        print('Deleted {o} occurences of {d}'.format(o=num_deletes, d=data))

    @staticmethod
    def run():
        print('**** Implementing Linked List')
        data = np.random.randint(0, high=100, size=5).tolist()
        print('Orig Data:', data)
        linked_list = LinkedList(data)  # Initialize linked list
        print(linked_list)
        val = 'abc'
        print('***** Appending data:', val)
        linked_list.insert_last(val)  # Append data to linked list
        print(linked_list, '\n\t', linked_list.head)
        indx = 4
        print('***** Getting data at:', indx)
        curr_node = linked_list.get_at(indx)  # Get data at index
        print('***** Insert data at first:', curr_node.data)
        linked_list.insert_at(0, curr_node.data)
        print(linked_list, '\n\t', linked_list.head)
        print('***** Insert data at third:', curr_node.data)
        linked_list.insert_at(2, curr_node.data)
        print(linked_list, '\n\t', linked_list.head)
        print('***** Try to insert at length greater than list')
        try:
            linked_list.insert_at(linked_list.len, curr_node.data)
        except Exception as e:
            print('Caught exception ', type(e).__name__, e)
        print('***** Insert at end of list')
        linked_list.insert_at(linked_list.len - 1, curr_node.data)
        print(linked_list, '\n\t', linked_list.head)
        print('***** Deleting from list all occurences of:', curr_node.data)
        linked_list.delete_at(curr_node.data)  # Delete from linked list
        print(linked_list, '\n\t', linked_list.head)


class Queue:
    ''' FIFO '''
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None
        self.num_items = 0

    def __str__(self):
        str_buffer = ['Queue:']
        node = self.first
        item = node.item
        while item is not None:
            str_buffer.append('\t{i}'.format(i=item.__str__()))
            node = node.next
            if node:
                item = node.item
            else:
                item = None
        return '\n'.join(str_buffer)
    def is_empty(self):
        if self.first is None:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.last is None:
            self.last = Queue.Node(item)
            self.first = self.last
        else:
            self.last.next = Queue.Node(item)
            self.last = self.last.next
        self.num_items += 1

    def dequeue(self):
        if self.first is not None:
            temp = self.first
            self.first = temp.next
            self.num_items -= 1
            if self.first is None:
                self.last = None
            return temp.item


class Stack:
    ''' FIFO '''
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    def __init__(self):
        self.top = None
        self.num_items = 0

    def __str__(self):
        str_buffer = ['Stack:']
        node = self.top
        item = node.item
        while item is not None:
            str_buffer.append('\t{i}'.format(i=item.__str__()))
            node = node.next
            if node:
                item = node.item
            else:
                item = None
        return '\n'.join(str_buffer)

    def pop(self):
        ''' Remove item from top of stack '''
        if self.top is None:
            return self.top
        else:
            temp = self.top
            self.top = self.top.next
            self.num_items -= 1
            return temp.item

    def push(self, item):
        ''' Add item to top of stack '''
        if self.top is None:
            self.top = Stack.Node(item)
        else:
            temp = self.top
            self.top = Stack.Node(item)
            self.top.next = temp
        self.num_items += 1

    def is_empty(self):
        ''' Check if stack is empty '''
        if self.top is None:
            return True
        else:
            return False