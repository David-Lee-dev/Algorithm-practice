def solution(n, lost, reserve):
    answer = 0
    lost_c = set(lost) - set(reserve)
    reserve_c = set(reserve) - set(lost)
    
    for i in sorted(list(reserve_c)):
        if i-1 in lost_c:
            lost_c -= set([i-1])
        elif i+1 in lost_c:
            lost_c -= set([i+1])
            
    answer = n - len(lost_c)
    return answer