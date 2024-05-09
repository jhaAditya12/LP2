def selection_sort(a):
    for i in range(len(a)-1):
        min_index=i
        for j in range(i,len(a)):
            if a[min_index]>a[j]:
                min_index=j
        a[i],a[min_index] = a[min_index],a[i]
        print(a)
        

a=[8,9,2,1,10,3,5] 
print("unsorted Array : ",a)
selection_sort(a)
print("Sorted Array ",a)















