def solution(array):
    answer = 0
    
    check = {}
    for ar in array:
        if ar not in check:
            check[ar] = 1
        else:
            check[ar] += 1
            
    # sorted_check = sorted(check.items(), reverse=True, key=lambda item: item[1])
    # if len(sorted_check) > 1:
    #     if sorted_check[0][1] != sorted_check[1][1]:
    #         answer = sorted_check[0][0]
    #     else:
    #         answer = -1
    # else:
    #     answer = sorted_check[0][0]
        
    # return answer
    
    m = max(check.values()) # 학생 수가 최대 많은 반 수
    
    s = {}
    for key, value in check.items(): # 각 반의 학생 수?
        if m == value: # 학생 수가 제일 많은 반과 다른 반 학생 수와 비교 했을 때 같을 때
            s.setdefault(key, value) # 같을 때 s 리스트에 추가하여 최대 학생 수가 많은 반의 리스트를 정렬한다?
            print(s)
        else:
            pass
    if len(s) == 1:
        return list(s.keys())[0]
    else:
        return -1
            
    return s #

            
            

print(solution([1,2, 3, 3])) 

#programmers 최빈값 구하기