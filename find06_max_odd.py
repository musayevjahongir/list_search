def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    a=0
    while i<len (data):
        if a<data[i]:
            if data[i]%2:
                a=data[i]
        i+=1
    if a:
        return a
    else:
        return -1
print(find_max_odd([11, 7, 5, 4, 9]))