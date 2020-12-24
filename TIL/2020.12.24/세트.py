#집합 (set)
# 중복 안됨,순서 없음

my_set ={1,2,3,3,3}

print(my_set)
#이러면 출력은 1,2,3 만 나온다 이유는 중복된것은 출력 안된다

java = {"유재석", "김태호","양세찬"}
python = set(["유재석","김태호"])

#교칩합 java 와 python 개발자 모두


#경우1
print(java & python)

#이러면 출력은 유재석 김태호 뿐

#경우2
print(java.intersection(python))

#이 경우에도 출력은 유재석과 김태호 뿐

#합집합 : java나 pyhon을 할 수 있는 사람

print(java & python)
print(java.union(python))

#이러면 김태호 유재석 양세형이 출력

#차집합 : java는 할 수 있지만 python은 할 줄 모르는 사람
print(java - python)
print(different(python))


#python 인원 추가
python.add("김종국")
print(python)




