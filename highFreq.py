def high_freq_ele(l):
    n = len(l)
    val = n // 3

    result = []
    for num in set(l):
        if l.count(num) > val:
            result.append(num)
    return result
l = [3,3,3,2,1,1]
result = high_freq_ele(l)
print(result)

''' Steps:
1. An consisting of integer values is given as input and it is passed to high_freq_ele function.
2. length of the array is stored in variable n.
3. Then we consider an empty array 'result', which is used to append the values that appear more than n/3 times.
4. For each element in the array, check if the element appears more than n/3 times. 
   If the count is greater than the value n/3, then append that element to the array 'result'.
5. Return the array 'result'.'''
