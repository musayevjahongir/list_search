def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i=1
    a=data[0]
    while i<len (data):
        if a>data[i]:
            a=data[i]
        i+=1
    return  data.count(a)
print(find_min_count([1, 8, 3, 8, 5]))
