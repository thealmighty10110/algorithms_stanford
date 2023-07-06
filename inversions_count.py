def mergeAndCount(a):
    if len(a) == 1:
        print('NO INVERSION')
        return 0
    else:
        count = 0
        n = len(a)
        print(n)
        if n == 2:
            if a[0] > a[1]:
                temp = a[0]
                a[0] = a[1]
                a[1] = temp
                return 1
            else:
                return 0
        else:
            b = a[:(n//2)]
            print(b)
            c = a[(n//2):]
            print(c)
            count+=mergeAndCount(b)
            count+=mergeAndCount(c)
            i,j=0,0
            print(n//2)
            for k in range(0,n):
                print(i,j)
                if (i < n//2+1) | (j < n//2+1):
                    if (b[i] < c[j]):
                        a[k] = b[i]
                        i+=1
                    elif (b[i] > c[j]):
                        a[k] = c[j]
                        j+=1
                        count+= len(b[i:])
                else:
                    if(i == n//2): a.extend(c[j:])
                    elif(j == n//2): a.extend(b[i:])
            return count

    print('Merged array: ', a)
    return count

arr1 = [1,3,5,2,4,6]
print(mergeAndCount(arr1))
arr2 = [1]
print(mergeAndCount(arr2))
arr3 = [3,1]
print(mergeAndCount(arr3))