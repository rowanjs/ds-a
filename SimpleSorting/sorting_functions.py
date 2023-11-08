from time import perf_counter

# bubble_li = [10,3,1,0,2,4,-1,5,9,8]
bubble_li = [4,3,5,10,1,7]

def how_long(func, li,n=1_000): #timing different sort functions
    placeholder = li
    start_time = perf_counter()
    for i in range(n):
        func(li)
        li = placeholder
    end_time = perf_counter()
    return end_time - start_time

def bubble_sort(li):
    n = len(li)-1
    while n > 0:
        for i in range(n):
            if li[i] > li[i+1]: #if next element bigger then swap
                li[i], li[i+1] = li[i+1], li[i]
                                #if not bigger then no action but move on to next element
        n -= 1                  #largest in list would bubble to n-1 index so ignore in next loop
    return li

print(f'Ran bubble sort\n{bubble_sort(bubble_li)}')
print(how_long(bubble_sort,bubble_li))

# sel_list = [10,3,1,0,2,4,-1,5,9,8]
sel_list = [4,3,5,10,1,7]

def selection_sort(li): #selection sort reduces the number of swaps to N instead of N^2
    for start in range(len(li)-1):
        minim = start
        for i in range(start+1,len(li)):
            if li[i] < li[minim]:
                minim = i
        li[start], li[minim] = li[minim], li[start]
    return li

print(f'Ran selection sort\n{selection_sort(sel_list)}')
print(how_long(selection_sort,sel_list))

# insert_li = [10,3,1,0,2,4,-1,5,9,8]
insert_li=[4,3,5,10,1,7]
def insertion_sort(li):
    for i in range(1, len(li)):
        val = li[i]
        run_count = i
        while run_count > 0 and li[run_count-1] > val:
            li[run_count] = li[run_count-1]
            run_count -= 1
        li[run_count] = val
    return li 
print(f'Ran insertion sort\n{insertion_sort(insert_li)}')
print(how_long(insertion_sort,insert_li))




