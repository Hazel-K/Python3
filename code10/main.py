from konlpy.tag import Okt

ok - Okt()
# test = "Hello. Im hazel. #fastcampus #internet lecture"

# for i in ok.pos(test, norm=True)
#     if i[1] == 'Hashtag':
#     print(i)

test = "fastcampus cording programing"
for i in ok.nouns(test):
    print(i)