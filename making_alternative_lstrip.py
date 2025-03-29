#Input a sentence from user

sentence = str(input("Enter a sentence: "))
result = ""

#Create a function that works similarly as lstrip() without using the actual function

for char in sentence:
    if result or not char.isspace():
        result += char

print(result)