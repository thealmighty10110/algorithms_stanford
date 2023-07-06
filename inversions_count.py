def mergeAndCount(a):
    n = len(a)
    if n == 1:
        return a, 0
    else:
        b, x= mergeAndCount(a[:n//2])
        c, y= mergeAndCount(a[n//2:])
        d, z=a,0
        i,j=0,0
        for k in range(0,n):
            # print(i,j)
            if (i < n//2) & (j < n//2):
                if (b[i] < c[j]):
                    d[k] = b[i] 
                    i+=1
                elif (b[i] > c[j]):
                    d[k] = c[j]
                    j+=1
                    z+= len(b[i:])
            else:
                if(i == n//2): 
                    d[k] = c[j]
                    j+=1
                elif(j == n//2):
                    d[k] = b[i]
                    i+=1
                    
        print('Merged array: ', d)
        return d, x+y+z

arr1 = [1,3,5,2,4,6]
print(mergeAndCount(arr1))
arr2 = [1]
print(mergeAndCount(arr2))
arr3 = [3,1]
print(mergeAndCount(arr3))