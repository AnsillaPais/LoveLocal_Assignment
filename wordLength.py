def last_word_lenth(a):
    words = a.split()
    
    if not words:
        return 0
    return len(words[-1])

a = " Hello SJEC "
res = last_word_lenth(a)
print(res)

'''Steps:
1. A sentence is given as input.
2. split the input using split function. Then the resultant output will be words=['Hello','SJEC']
3. Then it will check for the words in array.
4. If the number of words is zero, then the length also will be zero.
5. Or else it will return the length of last word using len(words[-1]). Here -1 indicates the last index value.
'''