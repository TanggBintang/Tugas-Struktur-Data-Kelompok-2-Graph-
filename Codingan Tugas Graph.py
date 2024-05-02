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
singaporegraph.masukanEdge("NOVENA","BUKIT TIMAH")
singaporegraph.masukanEdge("NOVENA","SINGAPURA")
singaporegraph.masukanEdge("NOVENA","ANG MO KIO")
singaporegraph.masukanEdge("NOVENA","SENGKANG")
singaporegraph.masukanEdge("NOVENA","TAMPINES")
singaporegraph.masukanEdge("PAYA LEBAR","SINGAPURA")
singaporegraph.masukanEdge("PAYA LEBAR","ANG MO KIO")
singaporegraph.masukanEdge("PAYA LEBAR","MANDAI")
singaporegraph.masukanEdge("PAYA LEBAR","SENGKANG")
singaporegraph.masukanEdge("PAYA LEBAR","TAMPINES")
singaporegraph.masukanEdge("TAMPINES","SINGAPURA")
singaporegraph.masukanEdge("TAMPINES","NOVENA")
singaporegraph.masukanEdge("TAMPINES","PAYA LEBAR")
singaporegraph.masukanEdge("TAMPINES","SENGKANG")
singaporegraph.masukanEdge("SENGKANG","TAMPINES")
singaporegraph.masukanEdge("SENGKANG","PAYA LEBAR")
singaporegraph.masukanEdge("SENGKANG","NOVENA")
singaporegraph.masukanEdge("SENGKANG","ANG MO KIO")
singaporegraph.masukanEdge("SENGKANG","MANDAI")
singaporegraph.masukanEdge("SENGKANG","SEMBAWANG")
singaporegraph.masukanEdge("TENGAH","JURONG EAST")
singaporegraph.masukanEdge("TENGAH","CHOA CHU KANG")
singaporegraph.masukanEdge("CHOA CHU KANG","TENGAH")
singaporegraph.masukanEdge("CHOA CHU KANG","JURONG EAST")
singaporegraph.masukanEdge("CHOA CHU KANG","BUKIT TIMAH")
singaporegraph.masukanEdge("CHOA CHU KANG","ANG MO KIO")
singaporegraph.masukanEdge("CHOA CHU KANG","MANDAI")
singaporegraph.masukanEdge("CHOA CHU KANG","KRANJI")
singaporegraph.masukanEdge("ANG MO KIO","NOVENA")
singaporegraph.masukanEdge("ANG MO KIO","BUKIT TIMAH")
singaporegraph.masukanEdge("ANG MO KIO","CHOA CHU KANG")
singaporegraph.masukanEdge("ANG MO KIO","MANDAI")
singaporegraph.masukanEdge("ANG MO KIO","SENGKANG")
singaporegraph.masukanEdge("ANG MO KIO","PAYA LEBAR")
singaporegraph.masukanEdge("MANDAI","SEMBAWANG")
singaporegraph.masukanEdge("MANDAI","KRANJI")
singaporegraph.masukanEdge("MANDAI","CHOA CHU KANG")
singaporegraph.masukanEdge("MANDAI","BUKIT TIMAH")
singaporegraph.masukanEdge("MANDAI","ANG MO KIO")
singaporegraph.masukanEdge("MANDAI","PAYA LEBAR")
singaporegraph.masukanEdge("MANDAI","SENGKANG")
singaporegraph.masukanEdge("KRANJI","CHOA CHU KANG")
singaporegraph.masukanEdge("KRANJI","MANDAI")
singaporegraph.masukanEdge("KRANJI","SEMBAWANG")
singaporegraph.masukanEdge("SEMBAWANG","KRANJI")
singaporegraph.masukanEdge("SEMBAWANG","MANDAI")
singaporegraph.masukanEdge("SEMBAWANG","SENGKANG")

singaporegraph.printGraph()
