# coding: utf-8

def first_index_of(sorted_name_list, name, start=0):
    '''获取排序列表sorted_name_list中指定名称元素的位置

    如果元素name在sorted_name_list中存在，则返回其下标，
    下标从0开始计数；如果不存在，则返回-1.

    >>> first_index_of([1,2,3], 1)
    0
    >>> first_index_of([1,2,3], 5)
    -1

    '''
    try:
        return sorted_name_list.index(name)
    except ValueError as e:
        return -1
        
