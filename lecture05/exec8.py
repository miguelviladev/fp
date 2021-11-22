def isPalindrome(str):
    nor_list = [c for c in str]
    rev_list = nor_list[::-1]
    return rev_list == nor_list

print(isPalindrome("Teste"))
print(isPalindrome("ABBCBBA"))