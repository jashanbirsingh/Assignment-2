s1 = int(input("Enter Length one: "))
s2 = int(input("Enter Length two: "))
s3 = int(input("Enter Length three: "))

if(s1+s2 > s3):
    test1 = True
else:
    test1 = False

if(s2+s3 > s1):
    test2 = True
else:
    test2 = False

if(s3+s1 > s2):
    test3 = True
else:
    test3 = False

if(test1 and test2 and test3):
    print("Yes")
else:
    print("No")


#if (a+b)>c and (b+C)>a and (c+a)>b: )
#    print(yes)
#else:
#   print("no")
