import numpy as np
import string
from sets import Item, custom_next
from seqncs import Queue, Stack
np.random.seed(0)


def dfs(graph, source_key, stack=None, reverse_topological_order=0, debug_flg=False):
    ''' Depth-first search
    '''
    vertex = graph.vertices[source_key]
    # initialize stack with source vertex
    if stack is None:
        stack = Stack()
        stack.push(vertex)
        vertex.set_visited_flg(True)
        # Update dictionary with vertex visited flag
        graph.vertices.update({vertex.key: vertex})
    while not stack.is_empty():
        #print(stack)
        vertex = stack.pop()
        print(f'{reverse_topological_order} Visited {vertex}')
        # sort edges list, edges were not added to the graph in lexical order
        sorted_edges = sorted(graph.edges[vertex.key], key=lambda x: x.to_vertex_key)
        # Print list of edges
        if debug_flg:
            str_buffer = []
            str_buffer.append(f'\tEdges of {vertex.key}: ')
            for edge in sorted_edges:
                str_buffer.append(f'{edge} ')
            print(''.join(str_buffer))
        # Loop through outgoing adjacency list correspond popped vertex
        # Recursively visit the vertices in adjacency list of each edge's to_vertex
        reverse_topological_order += 1
        for edge in sorted_edges:
            edge_vertex = graph.vertices[edge.to_vertex_key]
            if not edge_vertex.visited_flg:
                edge_vertex.set_visited_flg(True)
                edge_vertex.parent = vertex.key
                edge_vertex.order = reverse_topological_order + 1
                # Update dictionary with vertex
                graph.vertices.update({edge.to_vertex_key: edge_vertex})
                print('\t\t', end='')
                # Recursive call
                reverse_topological_order = dfs(graph, vertex.key,
                                                stack,
                                                reverse_topological_order=reverse_topological_order,
                                                debug_flg=False)
                stack.push(edge_vertex)
        #print(f'\tPushed {vertex}')
    return reverse_topological_order

def bfs(graph, source_key):
    ''' Breadth-first search
    '''
    queue = Queue()
    #print(graph)
    vertex = graph.vertices[source_key]
    vertex.set_visited_flg(True)
    # Update dictionary with vertex
    item = vertex.item
    graph.vertices.update({item.key: vertex})
    # initialize queue with source node item
    queue.enqueue(item)
    while not queue.is_empty():
        #print(queue)
        item = queue.dequeue()
        vertex = graph.vertices[item.key]
        print(f'Visited {vertex}')
        # Loop through outgoing adjacency matrix correspond to item key
        for edge in graph.edges[item.key]:
            #print('\tEdge', edge)
            edge_vertex = graph.vertices[edge.to_vertex_key]
            if not edge_vertex.visited_flg:
                edge_vertex.set_visited_flg(True)
                edge_vertex.parent = vertex.item.key
                edge_vertex.level = vertex.level + 1
                # Update dictionary with vertex
                graph.vertices.update({edge.to_vertex_key: edge_vertex})
                item = edge_vertex.item
                queue.enqueue(item)
                #print(f'\tEnqueued {vertex}, {item}')



class Vertex:
    ''' Vertex class to store key val pair '''

    def __init__(self, item: Item):
        self.key = item.key
        self.item = item
        self.visited_flg = False
        self.level = 0
        self.parent = None
        self.order = 0

    def __str__(self):
        return f'Vertex(key={self.key}, item={self.item}, ' \
               f'visited={self.visited_flg}, level={self.level}, ' \
               f'parent={self.parent}, order={self.order})'

    def set_visited_flg(self, flg):
        self.visited_flg = flg

class Edge:
    ''' Edge class to store from and to Vertex, plus weight '''
    def __init__(self, from_vertex_key: int, to_vertex_key: int, weight=0):
        self.from_vertex_key = from_vertex_key
        self.to_vertex_key = to_vertex_key
        self.weight = weight

    def __str__(self):
        return f'Edge({ self.from_vertex_key}->{self.to_vertex_key} with weight={self.weight})'


class Graph:
    FROM_VERTEX_INDX = 0
    TO_VERTEX_INDX = 1

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0
        # list of outgoing edges from each vertex, dictionary
        # outgoing adjacency dictionary with vertex key as key
        self.edges = {}
        self.num_edges = 0

    def __str__(self):
        str_buffer = []
        for key, vertex in self.vertices.items():
            str_buffer.append(vertex.__str__())
            for edge in self.edges[key]:
                str_buffer.append('\t{e}'.format(e=edge.__str__()))
        return '\n'.join(str_buffer)

    def add_vertex(self, item: Item):
        self.vertices[item.key] = Vertex(item)
        self.edges[item.key] = []
        self.num_vertices += 1

    def add_edge(self, from_vertex_key: int, to_vertex_key: int, weight=None):
        self.edges[from_vertex_key].append(Edge(from_vertex_key, to_vertex_key, weight))
        self.num_edges += 1

    def get_vertex(self, key):
        return self.vertices[key]

    def get_vertices(self):
        return self.vertices.copy()

    def clear_parents(self):
        ''' Clear all parents found during bfs or dfs '''
        for key, vertex in self.vertices.items():
            vertex.parent = None
            # Update dictionary with vertex
            self.vertices.update({key: vertex})
    def clear_visits(self):
        ''' Clear all visits assigned during bfs or dfs '''
        for key, vertex in self.vertices.items():
            vertex.set_visited_flg(False)
            # Update dictionary with vertex
            self.vertices.update({key: vertex})
    def clear_levels(self):
        ''' Clear all levels found during bfs '''
        for key, vertex in self.vertices.items():
            vertex.level = 0
            # Update dictionary with vertex
            self.vertices.update({key: vertex})
    def clear_orders(self):
        ''' Clear all orders found during dfs'''
        for key, vertex in self.vertices.items():
            vertex.order = 0
            # Update dictionary with vertex
            self.vertices.update({key: vertex})
    @staticmethod
    def validate():
        print('\n************ Validating Build Graph')
        # Create items
        key_data = range(6)
        num_items = len(key_data)
        # Get random values for items data
        val_data = [string.ascii_letters[i] for i in range(num_items)]
        print('key data', key_data, '\nval_data', val_data)
        # Create item list
        items = [Item(k, v) for k, v in zip(key_data, val_data)]
        items_iter = iter(items)
        edges = iter([(0,1), (0, 4), (0, 5), (1, 4), (1, 3), (2, 1), (3, 2), (3, 4)])
        graph = Graph()
        curr_item = custom_next(items_iter)
        while curr_item is not None:
            graph.add_vertex(curr_item)
            curr_item = custom_next(items_iter)
        curr_edge = custom_next(edges)
        while curr_edge is not None:
            graph.add_edge(curr_edge[Graph.FROM_VERTEX_INDX],
                           curr_edge[Graph.TO_VERTEX_INDX])
            curr_edge = custom_next(edges)
        print(graph)
        print('\n************ Depth-First Search starting with source 0')
        dfs(graph, 0)
        # Clean up vertex augmentation
        graph.clear_parents()
        graph.clear_visits()
        graph.clear_levels()
        graph.clear_orders()
        print('\n************ Breadth-First Search starting with source 0')
        bfs(graph, 0)
        print('\n********** Validating Queue class *******')
        queue = Queue()
        items_iter = iter(items)
        curr_item = custom_next(items_iter)
        while curr_item is not None:
            queue.enqueue(curr_item)
            curr_item = custom_next(items_iter)
        print(queue)
        num_delete = 3
        print(f'Dequeuing {num_delete} items')
        for num in range(3):
            item = queue.dequeue()
            print(f'\tDequeue {item}')
        print(queue)
        print('\n********** Validating Stack class *******')
        stack = Stack()
        items_iter = iter(items)
        curr_item = next(items_iter)
        while curr_item is not None:
            stack.push(curr_item)
            curr_item = custom_next(items_iter)
        print(stack)
        print(f'Popping {num_delete} items')
        for num in range(3):
            item = stack.pop()
            print(f'\tPopped {item}')
        print(stack)





