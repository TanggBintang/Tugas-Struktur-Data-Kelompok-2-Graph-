class Graph:
    def __init__(self):
        self.adjList = {}
    
    def printGraph(self):
        for vertex in self.adjList:
            print(vertex, ":", self.adjList[vertex])
    
    def masukanVertex(self,vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []
            return True
        return False
    
    def masukanEdge(self,kota1,kota2):
        if kota1 in self.adjList and kota2 in self.adjList:
            self.adjList[kota1].append(kota2)
            self.adjList[kota2].append(kota1)
            return True
        return False

singaporegraph = Graph() 
singaporegraph.masukanVertex("SINGAPURA")
singaporegraph.masukanVertex("ANG MO KIO")
singaporegraph.masukanVertex("SENGKANG")
singaporegraph.masukanVertex("PAYA LEBAR")
singaporegraph.masukanVertex("BUKIT TIMAH")
singaporegraph.masukanVertex("NOVENA")
singaporegraph.masukanVertex("TAMPINES")
singaporegraph.masukanVertex("JURONG EAST")
singaporegraph.masukanVertex("TENGAH")
singaporegraph.masukanVertex("CHOA CHU KANG")
singaporegraph.masukanVertex("MANDAI")
singaporegraph.masukanVertex("KRANJI")
singaporegraph.masukanVertex("SEMBAWANG")
singaporegraph.masukanEdge("SINGAPURA","JURONG EAST")
singaporegraph.masukanEdge("SINGAPURA","BUKIT TIMAH")
singaporegraph.masukanEdge("SINGAPURA","PAYA LEBAR")
singaporegraph.masukanEdge("SINGAPURA","NOVENA")
singaporegraph.masukanEdge("SINGAPURA","TAMPINES")
singaporegraph.masukanEdge("JURONG EAST","TENGAH")
singaporegraph.masukanEdge("JURONG EAST","CHOA CHU KANG")
singaporegraph.masukanEdge("JURONG EAST","BUKIT TIMAH")
singaporegraph.masukanEdge("JURONG EAST","SINGAPURA")
singaporegraph.masukanEdge("BUKIT TIMAH","SINGAPURA")
singaporegraph.masukanEdge("BUKIT TIMAH","JURONG EAST")
singaporegraph.masukanEdge("BUKIT TIMAH","CHOA CHU KANG")
singaporegraph.masukanEdge("BUKIT TIMAH","ANG MO KIO")
singaporegraph.masukanEdge("BUKIT TIMAH","MANDAI")
singaporegraph.masukanEdge("BUKIT TIMAH","NOVENA")
