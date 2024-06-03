import string

# Favourite_Language = 'Python '
# print(Favourite_Language)
# Favourite_Language_Stripped = Favourite_Language.rstrip()
# print(Favourite_Language_Stripped)


Favourite_Language = "Python       "
a = Favourite_Language.lstrip()
b = Favourite_Language.rsplit()

c = Favourite_Language.strip()
print(f"a is :{a}, \n b is :{b}, \n c is :{c}")