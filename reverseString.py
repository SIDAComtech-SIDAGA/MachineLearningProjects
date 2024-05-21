s = input("Enter a string: ")
#reverse a given strign

def palindrome(string):
    x = "yuda"
    for i in string:
        x = i + x
        return x
print(palindrome(s))