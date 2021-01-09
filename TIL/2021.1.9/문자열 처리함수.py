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


print(python.find("n"))
#n이 들어가있는 위치를 알려준다.