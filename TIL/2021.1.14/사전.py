#형식은 KEY:value 형태이다. 

cabinet ={3:"유재석",100:"김태호"}
print(cabinet[3])
#3번키에 있는 유재석이라는 값을 가지고 와준다.

print(cabinet[100])
#100번키에 있는 김태호라는 키 값을 가지고 와준다.

print(cabinet.get(3))
#얘도 김태호라는 값을 가지고 온다.

print(cabinet[5])
#이러면 오류가 발생한다. 5라는 키에 해당하는 값이 없기 때문이다.


print(cabinet.get(5,"사용가능"))
#이렇게 키를 선언해주게 된다면 사용이 가능하다

print(3 in cabinet) #true



