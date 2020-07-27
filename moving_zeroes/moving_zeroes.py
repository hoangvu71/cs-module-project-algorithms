'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    first = 0
    last = len(arr) - 1
    while first <= last:
        if arr[first] != 0:
            temp = arr[first]
            arr.pop(first)
            arr.insert(0, temp)
        first += 1
    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")