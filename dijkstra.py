import math, time

class Graph():
    graph = []
    
    # x is for vertices processed so far
    X = []

    # shortest path calculated
    A = []

    def __init__(self, vertices):
        self.getGraph()
        self.vertices = vertices
        self.X = [False] * vertices
        self.A = [1000000]* vertices
        self.A[0] = 0
        self.X[0] = True
    

    def getGraph(self):
        text = open(r"E:\Summer 2019\Algorithms\Dikstra's Algorithm\dijkstraData.txt")

        content = text.read().splitlines()
        edge = []

        for line in content:
            test = line.split('\t')
            for couple in test:
                temp = couple.split(',')
                if len(temp) == 2:
                    edge.append(tuple( ( int(temp[0]), int(temp[1]) ) ) )

            self.graph.append(edge)
            edge = []


    def dijkstra(self):
        
        while True:
            old = math.inf

            for i in range(len(self.X)):
                if self.X[i]:
                    for edge in self.graph[i]:
                        if self.X[edge[0] - 1] == False:
                            new = self.A[i] + edge[1]

                            if old > new:
                                old = new
                                # u = i
                                v = edge[0] - 1
            
            self.A[v] = old
            self.X[v] = True
            if not False in self.X:
                break

        #  print(self.A, len(self.A))

    def getShortestPath(self, i):
        print(f"For vertex {i}: {self.A[i - 1]}")

# driver code 

vertices = 200 

g = Graph(vertices)
g.dijkstra()

g.getShortestPath(7)
g.getShortestPath(37)
g.getShortestPath(59)
g.getShortestPath(82)
g.getShortestPath(99)

g.getShortestPath(115)
g.getShortestPath(133)
g.getShortestPath(165)
g.getShortestPath(188)
g.getShortestPath(197)