# Prompts user for height of triangle be created and then prints "hello world!" (normal sequence + reversed)

height = int(input("Enter a height for your triangle: "))
str = "hello world!"
i = 0
space_amt = 0
tab = 0
tab = height
print(" " * (tab + 1),"/\\")
while i is not (height - 1):
    print(" " * tab, "/", " " * space_amt, "\\")
    i += 1
    space_amt += 2
    tab -= 1
print(" " * tab, "/_", "_ " * ((space_amt - 1)//2), "_\\\n")
print(" " * (height//2), str[::-1])
print(" " * (height//2), str)



