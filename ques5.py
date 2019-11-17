def search(arr ,start, last, key):
    if (last >= start ):
     #   print("hello")
        
        mid =int((start +last)/2)
       # print(mid)

        if(arr[mid]== key):
            return mid
        elif (arr[mid] > key ):
            return search( arr,start,mid-1,key)
        else:
            return search( arr, mid+1, last,key)
    else:
        #print("world")
        return -1



arr = [1,2,3,5,9,10,12]

print(search(arr,0,6,99))



        
