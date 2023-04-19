
#숫자로써 의미가 x
#갯수 세는 용도니깐
#—> 그래서 문자열로 치환

#[] 자체를 문자로 인식

# debugging
print(str([4, 1, 2]))
print(str([4, 1, 2].count(4)))


# programmers 7의 개수
def solution(arr):
    string_arr = str(arr)
    return string_arr.count('7')
