class Graph():
    def __init__(self , vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = {v:[] for v in range(vertex_count)} #it create an dict with key and value is the list of vertices

    def add_edge(self ,u,v , weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v ,weight))
            self.adj_list[v].append((u ,weight))
        else:
            print("Invalid vertixes")
        
    def remove_edge(self ,u,v ):
          
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u] = [(vertex,weight) for vertex , weight in self.adj_list[u] if vertex!= v]
            self.adj_list[v] = [(vertex,weight) for vertex , weight in self.adj_list[v] if vertex!= u]
        else:
            print("Invalid vertixes")
        
        
    def has_edge(self ,u,v ):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex,x in self.adj_list[u]) #vertex=v and x= weight
        else:
            print("Invalid vertixes")
            return False

    def print_adj_list(self):
        for vertex,n in self.adj_list.items():
            print("V" ,vertex , ":", n)

g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)

g.print_adj_list()


# V 0 : [(1, 1)]
# V 1 : [(0, 1), (2, 1), (3, 1)]
# V 2 : [(1, 1), (3, 1)]
# V 3 : [(1, 1), (2, 1), (4, 1)]
# V 4 : [(3, 1)]