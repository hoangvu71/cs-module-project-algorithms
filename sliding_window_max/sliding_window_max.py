'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    first = 0
    last = len(nums) - 1
    array = []
    def findMaxWindow(arr):
        return max(arr)
    while first <= last - (k -1):
        new_arr = nums[first: first + k]
        array.append(findMaxWindow(new_arr))
        first += 1
    return array

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
