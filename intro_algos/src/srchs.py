

def binary_search(data: list, x: int, strt_indx: int=0, end_indx: int=None, debug_flg=False):
    ''' Binary search of data 
    
    Data must be sorted
    Arguments:
    Returns:
        indx: index of x, None if x is not in array
    '''
    if strt_indx is None: strt_indx = 0
    if end_indx is None: end_indx = len(data)
    # Loop version
    while strt_indx < end_indx:
        midpnt_indx = (end_indx + strt_indx) // 2
        if debug_flg: print('Searching for x:{x} data[{s}:{m}]='.format(x=x, s=strt_indx, m=midpnt_indx-1),
              data[strt_indx:midpnt_indx - 1],
              f', data[{midpnt_indx}]=', data[midpnt_indx],
               ', data[{m}:{e}]='.format(m=midpnt_indx+1, e=end_indx), data[midpnt_indx + 1:end_indx])
        if x == data[midpnt_indx]:
            return midpnt_indx
        elif x < data[midpnt_indx]:
            end_indx = midpnt_indx
        else:
            strt_indx = midpnt_indx + 1
    # X is not in the array
    print('{x} not found in array [{a},{b}]'.format(x=x, a=data[0], b=data[-1]))

    # # Recursive version
    # # Divide
    # midpnt_indx = strt_indx + (end_indx - strt_indx) // 2
    # if debug_flg: print(f'Searching for x:{x} data[{strt_indx}:{midpnt_indx}-1]', data[strt_indx:midpnt_indx - 1],
    #       f'data[{midpnt_indx}+1:{end_indx}]', data[midpnt_indx + 1:end_indx])
    # # If x is less than data at midpoint search lower array
    # if x < data[midpnt_indx]:
    #     return binary_search(data, x, strt_indx, midpnt_indx-1)
    # # Else if x is greater than data at midpoint search upper array
    # elif x > data[midpnt_indx]:
    #     return binary_search(data, x, midpnt_indx+1, end_indx)
    # # Else check if x is at midpoint
    # elif x == data[midpnt_indx]:
    #     return midpnt_indx
    # # X is not in the array
    # print('{x} not found in array [{a},{b}]'.format(x=x, a=data[0], b=data[-1]))


