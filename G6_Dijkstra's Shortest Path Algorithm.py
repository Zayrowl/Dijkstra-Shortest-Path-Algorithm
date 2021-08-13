from collections import defaultdict, deque
cityInStr = ["Sentul","Gombak","Kepong","Selayang","Setapak","Ampang","Setiawangsa"]
cityInNum = [0,1,2,3,4,5,6]
pathStr = []
class Graph(object):
    def __init__(self,vertices):
        self.V= vertices 
        self.nodes = set() 
        self.edges = defaultdict(list) 
        self.graph = defaultdict(list)
        self.distances = {} 

    def add_node(self, value):
        self.nodes.add(value) 
        
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance 
        
    def printAllPathsUtil(self, u, d, visited1, path1):
        global cityInStr
        global cityInNum
        global pathStr
        visited1[u]= True 
        path1.append(u)  
  
        if u ==d:
            pathStr =[]
            for i in path1:
                pathStr.append(cityInStr[i])
            print(pathStr)
        else: 
            for i in self.graph[u]: 
                if visited1[i]==False: 
                    self.printAllPathsUtil(i, d, visited1, path1) 
                      
        path1.pop() 
        visited1[u]= False
 
    def printAllPaths(self,s, d):
        visited1 =[False]*(self.V) 
        path1 = [] 
        self.printAllPathsUtil(s, d,visited1, path1) 

def dijkstra(graph, initial):
    visited = {initial: 0} #dictionary
    path = {} # dictionary

    nodes = set(graph.nodes) # creates a set object
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited: 
                if min_node is None:
                    min_node = node 
                elif visited[node] < visited[min_node]: 
                    min_node = node 
        if min_node is None:
            break
        
        nodes.remove(min_node) 
        current_weight = visited[min_node]  
        for edge in graph.edges[min_node]: 
            try:
                weight = current_weight + graph.distances[(min_node, edge)] 
            except:
                continue
            if edge not in visited or weight < visited[edge]: 
                visited[edge] = weight                        
                path[edge] = min_node                         
#     print("path",path)
#     print("visited",visited)
    return visited, path


def shortest_path(graph, origin, destination): 
    visited, paths = dijkstra(graph, origin) #call function
    full_path = deque() # declaring deque
    _destination = paths[destination] #paths["Selayang"] = "Gombak"
#     print("Paths[destination]",_destination)

    while _destination != origin: 
        full_path.appendleft(_destination) #first element = "Gombak"
        _destination = paths[_destination] #paths["Gombak"] = "Sentul"

    full_path.appendleft(origin) 
    full_path.append(destination) 

    return visited[destination], list(full_path)

if __name__ == '__main__':

    graph = Graph(7)
    for node in ["Sentul","Gombak","Kepong","Selayang","Setapak","Ampang","Setiawangsa"]:
        graph.add_node(node) 
    
    graph.add_edge("Sentul", "Gombak", 11)
    graph.add_edge("Sentul", "Kepong", 8)
    graph.add_edge("Gombak", "Selayang", 2)
    graph.add_edge("Kepong", "Selayang", 8)
    graph.add_edge("Gombak", "Setapak", 25)
    graph.add_edge("Selayang", "Setapak", 27)
    graph.add_edge("Setapak", "Ampang", 23 )
    graph.add_edge("Ampang", "Setiawangsa", 7)
    print("====================================================================================================================================")
    print("City availability : " , cityInStr)
    print("Please enter your starting and ending city: ")
    src = input("Start : " )
    while src != "Sentul" and src != "Gombak" and src != "Kepong" and src != "Selayang" and src != "Setapak" and src != "Ampang" and src != "Setiawangsa":
        src = input("Invalid input. Please enter another start: ")
    end = input("End   : " )
    while end != "Sentul" and end != "Gombak" and end != "Kepong" and end != "Selayang" and end != "Setapak" and end != "Ampang" and end != "Setiawangsa":
        end = input("Invalid input. Please enter another start: ")
    
    g = Graph(7) # 7 nodes
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 3) 
    g.addEdge(2, 3) 
    g.addEdge(1, 4) 
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
     
    startInNum = 0
    startInStr = "null"
    finishInNum = 0
    finishInStr = "null"
    for i in cityInNum: 
        if src == cityInStr[i]:
            startInNum = cityInNum[i]
            startInStr = cityInStr[i]
        if end == cityInStr[i]:
            finishInNum = cityInNum[i]
            finishInStr = cityInStr[i]
        
    print("\n====================================================================================================================================")
    print ("These are the all unique paths from node {} to {} :\n".format(startInStr,finishInStr)) # in str
    g.printAllPaths(startInNum, finishInNum) # in num

    dist, pathss = shortest_path(graph, src, end)
    print("\n====================================================================================================================================")
    print("The shortest path from {} to {} is {} km with the paths : {}".format(src,end,dist,pathss))
    print("====================================================================================================================================")
