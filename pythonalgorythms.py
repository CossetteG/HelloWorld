def valid_list(lyst):
    if type(lyst) != list:
        raise TypeError("lyst must be a list")
        
    for item in lyst:
        if type(item) != int:
            raise TypeError("all list elements must be an integer")

    return lyst

def is_sorted(lyst):
    j = -1
    
    for i in (lyst):
        if j == -1:
            pass
        elif i < lyst[j]:
            #print(i, lyst[j]) #this is to see the comparison
            return False
            
        j += 1
        
    return True
    
def quicksort(lyst):
    copy = valid_list(lyst)
    comparisons = 0
    swaps = 0

    
    def partition(section):
        high_idx = len(section)-1
        low_idx = 0
        midpoint = (high_idx + low_idx) // 2
        nonlocal swaps
        nonlocal comparisons
        pivot = section[midpoint]
        
        done = False
        while (done==False):
            while (section[low_idx] < pivot):
                comparisons += 1
                low_idx += 1
                
            while (section[high_idx] > pivot):
                comparisons +=1
                high_idx -= 1
                
            if (low_idx >= high_idx):
                done = True
            else:
                temp = section[low_idx]
                section[low_idx] = section[high_idx]
                section[high_idx] = temp
                swaps += 1
        
        if (len(section) > 2):
            low_section = partition(section[0:low_idx])
            high_section = partition(section[high_idx:])
            return low_section + high_section
        else:
            return section

    return (partition(lyst), comparisons, swaps)

def selection_sort(lyst):
    copy = valid_list(lyst)
    comparisons = 0
    swaps = 0
    
    size = len(lyst)
    
    for i in range(size):
        smol = i
        
        for j in range(i+1, size):
            comparisons += 1
            if lyst[smol] > lyst[j]:
                smol = j
        
        if (lyst[i] != lyst[smol]):
            swaps += 1
            temp = lyst[i]
            lyst[i] = lyst[smol]
            lyst[smol] = temp
        
    return (lyst, comparisons, swaps)
    
    
def insertion_sort(lyst):
    copy = valid_list(lyst)
    comparisons = 0
    swaps = 0
    
    size = len(lyst)
    
    for i in range(1, size):
        j = i
        
        while ((j > 0) and (lyst[j-1] > lyst[j])) :
            comparisons += 1
            swaps += 1
            
            temp = lyst[j]
            lyst[j] = lyst[j-1]
            lyst[j-1] = temp
            j -= 1
        
        comparisons += 1
    
    return (lyst, comparisons, swaps)
    
def mergesort(lyst):
    copy = valid_list(lyst)
    comparisons = 0
    swaps = 0
    
    def merge_partxn(lyst):
        size = len(lyst)
        midpoint = size // 2
        nonlocal comparisons
        nonlocal swaps
        
        if (size <= 2):
            return lyst
        
        left = []
        right = []
        
        for i in lyst:
            comparisons +=1
            if (i < lyst[midpoint]):
                left = left + [i]
            else:
                right = right + [i]
    
        return merge_partxn(left) + merge_partxn(right)
    
    result = merge_partxn(lyst)
    for i in range(0, len(lyst)-1, 2):
        if (result[i] > result[i+1]):
            swaps +=1
            temp = result[i]
            result[i]= result[i+1]
            result[i+1] = temp

    return (result, comparisons, swaps)


def main():
    testlyst1 = [6, 5, 4, 3, 1, 2]
    testlyst2 = [1, 2, 3, 4, 0]
    testlyst3 = 'a'
    testlyst4 = [8, 'a', 5]
    
    # print(is_sorted(testlyst1))
    # print(is_sorted(testlyst2))
    # print(quicksort(testlyst2))
    print(mergesort(testlyst2))


if __name__ == "__main__":
    main()