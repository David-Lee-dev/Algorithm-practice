T = int(input())
grade = [
    'A+', 'A0', 'A-', 
    'B+', 'B0', 'B-', 
    'C+', 'C0', 'C-', 
    'D0'
]
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    grade_index = 0
    total_score = []
    score = 0
    for i in range(N):
        student = (input().split())
        score += (int(student[0])*0.35) + (int(student[1])*0.45) + (int(student[2])*0.2)
        total_score.append(score)
        score = 0
        
    sort_score = sorted(total_score, reverse=True)
    
    for i in range(N):
        if(sort_score[i] == total_score[K-1]):
            grade_index = i // (N//10)
            
    print('#{} {}'.format(test_case, grade[grade_index]))