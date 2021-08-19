# 노드 만드는 클래스
class Node():
    def __init__(self, name, next):
        self.name = name
        self.next = next

    def find_node(self, nodes, src, dst):
        result = 0
        # 진행 가능한 경로만큼 반복 없으면 0
        for i in range(len(nodes[src].next)):
            # 다음 경로가 목적지면 1
            if nodes[src].next[i] == dst:
                return 1
            else:
                # 다음 경로가 목적지가 아니면 재귀
                result += self.find_node(nodes, nodes[src].next[i], dst)
        return result


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    nodes = [0]  # 노드
    routes = [[] for _ in range(V+1)]  # 경로
    for i in range(E):  # 노드 별 경로 저장
        n, d = map(int, input().split())
        routes[n] += [d]
    S, G = map(int, input().split())

    for i in range(1, len(routes)):  # 번호 별로 노드 저장
        if routes[i]:
            nodes += [Node(i, routes[i])]
        else:
            nodes += [Node(i, [])]

    print("#{} {}".format(tc, nodes[S].find_node(nodes, S, G)))
