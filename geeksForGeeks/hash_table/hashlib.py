import hashlib

data = 'test'.encode()
hash_object = hashlib.sha256()
hash_object.update(data)
hex_dig = hash_object.hexdigest()
print(hex_dig)

data2 = 'hello world'.encode()
hash_object2 = hashlib.sha256()
hash_object2.update(data2)
hex_dig2 = hash_object2.hexdigest()
print(hex_dig2)


dic = {'name': 'Lee', 'phone': '01042504296', 'birth': '901009'}


# 딕셔너리 생성
a = {1: 'a'}

# key(2), value(b) 쌍 추가
a[2] = 'b'
print(a)

# key(3), value([1, 2, 3]) 추가
a[3] = [1, 2, 3]
print(a)

# key 2인 요소 삭제
del a[2]
print(a)

# key 1인 요소 접근
a[1]

# key list 만들기
a.keys()

# key :value 쌍으로 얻기
a.items()

# key로 value 얻기
a.get(1)

# key: value 쌍 모두 지우기
a.clear()
print(a)

# 중복 주의
a = {1: 'a', 1: 'b'}
print(a)

# key값이 중복되면 가장 뒤쪽의 key, value 쌍을 출력한다.
# key값은 list로 쓸 수 없으며, key값으로 쓸 수 있는 값은 변하지 않는 값에 해당한다.

