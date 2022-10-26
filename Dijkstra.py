import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[-1 for column in range(vertices)]
                      for row in range(vertices)]
                      

    def dijkstra(self, src):
        vertex = list(map(lambda i: i, range(self.V)))
        dist = [sys.maxsize] * self.V
        pred = dict()
        dist[src] = 0
        pred[src] = src
        s = list()
        for i in range(self.V):
            global min_index
            min = sys.maxsize
            for v in vertex:
                if dist[v] < min:
                    min = dist[v]
                    min_index = v
            s.append(min_index)
            vertex.remove(min_index)
            for v in vertex:
                if self.graph[min_index][v] >= 0 and (v not in s) and dist[v] > dist[min_index] + self.graph[min_index][v]:
                    dist[v] = dist[min_index] + self.graph[min_index][v]
                    pred[v] = min_index
            print(f"{'-' * 20} step {len(s)} {'-' * 20}")
            for node in range(self.V):
                print(f"{node} Distance from {start} : {'infinity' if dist[node] == sys.maxsize else dist[node]}")
            print(f"this is S list :{s}")
            print(f"this is S' list :{vertex}")
            for ver in pred:
                print(f"{ver} pred is {pred[ver]}")
        print(f"{'-' * 20} shortest path {'-' * 20}")
        path = s[n - 1]
        output = str(path)
        while (path != pred[path]):
            path = pred[path]
            output = str(path) + " _ " + output
        print(output)
        print(f"Weight of the shortest path : {dist[s[n - 1]]}")


print("Enter the number of vertices : ")
n = int(input())
g = Graph(n)
print("Enter the number of edges : ")
e = int(input())
print(f"Notic: The name of vertices is 0 to {n - 1}")
print("Enter edges like this format : first vertex-second vertex-weight edge\nsample : 0-4-17 ")
for i in range(e):
    edge = input().split("-")
    g.graph[int(edge[0])][int(edge[1])] = int(edge[2])
    g.graph[int(edge[1])][int(edge[0])] = int(edge[2])
print("Enter start vertex : ")
start = int(input())

g.dijkstra(start)


"""
4
4
0-1-3
0-2-4
1-3-4
2-3-2
----------
8
11
0-1-1
0-4-2
0-2-3
1-3-5
1-6-4
2-3-6
2-5-1
3-7-3
4-5-7
5-7-4
6-7-2

"""