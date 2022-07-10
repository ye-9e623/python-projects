import numpy as np
import string
from sets import Item, custom_next
np.random.seed(0)


class Vertex:
    ''' Vertex class to store key val pair '''

    def __init__(self, item: Item):
        self.key = item.key
        self.item = item
        self.visited_flg = False

    def __str__(self):
        return f'Vertex(key={self.key}, item={self.item}, visited={self.visited_flg})'


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

    @staticmethod
    def validate():
        # Create items
        key_data = range(6)
        num_items = len(key_data)
        # Get random values for items data
        val_data = [string.ascii_letters[i] for i in range(num_items)]
        print('key data', key_data, '\nval_data', val_data)
        # Create item list
        items = iter([Item(k, v) for k, v in zip(key_data, val_data)])
        edges = iter([(0,1), (0, 4), (0, 5), (1, 4), (1, 3), (2, 1), (3, 2), (3, 4)])
        graph = Graph()
        curr_item = next(items)
        while curr_item is not None:
            graph.add_vertex(curr_item)
            curr_item = custom_next(items)
        curr_edge = next(edges)
        while curr_edge is not None:
            graph.add_edge(curr_edge[Graph.FROM_VERTEX_INDX],
                           curr_edge[Graph.TO_VERTEX_INDX])
            curr_edge = custom_next(edges)
        print(graph)

        print('************ Breadth-First Search starting with source 0')
        bfs(graph, 0)
        import sys; sys.exit()
        print('********** Validating Queue class *******')
        queue = Queue()
        items = iter([Item(k, v) for k, v in zip(key_data, val_data)])
        curr_item = next(items)
        while curr_item is not None:
            queue.enqueue(curr_item)
            curr_item = custom_next(items)
        print(queue)
        for num in range(3):
            item = queue.dequeue()
            print(f'\tDequeue {item}')
        print(queue)


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
        str_buffer = []
        node = self.first
        while node.next is not None:
            str_buffer.append('\t{i}'.format(i=node.item.__str__()))
            node = node.next
        return '\n'.join(str_buffer)
    def isEmpty(self):
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

def bfs(graph, source_key):
    queue = Queue()
    graph.vertices[source_key].visited_flg = True
    print(graph)
    item = graph.vertices[source_key].item
    queue.enqueue(item)

    while not queue.isEmpty():
        item = queue.dequeue()
        print(f'Visited {item}')

            for edge in graph.edges[item.key]:
                if not graph.vertices[edge.to_vertex_key].visited_flg:
                    graph.vertices[edge.to_vertex_key].visted_flg = True
                    print(graph)
                    item = graph.vertices[edge.to_vertex_key].item
                    queue.enqueue(item)
        breakpoint()