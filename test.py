from queue import LifoQueue
from queue import Queue

class Node :

    def __init__(self, name) :
        self.name = name
        self.edges = []

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
        
        node_arad.edges = [
            Edge(node_zerind, 75),
            Edge(node_timisoara,118)
        ]

        node_zerind.edges = [
            Edge(node_oradea,71),
            Edge(node_arad,75)
        ]

        self.nodes = {
            "Arad": node_arad,
            "Zerind": node_zerind,
            "Oradea": node_oradea
        }

def bfs(starting_city, destination_city):
    queue = Queue(maxsize=0)
    graph = Graph()
    start_node = graph.nodes[starting_city]
    end_node = graph.nodes[destination_city]
    queue.put(start_node)
    end = True
    while queue and end :
        node = queue.get()
        print(node.name)
        for edge in node.edges:
            if edge.node == end_node:
                print(node.name)
                end = False
                break
            else:
                queue.put(edge.node)

def main():
    bfs("Arad","Oradea")

if __name__ == "__main__":
    main()
