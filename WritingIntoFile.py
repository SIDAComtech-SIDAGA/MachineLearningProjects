words = ["Amazing", "Green", "Python", "Code"]

with open("Script.sh", "w") as file:
     for word in words:
         file.write(word + "\n")
         print(file)