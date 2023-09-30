# BUBBLE SORT
# Time Complexity: O(n^2)

def bubble_sort(dataset, order):
    if order == "asc":
        sorted = False
        while not sorted:
            for i in range(len(dataset)-1):
                sorted = True
                if dataset[i] > dataset[i+1]:
                    sorted = False
                    temp = dataset[i]
                    dataset[i] = dataset[i+1]
                    dataset[i+1] = temp
    elif order == "desc":
        sorted = False
        while not sorted:
            for i in range(len(dataset)-1):
                sorted = True
                if dataset[i] < dataset[i+1]:
                    sorted = False
                    temp = dataset[i]
                    dataset[i] = dataset[i+1]
                    dataset[i+1] = temp
    else:
        print("Invalid order. Please enter 'asc' or 'desc'.")
        return
    
    return dataset

# SELECTION SORT
# Time Complexity: O(n^2)

def findSmallestIdx(i, dataset):
    imin = i
    for j in range(i+1, len(dataset)):
        if dataset[j] < dataset[imin]:
            imin = j
    return imin

def findBiggestIdx(i, dataset):
    imax = i
    for j in range(i+1, len(dataset)):
        if dataset[j] > dataset[imax]:
            imax = j
    return imax

def swap(i, j, dataset):
    temp = dataset[i]
    dataset[i] = dataset[j]
    dataset[j] = temp

def selection_sort(dataset, order):
    if order == "asc":
        for i in range(len(dataset)):
            imin = findSmallestIdx(i, dataset)
            swap(i, imin, dataset)
    elif order == "desc":
        for i in range(len(dataset)):
            imax = findBiggestIdx(i, dataset)
            swap(imax, i, dataset)
    else:
        print("Invalid order. Please enter 'asc' or 'desc'.")
        return
    
    return dataset


# INSERTION SORT
# Time Complexity: O(n^2)

def insertAsc(val, dataset, hi):
    for i in range(hi-1, -1,-1):
        if val < dataset[i]:
            dataset[i+1] = dataset[i]
        else:
            dataset[i+1] = val
            return
    dataset[0] = val

def insertDesc(val, dataset, hi):
    for i in range(hi-1, -1,-1):
        if val > dataset[i]:
            dataset[i+1] = dataset[i]
        else:
            dataset[i+1] = val
            return
    dataset[0] = val

def insertion_sort(dataset, order):
    if order == "asc":
        for i in range(1, len(dataset)):
            insertAsc(dataset[i], dataset, i)
    elif order == "desc":
        for i in range(1, len(dataset)):
            insertDesc(dataset[i], dataset, i)
    else:
        print("Invalid order. Please enter 'asc' or 'desc'.")
        return
    
    return dataset


# MERGE SORT
# Time Complexity: O(n log n)

def merge_sort(dataset, order):
    return

def merge(A, B, order):
    return

# QUICK SORT
# Time Complexity: O(n log n)



# TEST CASES
A = [9,1,2,8,0,-1,13]
print(insertion_sort(A, "desc"))