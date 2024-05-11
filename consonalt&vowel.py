random_string = input("Enter the string \t")
print("You provided string", random_string)
result =""

# exctract the words 
for char in random_string:
    if char.isalpha():
        result += char
    

print("Extracted stieng is ", result)

# initialiazing two void intergers 
vowel_count = 0
consonant_count = 0

#Storing vowels both in upper and lowers in a string variable
vowels = 'AaEeIiOoUu'

for display_string in result:
    if display_string in vowels:
        vowel_count += 1
    else:
        consonant_count +=1

print('Number of Vowels: ', vowel_count)
print('Number of consonalt: ', consonant_count)
        
