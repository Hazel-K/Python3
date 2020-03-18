# num_tuple = (1, 2, 3)
# num_tuple[0] = 0
#TypeError: 'tuple' object does not support item assignment
# del num_tuple[0]
#TypeError: 'tuple' object does not support item assignment
# print(num_tuple)
# 튜플 형태의 값은 수정 삭제가 불가능

# num_set = {1, 1, 2, 2, 3, 3} # {1,2,3} 중복 제거됨
# num_set.add(4)
# print(num_set)
# 순서를 갖지 않으므로 인덱싱, 슬라이싱 불가능

# set1 = {1, 2, 3, 4}
# set2 = {1, 2, 3}
# print(set1 & set2) #교집합 연산
# print(set1 | set2) #합집합 연산
# print(set1 - set2) #처집합 연산

test_list = [1, 2 ,3, 1, 2, 3]
# sub_list = [1, 2 ,3]
# print(test_list + sub_list)
# print(test_list * 2)

# list(), dict(), set(), tuple()
print(set(test_list)) #다른 속성값으로 변경 가능