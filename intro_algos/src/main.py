import numpy as np
from graphs import Graph
from sets import DirectAccessArray, HashTable
from trees import Set_Binary_Tree
from seqncs import LinkedList
from sorts import mergesort_v1, quicksort, selectsort
from srchs import binary_search

def main():
    ####################################
    # Binary Tree Set Interface
    ####################################
    print('***** Implementation of Graphs, BFS, DFS')
    Graph.validate()
    import sys; sys.exit()

    ####################################
    # Binary Tree Set Interface
    ####################################
    print('***** Implementation of Binary Tree for set')
    Set_Binary_Tree.validate()
    #import sys; sys.exit()

    ####################################
    # Direct Access Array Set Interface
    ####################################
    print('***** Implementation of Direct Access Array for set')
    DirectAccessArray.validate()


    ####################################
    # Hash Table Set Interface
    # Uses LinkedList for collisions
    ####################################
    print('***** Implementation of Hash Table for set')
    HashTable.validate()
    import sys;
    sys.exit()




    ####################################
    # Binary Search
    ####################################
    print('***** Performing Binary Search')
    data = np.random.randint(0, high=100, size=25).tolist()
    # Sort data
    quicksort(data, debug_flg=False)
    val = data[12]
    indx = binary_search(data, val, debug_flg=True)
    print(f'\tBinary Search found val {val} at indx {indx}\n*****')
    val = max(data) + 1
    indx = binary_search(data, val, debug_flg=False)


    ####################################
    # Merge sort
    ####################################
    print('***** Performing Merge sort')
    data = np.random.randint(0, high=100, size=25).tolist()
    print('\tOrig Data[{l}]:'.format(l=len(data)), data)
    mergesort_v1(data, debug_flg=False)
    print('\tMergesorted Data:', data, '\n*****')

    ###########################
    # Quicksort
    ##############################
    print('***** Performing Quicksort')
    data = np.random.randint(0, high=100, size=5).tolist()
    print('\tOrig Data:', data)
    #partition_array(data)
    quicksort(data, debug_flg=False)
    print('\tQuicksorted Data:', data, '\n*****')

    ################################
    # Selection sort
    ####################################
    print('***** Performing Selection sort')
    data = np.random.randint(0, high=100, size=25).tolist()
    print('\tOrig Data:', data)
    selectsort(data)
    print('\tSelect sorted Data:', data, '\n*****')
    data = np.random.randint(0, high=100, size=25).tolist()
    print('\tOrig Data:', data)
    selectsort(data, recursive_flg=True)
    print('\tRecursive Select sorted Data:', data, '\n*****')

    ###################################
    # Radix sort
    #####################################

    ##############################
    # Linked List
    #######################################
    print('***** Implementation of Linked List for sequence')
    LinkedList.run()

    #######################################
    # Hash Table
    ########################################

if __name__ == '__main__':
    main()

