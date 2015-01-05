
badList = [7,8,4,6,2,3,4,1];


def bubble_sort(data):
    n = len(data)
    swapped_elements = True
    while swapped_elements == True:
        swapped_elements = False
        for j in range(0, n-1):
            if data[j] > data[j+1]:
                swapped_elements = True
                data[j],data[j+1] = data[j+1],data[j]
    return data


goodList = bubble_sort(badList)

print goodList
