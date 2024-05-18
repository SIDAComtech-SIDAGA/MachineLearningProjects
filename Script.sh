# # def add(z,y):
# #     return x+y
# # def substract(x,y):
# #     return x - y
# # def multply(x,y):
# #     return x * y
# # def divide(z,y):
# #     if y !=0:
# #         return x / y
# #     else:
# #         return "Error! division by zero"
# # def main():
# #     echo ("Select an operation")
# #     echo ("1. Add")
# #     echo ("2. Substract")
# #     echo ("3. Multply")
# #     echo ("4. Divide")

# #     while True:
# #         choice = input("Enter choice(1/2/3/4)")

# #         if choice in ['1','2','3','4']:
# #             try:
# #                 num1 = float(input("Enter the first number"))
# #                 num2 = float(input("Enter the second number"))

# #             except ValueErro:
# #                 echo "Invalid input. Please enter a number"

# #                 continue

# #             if choice == '1':
# #                 echo "Result :", $num1 + $num2
# #             break
# #         else:
# #             echo "invalid input"
# # if __name__ == "__main__":
# #     main()


# sum=$((20+2))
# echo "sum = ${sum}"

# sub=$((20-2))
# echo "Sub=${SUB}"

# mul=$((20*2))
# echo "mul=${mul}"

#!bin/bash
a=5
b=6
echo "$((a+b))"
echo "$((a-b))"
echo "$((a*b))"
echo "$((a/b))"
echo "$((a%b))"
echo "$((2**3))"
((a++))
echo $a
((a+=3))
echo $a