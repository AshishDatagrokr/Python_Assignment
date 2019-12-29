""" Implementing Binary Search """
# pylint: disable=no-else-return
def search(array, start, last, key):
    """ defining search function """
    if last >= start:
     #   print("hello")

        mid = int((start +last)/2)
       # print(mid)

        if array[mid] == key:
            return mid
        elif array[mid] > key:
            return search(array, start, mid-1, key)
        else:
            return search(array, mid+1, last, key)
    else:
        #print("world")
        return -1

ARRAY = [1, 2, 3, 5, 9, 10, 12]
print(search(ARRAY, 0, 6, 99))
