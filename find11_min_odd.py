def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i=1
    a=data[0]
    while i<len (data):
        if data[i]%2==1:
            if a>data[i]:
                a=data[i]
        i+=1
    return a
print(find_min_odd([1, 8, 2, 8, 5]))

