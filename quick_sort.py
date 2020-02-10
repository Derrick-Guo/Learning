"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def quicksort(array):
    if len(array)>1:    
        l=0
        p=len(array)-1
        while p-1>l:
            if array[l]>array[p]:
                array[p],array[p-1],array[l]=array[l],array[p],array[p-1]
                p-=1
            elif array[l]<=array[p]:
                l+=1
        if array[p]<array[l]:
            array[p],array[l]=array[l],array[p]
            p-=1
        array[p+1:len(array)]=quicksort(array[p+1:len(array)])
        array[0:p]=quicksort(array[0:p])
    return array
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))