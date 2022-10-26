import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[-1 for column in range(vertices)]
                      for row in range(vertices)]
        

    def dijkstra(self, src):
        vertex_name = ['a', 'b', 'c', 'd', 'e', 'f', 'l', 'k']
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
                print(f"{vertex_name[node]} Distance from {vertex_name[start]} : {'infinity' if dist[node] == sys.maxsize else dist[node]}")
            print(f"this is S list :{list(map(lambda x: vertex_name[x], s))}")
            print(f"this is S list :{list(map(lambda x: vertex_name[x], vertex))}")
            # print(f"this is S list :{s}")
            # print(f"this is S' list :{vertex}")
            for ver in pred:
                print(f"{vertex_name[ver]} pred is {vertex_name[pred[ver]]}")
                # print(f"{ver} pred is {pred[ver]}")
        print(f"{'-' * 20} shortest path {'-' * 20}")
        path = s[n - 1]
        # output = str(path)
        # while (path != pred[path]):
        #     path = pred[path]
        #     output = str(path) + " _ " + output
        output = str(vertex_name[path])
        while (path != pred[path]):
            path = pred[path]
            output = str(vertex_name[path]) + " _ " + output
        print(output)
        print(f"Weight of the shortest path : {dist[s[n - 1]]}")


print("Enter the number of vertices : ")
n = int(input())
g = Graph(n)
print("Enter the number of edges : ")
e = int(input())
print(f"Notic: The name of vertices is 0 to {n - 1}")
vertex_name = ['a', 'b', 'c', 'd', 'e', 'f', 'l', 'k']
print("Enter edges like this format : first vertex-second vertex-weight edge\nsample : a-b-17 ")
for i in range(e):
    edge = input().split("-")
    g.graph[vertex_name.index(edge[0])][vertex_name.index(edge[1])] = int(edge[2])
    g.graph[vertex_name.index(edge[1])][vertex_name.index(edge[0])] = int(edge[2])
print("Enter start vertex : ")
start = vertex_name.index(input())

g.dijkstra(start)


"""
8
11
a-b-1
a-e-2
a-c-3
b-d-5
b-l-4
c-d-6
c-f-1
d-k-3
e-f-7
f-k-4
l-k-2

"""