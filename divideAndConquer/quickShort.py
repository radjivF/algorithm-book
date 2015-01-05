def qsort(L):
   if L == []: return []
   return qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + \
          qsort([x for x in L[1:] if x>=L[0]])


listNeedToBeShort =  [1,4, 2, 7,6,8]
shortList = qsort(listNeedToBeShort)
print shortList
