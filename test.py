from queue import LifoQueue
from queue import Queue

class Node :

    def __init__(self, name) :
        self.name = name
        self.edges = []
        self.depth = 0

    def __repr__(self) :
        return self.name #+ " " + self.edges

    def __eq__(self, other):
        return self.name == other.name
    
class Edge :
    
    def __init__(self, node, cost) :
        self.node = node
        self.cost = cost
        
    def __repr__(self) :
        return self.node.name + " " + str(self.cost)
        
class Graph :

    def __init__(self):

        node_arad = Node("Arad")
        node_zerind = Node("Zerind")
        node_oradea = Node("Oradea")
        node_timisoara = Node("Timisoara")
        node_lugoj = Node("Lugoj")
        node_sibiu = Node("Sibiu")
        node_mehadia = Node("Mehadia")
        node_drobeta = Node("Drobeta")
        node_craiova = Node("Craiova")
        node_rimnicu_vilcea = Node("Rimnicu Vilcea")
        node_fagaras = Node("Fagaras")
        node_pitesti = Node("Pitesti")
        node_bucharest = Node("Bucharest")
        node_giurgiu = Node("Giurgiu")
        node_urziceni = Node("Urziceni")
        node_hirzova = Node("Hirzova")
        node_eforie = Node("Eforie")
        node_vaslui = Node("Vaslui")
        node_iasi = Node("Iasi")
        node_neamt = Node("Neamt")
        
        node_arad.edges = [
            Edge(node_zerind, 75),
            Edge(node_timisoara,118),
            Edge(node_sibiu, 140)
        ]

        node_zerind.edges = [
            Edge(node_oradea, 71),
            Edge(node_arad, 75)
        ]

        node_oradea.edges = [
            Edge(node_zerind, 71),
            Edge(node_sibiu, 151)
        ]

        node_timisoara.edges = [
            Edge(node_arad, 118),
            Edge(node_lugoj, 111)
        ]

        node_lugoj.edges = [
            Edge(node_timisoara, 111),
            Edge(node_mehadia, 70)
        ]

        node_mehadia.edges = [
            Edge(node_lugoj, 70),
            Edge(node_drobeta, 75)
        ]

        node_drobeta.edges = [
            Edge(node_mehadia, 75),
            Edge(node_craiova, 120)
        ]

        node_craiova.edges = [
            Edge(node_rimnicu_vilcea, 146),
            Edge(node_drobeta, 120),
            Edge(node_pitesti, 138)
        ]

        node_rimnicu_vilcea.edges = [
            Edge(node_pitesti, 97),
            Edge(node_craiova, 146),
            Edge(node_sibiu, 80)
        ]

        node_sibiu.edges = [
            Edge(node_arad, 140),
            Edge(node_oradea, 151),
            Edge(node_fagaras, 99),
            Edge(node_rimnicu_vilcea, 80)
        ]

        node_pitesti.edges = [
            Edge(node_craiova, 138),
            Edge(node_rimnicu_vilcea, 97),
            Edge(node_bucharest, 101)
        ]

        node_fagaras.edges = [
            Edge(node_bucharest, 211),
            Edge(node_sibiu, 99)
        ]

        node_bucharest.edges = [
            Edge(node_fagaras, 211),
            Edge(node_pitesti, 101),
            Edge(node_giurgiu, 90),
            Edge(node_urziceni, 85)
        ]

        node_giurgiu.edges = [
            Edge(node_bucharest, 90)
        ]

        node_urziceni.edges = [
            Edge(node_bucharest, 85),
            Edge(node_hirzova, 98),
            Edge(node_vaslui, 142)
        ]

        node_hirzova.edges = [
            Edge(node_urziceni, 98),
            Edge(node_eforie, 86)
        ]

        node_eforie.edges = [
            Edge(node_hirzova, 86)
        ]

        node_vaslui.edges = [
            Edge(node_urziceni, 142),
            Edge(node_iasi, 92)
        ]

        node_iasi.edges = [
            Edge(node_vaslui, 92),
            Edge(node_neamt, 87)
        ]

        node_neamt.edges = [
            Edge(node_iasi, 87)
        ]

        self.nodes = {
            "Arad": node_arad,
            "Zerind": node_zerind,
            "Oradea": node_oradea,
            "Neamt": node_neamt,
            "Fagaras": node_fagaras,
            "Eforie": node_eforie,
            "Rimnicu Vilcea": node_rimnicu_vilcea
        }

def bfs(starting_city, destination_city):
    queue = Queue(maxsize=0)
    graph = Graph()
    start_node = graph.nodes[starting_city]
    end_node = graph.nodes[destination_city]
    queue.put(start_node)
    not_found = True
    path = ""
    visited = []
    while queue and not_found :
        current_node = queue.get()
        path = path +" => "+ current_node.name
        visited.append(current_node)
        for edge in current_node.edges: 
            if edge.node == end_node:
                path = path + " => "+ edge.node.name
                not_found = False
                break
            else:
                if edge.node not in visited:
                    queue.put(edge.node)

    print("BFS: " + path)

def dfs(current_node, graph, end_node, limit, path = [], last_node = []):
    if current_node.depth > limit:
        return

    if current_node != end_node:
        if current_node not in path:
            path.append(current_node)
            for edge in current_node.edges:
                if(not last_node):
                    if(edge.node not in path):
                        edge.node.depth = current_node.depth + 1
                        dfs(edge.node, graph, end_node, limit, path, last_node)
                    else:
                        edge.node.depth = current_node.depth - 1
                else:
                    return path
                
    else:
        path.append(current_node)
        last_node.append(current_node)
        print(path)
        

def init_dfs(starting_city, destination_city, limit):
    graph = Graph()
    start_node = graph.nodes[starting_city]
    end_node = graph.nodes[destination_city]
    
    try:
        print(dfs(start_node, graph, end_node, limit))
    except ValueError:
        print("Stopping DFS due to limit")
    finally:
        print("DFS Stopped")
    
def main():
    bfs("Arad","Fagaras")
    #init_dfs("Arad","Eforie", 20)
    init_dfs("Arad","Rimnicu Vilcea", 2)


if __name__ == "__main__":
    main()
