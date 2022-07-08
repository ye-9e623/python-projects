import numpy as np
import string
from sets import Item, custom_next, SetInterface
np.random.seed(0)


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

    def subtree_iter(self):
        ''' Iterate in travesal order

        Everything to left of root node is < everything to right of root node
        Iterate on all nodes in left subtree
        Iterate on root node of subtree
        Iterate on all nodes in right subtree'''
        if self.left:
            #print(self.left)
            yield from self.left.subtree_iter()
        #print(self)
        yield self
        if self.right:
            #print(self.right)
            yield from self.right.substree_iter()
    def subtree_first(self):
        ''' Return first node of subtree in traversal order
        Recurse on left nodes until node is None (fall off tree)
        then undo last step by return self '''
        if self.left: return self.subtree_first()
        else: return self

    def subtree_last(self):
        if self.right: return self.subtree_last()
        else: return self

    def successor(self):
        ''' Next node in tree's traversal order

        if there is a right child, get the left most leaf
        (first thing in the right child's subtree)
        if there is no right child,
        if the node is the left child of a parent, then return parent
        (walk up the tree until node is left child of parent '''
        if self.right: return self.right.subtree_first()
        # walk up the tree until going up a left branch
        # while there is a parent (not at root)
        # and still the right most node, keep going to parent
        while self.parent and (self == self.parent.right):
            self = self.parent
        return self.parent

    def predecessor(self):
        if self.left: return self.left.subtree_last()
        while self.parent and (self == self.parent.left):
            self = self.parent
        return self.parent

    def subtree_insert_before(self, new_node): # O(h)
        ''' If has node has left child, walk down the tree to the last node
        and the '''
        if self.left:
            self = self.left.subtree_last()
            self.right, new_node.parent = new_node, self
        else:
            self.left, new_node.parent = new_node, self
        #self.maintain() # wait for R07!
    def subtree_insert_after(self, new_node): # O(h)
        ''' If no right child, put new node in right child
        If node has right child, get left most descedant in right subtree
        '''
        if self.right:
            self = self.right.subtree_first()
            self.left, new_node.parent = new_node, self
        else:
            self.right, new_node.parent = new_node, self
        # self.maintain() # wait for R07!
    #lec 6 42min
    def subtree_delete(self): # O(h)
        ''' If leaf just delete node (
        If root (self.parent is None)'''

        # if not a leaf
        if self.left or self.right:
            if self.left:
                # have a left child, get predecessor (lower in tree)
                node = self.predecessor()
            else:
                node = self.successor()
            # swap contents of node to delete with predecessor/successor
            # delete recursively, node to delete move to bottom of tree
            self.item, node.item = node.item, self.item
            return node.subtree_delete()
        if self.parent:
            if self.parent.left is self:
                self.parent.left = None
            else:
                self.parent.right = None
            # self.parent.maintain() # wait for R07!
        return self

class BST_Node(Node):
    def subtree_find(self, k): # O(h)
        if k < self.item.key:
            if self.left: return self.left.subtree_find(k)
        elif k > self.item.key:
            if self.right: return self.right.subtree_find(k)
        else: return self
        return None

    def subtree_find_next(self, k): # O(h)
        if self.item.key <= k:
            if self.right: return self.right.subtree_find_next(k)
            else: return None
        elif self.left:
            B = self.left.subtree_find_next(k)
            if B: return B
        return self

    def subtree_find_prev(self, k): # O(h)
        if self.item.key >= k:
            if self.left: return self.left.subtree_find_prev(k)
            else: return None
        elif self.right:
            B = self.right.subtree_find_prev(k)
            if B: return B
        return self

    def subtree_insert(self, B): # O(h)
        if B.item.key < self.item.key:
            if self.left: self.left.subtree_insert(B)
            else: self.subtree_insert_before(B)
        elif B.item.key > self.item.key:
            if self.right: self.right.subtree_insert(B)
            else: self.subtree_insert_after(B)
        else: self.item = B.item
        #print('Inserted B', B)
        #print('Updated A', self)
        #breakpoint()

class Binary_Tree:
    def __init__(self, Node_Type = Node):
        self.root = None
        self.num_items = 0
        #T.Node_Type = Node_Type
    def __len__(self):
         return T.num_items
    def __iter__(self):
        if self.root:
            for self in self.root.subtree_iter():
                #print(self.item)
                yield self.item

class Set_Binary_Tree(Binary_Tree): # Binary Search Tree
    def __init__(self): super().__init__(BST_Node)

    def iter_order(self):
        print(self)
        yield from self

    def build(self, X):
        for x in X:
            self.insert(x)

    def find_min(self):
        if self.root: return self.root.subtree_first().item
    def find_max(self):
        if self.root: return self.root.subtree_last().item
    def find(self, k):
        if self.root:
            node = self.root.subtree_find(k)
            print(node, end="")
            if node: return node.item
    def find_next(self, k):
        if self.root:
            node = self.root.subtree_find_next(k)
            if node: return node.item
    def find_prev(self, k):
        if self.root:
            node = self.root.subtree_find_prev(k)
            if node: return node.item
    def insert(self, x):
        new_node = BST_Node(x)

        if self.root:
            self.root.subtree_insert(new_node)
            if new_node.parent is None: return False
        else:
            self.root = new_node

        self.num_items += 1
        return True
    def delete(self, k):
        assert self.root
        node = self.root.subtree_find(k)
        assert node
        ext = node.subtree_delete()
        if ext.parent is None: self.root = None
        self.num_items -= 1
        return ext.item

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
        item = custom_next(iter(items))
        binary_tree_set = Set_Binary_Tree()
        binary_tree_set.build(items)
        #next(binary_tree_set.root.subtree_iter())
        #print(binary_tree_set.find(2732))
        #print(binary_tree_set.iter_order())
        for key in key_data:
            print(binary_tree_set.find(key))
            #range(binary_tree_set.num_items):
            #next(binary_tree_set.root.subtree_iter())
            #next(binary_tree_set.root.iter_order())
        breakpoint()
        #         self.root = BinaryTree.Node(item)
        #         print(f'root node {self.root}')
        #         while item is not None:
        binary_tree = Set_Binary_Tree(iter(items))

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
# class BinaryTree:
#     # traversal order, ordered by increasing item key
#     def __init__(self, items: zip):
#         # Iterate through elements until the end
#         # Build direct access set with items, O(n)
#         self.num_items = 0
#         item = custom_next(items)
#         self.root = BinaryTree.Node(item)
#         print(f'root node {self.root}')
#         while item is not None:
#             self.num_items += 1
#             item = custom_next(items)
#             if item is not None:
#                 self.insert(item)
#         self.subtree_iter(self.root)
#         return
#
#     def __len__(self): return self.num_items
#     def __iter__(self):
#         if self.root:
#             for node in self .root.subtree_iter():
#             yield node.item
#     def __str__(self):
#         return ''
#     #     str_buffer = ['Set: [']
#     #     while node is not None:
#     #         if item is None:
#     #             str_buffer.append(',')
#     #         else:
#     #             str_buffer.append('\n\t\t' + str(item) + ',')
#     #     str_buffer.append(']')
#     #     join_str = ''.join(str_buffer)
#     #     return join_str
#
#     def build(X):
#         A = [x for x in X]
#
#         def build_subtree(self, i, j):
#             c = (i + j) // 2
#
#         root = self.Node_Type(A[c])
#         if i < c:  # needs to store more items in left subtree
#         root.left = build_subtree(self, i, c - 1)
#         root.left.parent = root
#         if c < j:  # needs to store more
#             root.right = build_subtree(self, c + 1, j)
#         root.right.parent = root
#         return root
#         items in right
#         subtree
#         self.root = build_subtree(self, 0, len(A) - 1)
#     def find(self, key):
#         return
#
#     def insert(self, item):
#         def put(self, key, val):
#             if self.root:
#                 self._put(key, val, self.root)
#             else:
#                 self.root = TreeNode(key, val)
#             self.size = self.size + 1
#
#         def _put(self, key, val, currentNode):
#             if key < currentNode.key:
#                 if currentNode.hasLeftChild():
#                     self._put(key, val, currentNode.leftChild)
#                 else:
#                     currentNode.leftChild = TreeNode(key, val, parent=currentNode)
#             else:
#                 if currentNode.hasRightChild():
#                     self._put(key, val, currentNode.rightChild)
#                 else:
#                     currentNode.rightChild = TreeNode(key, val, parent=currentNode)
#
#         node = self.root
#         print(f'root node {node}')
#
#         while node.left is not None:
#             if node.right is None:
#                 node.right = BinaryTree.Node(item)
#                 node.right.parent = node
#                 print(f'right node {node.right}')
#                 return
#             node = node.left
#         node.left = BinaryTree.Node(item)
#         node.left.parent = node
#         print(f'left node {node.left}')
#         return
#
#         # Visit right recursive until reach node None
#         # If left node is None, insert new node, return
#         return
#
#     def delete(self, key):
#         return
#
#     def find_min(self):
#         return
#
#     def find_max(self):
#         return
#
#     def find_prev(self, key):
#         return
#
#     def find_next(self, key):
#         return
#
#     @staticmethod
#     def validate():
#         # Get random integer keys
#         max_key = 10000
#         num_items = 50
#         key_data = np.random.randint(0, high=max_key, size=num_items)
#         # Get random values for items data
#         val_data = [string.ascii_letters[i] for i in range(num_items)]
#         print('key data', key_datself, '\nval_data', val_data)
#         # Create item list
#         items = [Item(k, v) for k, v in zip(key_datself, val_data)]
#         binary_tree = BinaryTree(iter(items))
#         import sys; sys.exit()
#         # Get fill prcnt
#         hash_table.get_fill_prcnt()
#         # find key
#         key = 7012  # key_data[2]
#         print(f'\tLooking for key={key}', end="")
#         item = hash_table.find(key)
#         print(f', Found {item}')
#
#         # insert key val pair
#         keys = [0, 1, 2, array_size - 1]  # np.random.randint(0, high=max_key, size=3)
#         val = 'U'
#         for key in keys:
#             hash_table.insert(Item(key, val))
#             print(f'\tInserting val {val} at {key}')
#         print('\t\t', hash_table)
#
#         # delete item with keys
#         for key in keys:
#             item = hash_table.delete(key)
#             print(f'\tDeleted item {item}')
#         print('\t\t', hash_table)
#         # find item with min key
#         min_item = hash_table.find_min()
#         print(f'\tFound item at min key {min_item}')
#         import sys;
#         sys.exit()
#         # todo implement find_max, ....
#         # find item with max key
#         max_item = hash_table.find_max()
#         print(f'\tFound item at max key {max_item}')
#         # find item after min key
#         next_item = hash_table.find_next(min_item.key)
#         print(f'\tFound item after to min key, {next_item}')
#         # find item before max key
#         prev_item = hash_table.find_prev(max_item.key)
#         print(f'\tFound item before max key, {prev_item}')
#         # find item before min key
#         prev_item = hash_table.find_prev(min_item.key)
#         print(f'\tFound item before min key, {prev_item}')
#         # find item after max key
#         next_item = hash_table.find_next(max_item.key)
#         print(f'\tFound item before max key, {next_item}')
