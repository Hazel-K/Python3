# def sum(x, y, test = 1):
#     return x + y + test

# x = 1
# y = 1
# print(sum(x,y))

# def sum(x,*y):  # *가변인자, 값이 여러 개 들어온다.
#     # sum_list = []
#     result = 0
#     for i in y:
#         # sum_list.append(i)
#         result += i
#     print(x + result)
# sum(1,1,2,3,4,5)

def sum(one, two):
    return one + two

print(sum(one = 1, two = 1))