#len(12345) # TypeError len() takes String,bytes,tuples and collections as argument

#len("12345") # No TypeError

#Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

#Type Conversion
print(int("123") + int("456"))

print("Number of letters in your name: "+ str(len(input("Enter your name"))))