"""
Crie uma função ispalindrome(s) que devolva um valor booleano indicando se a string s é um palíndromo ou não.
"""

def isPalindrome(str):
    nor_list = [c for c in str]
    rev_list = nor_list[::-1]
    return rev_list == nor_list

print(isPalindrome("Teste"))
print(isPalindrome("ABBCBBA"))