def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    i=0
    a=0
    while i<len (data):
        if a<data[i]:
            if data[i]%2==0:
                a=data[i]
        i+=1
    return a
print(find_max_even([1, 4, 3, 8, 5]))
