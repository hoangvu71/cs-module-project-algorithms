'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n, cache = [0 for i in range(11)]):
    # Your code here
    if n <= 1:
        cache[1] = 1
        return 1
    elif n == 2:
        cache[2] = 2
        return 2

    if cache[n]:
        return cache[n]
    
    way_3 = eating_cookies(n - 3, cache)
    way_2 = eating_cookies(n - 2, cache)
    way_1 = eating_cookies(n - 1, cache)

    result = way_3 + way_2 + way_1
    cache[n] = result
    return result

import time

start = time.time()
print(f'{eating_cookies(50, [0 for i in range(51)])}')
print(f'\nResult calculated in {time.time()-start:.5f} seconds')
print('\n--------------------------------\n')

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
