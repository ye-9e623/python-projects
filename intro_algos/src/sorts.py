
def partition_with_last_element(data: list, strt_indx: int=0, end_indx: int=None, debug_flg=False) -> list:
    ''' Partition array

    Move all elements less than pivot to the left of pivot
    Move all elements greater than pivot to the right of pivot
    time complexity O(n), space complexity O(1)

    Arguments:
        data: iterable to partition
    Returns:
        index of pivot
    '''
    if end_indx is None:
        end_indx = len(data) - 1
    if debug_flg: print('Initial data', data, '[{s},{e}]'.format(s=strt_indx, e=end_indx))
    lt_indx = strt_indx # max index of less than pivot group
    pvt_indx = end_indx
    #pvt_indx = (strt_indx + end_indx) // 2 # middle index
    pvt = data[pvt_indx]
    # iterate through data
    # if data[i] >= pvt, increment i
    # else data[i] < pvt, swap data[i] and lt_indx, increment lt_indx, i
    if debug_flg: print(f'Pivot indx: {pvt_indx}, Pivot: {pvt}')
    for i in range(strt_indx, end_indx): # O(n)
        if data[i] >= pvt:  #O(1)
            if debug_flg: print('\tAdd {d} to gt group'.format(d=data[i]), data)
        else:
            data[lt_indx], data[i] = data[i], data[lt_indx] #O(1)
            lt_indx += 1
            if debug_flg: print('\tAdd {d} to lt group'.format(d=data[i]), data)
    # swap pivot with lt_indx + 1
    data[lt_indx], data[end_indx] = pvt, data[lt_indx]
    if debug_flg: print('Paritioned data:', data, 'pvt_indx', lt_indx)
    return lt_indx

def quicksort(data: list, strt_indx:int=None, end_indx:int=None, debug_flg=False):
    ''' quiksort in-place

    Arguments:
        data: unordered iterable
    '''
    if strt_indx is None: strt_indx = 0
    if end_indx is None: end_indx = len(data) - 1
    # Base case
    if strt_indx > end_indx:
        return
    # DIVIDE: Partition less than and greater than pivot group separately
    pvt_indx = partition_with_last_element(data, strt_indx=strt_indx,
                                           end_indx=end_indx, debug_flg=debug_flg)
    # CONQUER: Recursive case
    if strt_indx < pvt_indx - 1:
        quicksort(data, strt_indx, pvt_indx-1, debug_flg=debug_flg)
    if pvt_indx + 1 < end_indx:
        quicksort(data, pvt_indx+1, end_indx, debug_flg=debug_flg)

#TODO add partition_with_median

def find_max_indx(data: list, indx) -> int:
    ''' get maximum
    Arguments:
    Returns: '''
    max_indx = 0
    max_val = data[max_indx]
    for i, val in enumerate(data[1:indx], start=1):
        if data[i] > max_val:
            max_indx = i
            max_val = data[max_indx]
    return max_indx

def selectsort(data: list, recursive_flg: bool=False, indx: int=None, debug_flg: bool=False):
    ''' Selection sort inplace

    Find largest item in unsorted portion of array and
    move it to end (beginning of sorted portion, O(n^2) '''
    if indx is None:
        indx = len(data)
    # Base case
    base_case_threshold = 2
    if indx < base_case_threshold:
        indx -= 1
        return

    if not recursive_flg:
        while indx >= base_case_threshold:
            max_indx = find_max_indx(data, indx)
            # swap max element to end (beginning of sorted portion of array)
            data[indx-1], data[max_indx] = data[max_indx], data[indx-1]
            if debug_flg: print(f'Finding max btw data[0,{indx}] and swapping', data)
            indx -= 1
    else:
        # Recursive case
        max_indx = find_max_indx(data, indx)
        # swap max element to end (beginning of sorted portion of array)
        data[indx - 1], data[max_indx] = data[max_indx], data[indx - 1]
        if debug_flg: print(f'Finding max btw data[0,{indx}] and swapping', data)
        indx -= 1
        selectsort(data, recursive_flg=True, indx=indx)

def mergesort_v1(data: list, debug_flg=False):
    ''' Merge sort

    O(NlogN), stable, not in-place sort
    Arguments:
     data:
     debug_flg:
    '''
    if debug_flg: print('\tInitial data, len={l} :'.format(l=len(data)), data)
    # Base case
    base_case_threshold = 2
    if len(data) < base_case_threshold:
        return
    # DIVDE: divide at midpoint, O(logn)
    midpnt_indx = len(data) // 2
    low_data = data[:midpnt_indx] #todo, change to use slicing in mergesort, need to pass srtd_data helper array
    high_data = data[midpnt_indx:]
    if debug_flg:
        print(f'\tDivide at midpoint {midpnt_indx}')
        print('\t\tLow half:', low_data, '\n\t\tHigh half:', high_data)
    # CONQUER: Recursive case
    mergesort_v1(low_data)
    mergesort_v1(high_data)
    # MERGE:
    merge_and_sort_v1(low_data, high_data, data)

def merge_and_sort_v1(data1: list, data2: list, srtd_data, debug_flg=False):
    ''' Merge data1 and data2
    Assume data1 and data2 are sorted
    Sort data1 and data2 while merging'''
    len_data1 = len(data1)
    len_data2 = len(data2)
    srtd_indx = 0
    data1_indx = 0
    data2_indx = 0
    if debug_flg: print('\tMerge and sort data1({l1}) & data2({l2}):'.format(l1=len_data1, l2=len_data2),
          '\n\t', data1, '\n\t', data2)
    # while we have not reached the end of data1 or data2
    while data1_indx < len_data1 and data2_indx < len_data2:
        # if the current element of data1 < current element of data2
        # then add the current element of data1 to the sorted array
        if data1[data1_indx] <= data2[data2_indx]:
            srtd_data[srtd_indx] = data1[data1_indx]
            data1_indx += 1
        else:
            srtd_data[srtd_indx] = data2[data2_indx]
            data2_indx += 1
        srtd_indx += 1
    # Copy remaining portion of non-empty array to the sorted array
    while data1_indx < len_data1:
        srtd_data[srtd_indx] = data1[data1_indx]
        data1_indx += 1
        srtd_indx += 1
    while data2_indx < len_data2:
        srtd_data[srtd_indx] = data2[data2_indx]
        data2_indx += 1
        srtd_indx += 1
    if debug_flg: print('\t\tMerged data({l}):'.format(l=len(srtd_data)), srtd_data)
    return srtd_data

def mergesort_v2(data: list, debug_flg=False):
    ''' Merge sort

    O(NlogN), stable, not in-place sort
    Arguments:
     data:
     debug_flg:
    '''
    if debug_flg: print('\tInitial data, len={l} :'.format(l=len(data)), data)
    # Base case
    base_case_threshold = 2
    if len(data) < base_case_threshold:
        return
    # DIVDE: divide at midpoint, O(logn)
    midpnt_indx = len(data) // 2
    low_data = data[:midpnt_indx] #todo, change to use slicing in mergesort, need to pass srtd_data helper array
    high_data = data[midpnt_indx:]
    if debug_flg:
        print(f'\tDivide at midpoint {midpnt_indx}')
        print('\t\tLow half:', low_data, '\n\t\tHigh half:', high_data)
    # CONQUER: Recursive case
    mergesort_v2(low_data)
    mergesort_v2(high_data)
    # MERGE: Step through n items
    merge_and_sort_v2(low_data, high_data, data)


def merge_and_sort_v2(data1: list, data2: list, srtd_data, debug_flg=False):
    ''' Merge data1 and data2
    Assume data1 and data2 are sorted
    Sort data1 and data2 while merging'''
    len_data1 = len(data1)
    len_data2 = len(data2)
    srtd_indx = 0
    data1_indx = 0
    data2_indx = 0
    if debug_flg: print('\tMerge and sort data1({l1}) & data2({l2}):'.format(l1=len_data1, l2=len_data2),
          '\n\t', data1, '\n\t', data2)
    # while we have not reached the end of data1 or data2
    while data1_indx < len_data1 and data2_indx < len_data2:
        # if the current element of data1 < current element of data2
        # then add the current element of data1 to the sorted array
        if data1[data1_indx] <= data2[data2_indx]:
            srtd_data[srtd_indx] = data1[data1_indx]
            data1_indx += 1
        else:
            srtd_data[srtd_indx] = data2[data2_indx]
            data2_indx += 1
        srtd_indx += 1
    # Copy remaining portion of non-empty array to the sorted array
    while data1_indx < len_data1:
        srtd_data[srtd_indx] = data1[data1_indx]
        data1_indx += 1
        srtd_indx += 1
    while data2_indx < len_data2:
        srtd_data[srtd_indx] = data2[data2_indx]
        data2_indx += 1
        srtd_indx += 1
    if debug_flg: print('\t\tMerged data({l}):'.format(l=len(srtd_data)), srtd_data)
    return srtd_data

def radix_sort(data):
    pass
