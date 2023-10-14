def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i=1
    a=data[i]
    while i<len (data):
        if data[i]%2==0:
            if a>data[i]:
                a=data[i]
        i+=1
    return a 
print(find_min_even([1, 8, 2, 8, 5]))

