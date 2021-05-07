## input -  한 번에 여러 개의 값 입력받기



#### 지금까지는 input 한 번에 값 하나만 입력을 받았다. 그럼 input 한 번에 값을 여러 개 입력 받으려면 어떻게 해야 할까? 이때는 input에서 spilt을 사용한 여러 개에 저장해주면 된다.(각 변수는 콤마로 구분해 준다)

```py
변수1,변수2 = input().split()
변수1,변수2 = input().split('기준문자열')
변수1,변수2 = input('문자열').split()
변수1,변수2 = input('문자열').split('기준 문자열')

a,b = input('문자열 두 개를 입력하세요 : ').split() #입력받은 값을 공백을 기준으로 분리

print(a)
print(b)

---------------------------
실행결과

문자열 두 개를 입력하세요 : Hello Python(입력)
Hello
Python
```

```py
>> a,b = input('숫자 두 개를 입력허세요  : ').split()
숫자 두 개를 입력허세요  : 10 20
>>> a = int(a)
>>> b = int(b)
>>> c = a+b
>>> a,b = input('숫자 두 개를 입력허세요  : ').split()
숫자 두 개를 입력허세요  : 10 20
>>> print(c)
30
```



#### map을 사용하면 split의 결과를 한 번에 int 로 변활해 줄 수 있다.

```python
변수1,변수2 = map(int ,input().split())

변수1,변수2 = map(int ,input().split('기준문자열'))

변수1,변수2 = map(int ,input('문자열').split())

변수1,변수2 = map(int ,input('문자열').split()'기준문자열))

```



더하기 문제

```pyth
a,b = map(int,input('숫자 두 개를 입력하세요 : ').split())
숫자 두 개를 입력하세요 : 10 20
>>> print(a+b)
---------------
실행결과 
30
```

