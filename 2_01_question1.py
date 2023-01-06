b=str("Python is a case sensitive language")
#find the length of the string
print(len(b))


# #find the length of the string
# count=0
# for i in b:
#     count=count+1
# print(count)


#reverse the order of the string in one line code
rev = b[::-1]
print(rev)


#use a slice function store "a case sensitive" in new string
slice = b[10:26]
print(slice)
    

#replace "a case sensitive" with "object oriented"
a1=b.replace('a case sensitive','object oriented')
print(a1)

#find index of substring "a" in the given input string
print(b.find("a"))


# remove the white spaces from the given input string
nowhites = b.replace(" ", "")
print(nowhites)