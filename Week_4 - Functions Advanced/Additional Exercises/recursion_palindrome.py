def palindrome(string, index, index_o = -1):
    if len(string) // 2 == index:
        return f'{string} is a palindrome'

    if string[index] != string[index_o]:
        return f'{string} is not a palindrome'

    return palindrome(string, index+1, index_o-1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))