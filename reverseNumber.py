def rev_num(num):
    rev = 0
    while num > 0:
        reminder = num % 10
        rev = (rev * 10) + reminder
        num = num // 10
    return rev
print("reverse of a given number is {rev_num(1234)}")