str1=input("Enter the string 1: ")
str2=input("Enter the string 2: ")

print("the original string 1 is: ",str1)
print("the original string 2 is: ",str2)


#string concanting
print("Concating: ",str1 +" "+ str2)

#string slicing
print("Slicing1: ",str1[0:4])
print("Slicing2: ",str2[0:4])

print("reverse1: ",str1[::-1])
print("reverse2: ",str2[::-1])

#string basic_case
print("Upper1: ",str1.upper())
print("Lower1: ",str1.lower())

print("Upper2: ",str2.upper())
print("Lower2: ",str2.lower())

#string capitalize
print("Capitalize1: ",str1.capitalize())
print("Capitalize2: ",str2.capitalize())

#string find
print("Find1: ",str1.find("m"))
print("Find2: ",str2.find("j"))

#string split
print("Split1: ",str1.split())
print("Split2: ",str2.split())

#string count
print("Count1: ",str1.count("e"))
print("Count2: ",str2.count("i"))

#string replace
print("replace1: ",str1.replace("shreehari","Adv" ))
print("replace2: ",str2.replace("joshi","vyanki"))

#string length
print("string length 1",len(str1))
print("string length 2",len(str2))

#string Formating
print(f"The name of student is {str1} & surname of student is {str2}")

