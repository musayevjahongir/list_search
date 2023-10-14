def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i=1
    a=0
    while i<len (data):
        a=data[0]
        if data[i]>a:
            a=data[i]
        i+=1
    return a
print(find_max([1, 2, 3,9, 4, 5,7]))
    