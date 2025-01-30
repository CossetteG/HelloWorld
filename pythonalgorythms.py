from random import seed, sample

def make_data(data_size):#DO NOT REMOVE OR MODIFY THIS FUNCTION
    '''A generator for producing data_size random values
    '''
    seed(0)
    data = sample(range(data_size * 3), k=data_size)
    data.sort()
    while True:
        yield data

def linear_search(lyst, target, comparisons=0):
    for i in lyst:
        comparisons +=1
        if (target == i):
            return [True,comparisons]
            
    return [False, comparisons]

def binary_search(lyst, target, comparisons=0):
    comparisons +=1
    mid = lyst[len(lyst)//2]
    

    if (mid == target):
        return [True, comparisons]
    elif (len(lyst) == 1):
        return [False, comparisons]
    elif (mid > target):
        return binary_search(lyst[0:len(lyst)//2], target, comparisons)
    elif (mid < target):
        return binary_search(lyst[len(lyst)//2: len(lyst)], target, comparisons)
            

def jump_search(lyst, target):
    skip = 4
    section = 0
    comparisons = 0

    if (target > lyst[len(lyst)-1]):
        return [False, 1]
    elif (target < lyst[0]):
        return [False, 1]
    
    while (lyst[section] <= target):
        comparisons +=2
        if (lyst[section] == target):
            return [True, comparisons]
        
        section += skip
        if (section >= len(lyst)):
            break
    
    return linear_search(lyst[section-skip:section], target, comparisons)

def tests(lyst, target):
    print(f"The list is {lyst}, the target is {target}")
    
    linear = linear_search(lyst, target)
    binary = binary_search(lyst, target)
    jump = jump_search(lyst, target)

    print(f"Linear Search: Target found- {linear[0]} --- Comparisons made- {linear[1]}")
    print(f"Binary Search: Target found- {binary[0]} --- Comparisons made- {binary[1]}")
    print(f"Jump Search: Target found- {jump[0]} --- Comparisons made- {jump[1]}")

def main():
    data = [1,2,2,5,6,8,9,13,14,17,18,19]
    tests(data, 5)
    tests(data, 19)
    tests(data, 20)

if __name__ == "__main__":
    main()