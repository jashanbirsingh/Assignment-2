a = int(input("Input the first number: "))
b= int(input("Input the second number: "))
c = int(input("Input the third number: "))
given = [a, b, c]
#print(max(given))

given.sort()

print(f"The largest number out of the inputs is {given[-1]}")
