def merge(A, B):
    # Loop through all elements of both lists
    result = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i = i + 1
        else:
            result.append(B[j])
            j = j + 1
    while i < len(A):
        result.append(A[i])
        i = i + 1
    while j < len(B):
        result.append(B[j])
        j = j + 1

    return result


def sort(A):
    # If we have only 1 element, return it
    if len(A) < 2:
        return A

    # Split up the lists into two sublists
    mid = len(A) / 2
    left = A[:mid]
    right = A[mid:]

    # Recursively call sort on the sublists
    left, right = sort(left), sort(right)

    # Finally, merge the sorted sublists
    return merge(left, right)

listNeedToBeShort =  [1,4, 2, 7,6,8]
shortList = sort(listNeedToBeShort)
print shortList 
