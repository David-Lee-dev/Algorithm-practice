def solution(nums):
    nums_set = set(nums) # 폰캣몬의 종류
    
    if int(len(nums)/2) >= len(nums_set):
        answer = len(nums_set)
    else:
        answer = len(nums)/2
        
    
    return answer