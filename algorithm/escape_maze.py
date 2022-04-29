from collections import deque  # 덱 사용을 위해


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 첫 값을 그대로 집어 넣는다.
    while queue:
        x, y = queue.popleft()  # 해당 값을 밖으로 끄집어 낸다.
        for i in range(4):
            nx = x + dx[i]  # 다음 상하좌우를 탐색하기
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue  # 위치가 범위에서 벗어나는 경우 무시
            if graph[nx][ny] == 0:
                continue  # 괴물이 나오는 경우(벽인 경우) 무시
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                # 갈 수 있는 경우 해당 노드 도착하여 기존의 이동거리 누적, 큐 안에 집어 넣는다.
    print(graph[0])
    print(graph[1])
    print(graph[2])
    print(graph[3])
    print(graph[4])
    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
