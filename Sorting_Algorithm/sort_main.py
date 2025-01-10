import random

def gen_list(length_of_list):
    random_list=[]
    for i in range(length_of_list):                                # Generate a list of 100 random integers between 1 and 100
        random_list.append(random.randint(1, 10))
    return random_list



def bubbleSort(random_list):
    n = len(random_list)
    for i in range(n-1):
        for j in range(n-i-2):
            if random_list[j] > random_list[j+1]:
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j] #swap the elements
    return random_list





def selectionsort(random_list):
    n = len(random_list)
    for i in range(n):
        smallest_num = i # Assume the first element of the unsorted portion is the smallest
        for j in range(i + 1, n):   # Find the actual smallest element in the unsorted portion
            if random_list[j] < random_list[smallest_num]:
                smallest_num = j 
        random_list[i], random_list[smallest_num] = random_list[smallest_num], random_list[i]
        # Swap the found minimum element with the first element of the unsorted portion
    return random_list





def insertionsort(random_list):
    n = len(random_list)
    for i in range(1,n):
       key = random_list[i]
       j = i - 1

       while j >= 0 and random_list[j] >key:
            random_list[j + 1] = random_list[j]
            j -= 1
       random_list[j + 1] =key
    return random_list





def mergesort(random_list):
    # Base case: A list with 0 or 1 element is already sorted
    if len(random_list) <= 1:
        return random_list
    # Step 1: Divide the list into two halves
    mid = len(random_list) // 2
    left_half = mergesort(random_list[:mid])
    right_half = mergesort(random_list[mid:])

    # Step 2: Merge the two sorted halves
    return merge(left_half, right_half)
def merge(left, right):
    merged = []
    i = j = 0

    # Step 3: Compare elements and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Step 4: Add any remaining elements from the left or right half
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged





def quicksort(random_list):
    # Base case: A list with 0 or 1 element is already sorted
    if len(random_list) <= 1:
        return random_list

    # Step 1: Choose a pivot (here, the last element)
    pivot = random_list[-1]

    # Step 2: Partition the list into two sublists
    left = [x for x in random_list[:-1] if x <= pivot]  # Elements smaller or equal to the pivot
    right = [x for x in random_list[:-1] if x > pivot]  # Elements larger than the pivot

    # Step 3: Recursively apply Quick Sort to sublists and combine
    return quicksort(left) + [pivot] + quicksort(right)





def heapify(random_list, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # If left child is larger than root
    if left < n and random_list[left] > random_list[largest]:
        largest = left

    # If right child is larger than largest so far
    if right < n and random_list[right] > random_list[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        random_list[i], random_list[largest] = random_list[largest], random_list[i]  # Swap
        # Recursively heapify the affected subtree
        heapify(random_list, n, largest)
def heapsort(random_list):
    n = len(random_list)

    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(random_list, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        random_list[0], random_list[i] = random_list[i], random_list[0]
        # Call heapify on the reduced heap
        heapify(random_list, i, 0)
        return random_list





def counting_sort(random_list, exp):
    n = len(random_list)
    output = [0] * n  # Output random_listay
    count = [0] * 10  # Count random_listay for digits (0-9)

    # Step 1: Count occurrences of each digit
    for num in random_list:
        index = (num // exp) % 10
        count[index] += 1

    # Step 2: Update count random_listay to store positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Step 3: Build the output random_listay
    for i in range(n - 1, -1, -1):
        index = (random_list[i] // exp) % 10
        output[count[index] - 1] = random_list[i]
        count[index] -= 1

    # Step 4: Copy the output random_listay back to the original random_listay
    for i in range(n):
        random_list[i] = output[i]

def radixsort(random_list):
    # Step 1: Find the maximum number to determine the number of digits
    max_num = max(random_list)
    exp = 1  # Initialize the digit position (1, 10, 100, ...)

    # Step 2: Sort based on each digit
    while max_num // exp > 0:
        counting_sort(random_list, exp)
        exp *= 10
    return random_list




def countingsort(random_list):
    # Step 1: Find the maximum and minimum values
    max_val = max(random_list)
    min_val = min(random_list)
    range_of_elements = max_val - min_val + 1

    # Step 2: Initialize the count array
    count = [0] * range_of_elements

    # Step 3: Store the count of each element
    for num in random_list:
        count[num - min_val] += 1

    # Step 4: Update the count array to store cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build the output array
    output = [0] * len(random_list)
    for i in range(len(random_list) - 1, -1, -1):  # Traverse the input array from right to left
        num = random_list[i]
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    # Step 6: Copy the sorted elements back into the original array
    for i in range(len(random_list)):
        random_list[i] = output[i]
    return random_list










#test the algorithm here>>>>>>
unsorted_list=gen_list(10)
print(unsorted_list)
sorted_list=countingsort(unsorted_list)
print(sorted_list)