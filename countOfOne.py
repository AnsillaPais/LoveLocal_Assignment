def count_of_dig1(numbers):
    count = 0

    # Count the occurrences of digit "1" in each number
    for num in numbers:
        num_str = str(num)
        count += num_str.count('1')

    return count

n = [1, 13, 2, 4,13]
result = count_of_dig1(n)
print(result)

''' Steps:
1. Array consisting of integer values is given as input. 
2. This array is passed as an arguement to the function count_of_dig1.
3. Initially count=0.
4. Convert each element in the array to string.
5. Then increment the 'count' value if 1 is present in each element, using num_str.count('1')
6. Return 'Count' '''
