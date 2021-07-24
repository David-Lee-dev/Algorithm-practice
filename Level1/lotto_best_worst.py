def solution(lottos, win_nums):
    answer = []
    
    rank = [6, 6, 5, 4, 3, 2, 1]
    count = 0
    zero_count = 0
    
    for num in lottos:
        if num in win_nums:
            count += 1
        elif not num:
            zero_count  += 1
            
    answer += [rank[count + zero_count], rank[count]]
    
    return answer
