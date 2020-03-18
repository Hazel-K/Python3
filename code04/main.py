# x = 10
# y = 10.1
# z = "문자열"
# isBool = Ture # False
# isNone = None

num_list = [1, 2, 3, 4, 5]
#인덱싱은 0부터 시작

# print(num_list[0], num_list[-1])
    
# for i in num_list:
#     print(i)
# 슬라이싱 (범위) 시작:끝-1

# print(num_list[0:3])
# print(num_list[1:])

num_list.append(6)
num_list.append(7)
# len(num_list)
del num_list[len(num_list) - 1] # 삭제
num_list[0] = 0 # 수정
print(num_list)


num_dict = {"k":"Kim", "h":"Hyo"}
print(num_dict["k"])

for k, v in num_dict.items():
    print(k, v)
# keys(), values()

num_dict["j"] = "Jin" # 키의 존재 유무 > 추가, 수정
print(num_dict)

del num_dict["k"] # 삭제
print(num_dict.get("k")) # 키에러 안나게 하는 메서드