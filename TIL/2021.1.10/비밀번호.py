url ="http://naver.com"

my_str = url.replace("http://","") #규칙

#print(my_str)

my_str = my_str[:my_str.index(" . ")]

print(my_str)

password = my_str[:3]+str(len(my_str)) + str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호 {1} 입니다ㅏ".format(password))

