python = "Python is amazing"
print(python.lower())
#모든 문자열이 소문자로 변하게 된다.
print(python.upper())
#모든 문자열이 대문자로 변하게 된다.
print(python[0],isupper())
#True가 나오게 된다.

print(len(python))
#전체 문자열의 길이를 알려준다.

print(python.replace("python","Java"))

index = python.index("n")
print(index)
index = python.index("n",index+1)
print(index)


print(python.find("Java"))
#java가 저기에 있는지 확인해준다.
#안나오므로 -1이 나오게 된다.

print("hi")

print(python.count("n"))
#n이 몇번이 들어가는지 count해준다.