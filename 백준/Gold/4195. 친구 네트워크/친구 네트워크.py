import sys
input = sys.stdin.readline


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a == b:
        return network[a]
    
    # 합쳐야하는 경우면 a를 부모노드로 설정하는 방식
    parent[b] = a
    network[a] += network[b]
    return network[a]
    
testcase = int(input())

for i in range(testcase):
    # 각 케이스별로 부모용, 네트워크용?
    parent = dict()
    network = dict()
    relation = int(input())

    for j in range(relation):
        a, b = map(str, input().split())
        if parent.get(a) == None:  # 그 값 없으면
            parent[a] = a  # 본인 스스로를 부모 노드로 설정
            network[a] = 1 # 본인 스스로만 포함이니 1
        if parent.get(b) == None:
            parent[b] = b
            network[b] = 1
            
        # 매 relation 주어질때마다 실행해서 출력
        print(union_parent(a,b))