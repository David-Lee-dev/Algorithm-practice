T = int(input())
for test_case in range(1, T + 1):
    '''
    K = 3          # 최대 이동 거리
    N = 10         # 도달해야 하는 거리
    M = 5          # 충전소 갯수
    '''
    K, N, M = map(int, input().split())

    # 목표 위치까지 정류장 정보 charge에 저장
    charge_location = list(map(int, input().split()))
    charge = [0]*(N+1)
    for idx in range(M):
        charge[charge_location[idx]] = 1

    now_station = 0
    count = 0

    while now_station < N:
        # 최대 거리 이동
        now_station += K

        # 거리 도달 시 종료
        if now_station >= N:
            break
        # 최대 거리 이동 후 정류장이 없을 때
        tmp = 0
        for idx in range(K):
            if charge[now_station]:
                break
            now_station -= 1
            tmp += 1

        # 정류장 없어서 다시 돌아오면
        if tmp == K:
            count = 0
            break

        # 충전
        count += 1

    print("#{} {}".format(test_case, count))
