#Python 포매팅 지시어
# %s : 문자열
# %c : 문자 1개
# %d : 정수
# %f : 실수
# %o : 8진수
# %x : 16진수
# %% : Literal(문자 '%' 자체)

#Python 이스케이프 문자
# \b : 백스페이스
# \t : 탭
# \n : 줄바꿈
# \f : 다음 페이지 출력
# \r : 시작 라인으로 바꿈
# \\ : 역슬래시
# \' : 작은 따옴표
# \" : 큰 따옴표


# test1 = "Life is short, %s"
# result1 = test1 % "You need python."
# print(result1)
# case2 = "Life is short, %s %s %s"
# case2result = case2 % ("You", "need", "python")
# print(case2result)

# test2 = "Life is short, %d"
# result2 = test2 % "10" #TypeError: %d format: a number is required, not str
# print(result2)

# test3 = "Life is short, %.2f"
# result3 = test3 % 100
# print(result3)

# test4 = "Life is short, {} {} {}"
# result4 = test4.format("You", "need", 10)
# print(result4)

test5 = "Life is short,\n\'You need python.\'"
print(test5)