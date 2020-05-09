from collections import defaultdict
import math

class Graph:

    def __init__(self):
        #Graph is [node, [nodeConnection 1, nodeConnection2, ...]]
        self.graph = defaultdict(list)
        self.current_label = len(self.graph)
        #self.explored = []

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if self.graph[v] == None:
            self.graph[v] == []

    def removeEdge(self, u, v):
        self.graph[u].remove(v)

    #TODO: check edge cases
    def BFS(self, s, v):
        """
        Uses breadth-first search to find the shortest distance from s to v. This implementation still explores every
        node and does not break when the shortest distance to v is found. This demonstrates the full power of BFS
        :param s: starting index
        :param v: The "finish" index of which to find the shortest distance from s
        :return: The minimum number of edges to be explored to get to v from s (distance)
        """
        #Initialize distance from s to v as infinity, unless they are the same node, where distance is 0
        dist = {}
        dist[v] = math.inf if s != v else 0
        dist[s] = 0

        #Initialize list of explored nodes with value of s
        explored = {}
        for vert in self.graph:
            explored[vert] = False

        explored[s] = True

        #Initialize queue of nodes to be explored
        queue = [s]

        #Whie the queue is not empty, explore neighbors of next vertex
        while len(queue) != 0:
            #Get next vertex
            u = queue.pop(0)

            #Add all unexplored, connected vertices to queue and mark as explored
            for w in self.graph[u]:
                if not explored[w]:
                    dist[w] = dist[u] + 1
                    explored[w] = True
                    queue.append(w)

        return dist[v]


    def DFS_loop(self, s, explored, f):
        """
        Performs DFS on a given start node to find a topological ordering. Assigns a label from each node signifying the
        ordering. This labeling starts from the sink (end) node and works back to the first (start) node.
        :param s: The start node
        :return: None, This alters the instance variable f
        """
        #Set start node to explored
        explored[s] = True

        #Perform DFS on all unvisited nodes connected to s
        for w in self.graph[s]:
            if not explored[w]:
                self.DFS_loop(w, explored, f)

        #Put node in its proper place in ordering
        f[self.current_label-1] = s

        #Increment current label down by 1
        self.current_label -= 1



    def DFS(self):
        """
        An outer loop to implement DFS on each node in order to find the topological ordering of a graph.
        :return: f, an array with the topological ordering of the graph.
        """

        #Initialize all nodes as not visited
        explored = {}
        for v in self.graph:
            explored[v] = False

        #Start the current label index as the number of nodes in the graph
        self.current_label = len(self.graph)

        #Initialize ordering as array of zeros
        f = [0] * len(self.graph)

        # Perform DFS on all unexplored vertices
        for v in self.graph:
            if not explored[v]:
                self.DFS_loop(v, explored, f)

        #Rrturn topological ordering of graph
        return f



    def FindComponents(self):
        """
        Finds the strongly connected components (SCC) of a given graph using Kosaraju's algorithm
        :return: Sol: A list of the SCC's of a given graph
        """
        #Call DFS to get the toplogical ordering of the graph
        order = self.DFS()
        #Get the reversed graph
        reversed_graph = self.reverseGraph()

        #Initialize all nodes as unexplored
        explored = {}
        for v in reversed_graph:
            explored[v] = False

        #Initialize solution as empty list
        sol = []

        #Go through each vertex in the order of the topoligcal ordering
        for v in order:
            #reset SCC as empty for each SCC
            SCC = []
            #If vertex not already in another SCC, find the SCC
            if not explored[v]:
                #Perform DFS on reversed graph
                self.findComponentsDFS(reversed_graph, v, explored, SCC)
                #Add SCC to final solution
                sol.append(SCC)

        return sol

    @staticmethod
    def findComponentsDFS(rev_graph, s, explored, SCC):
        """
        :param rev_graph: The original graph with all arcs reversed
        :param s: Vertex to start DFS at
        :param explored: Dictionary of nodes and their explored status
        :param SCC: A list with all the nodes in the current SCC
        :return: None, alters variable SCC
        """

        # Set start node to explored
        explored[s] = True

        # Perform DFS on all unvisited nodes connected to s
        for w in rev_graph[s]:
            if not explored[w]:
                Graph.findComponentsDFS(rev_graph, w, explored, SCC)

        SCC.append(s)



    def reverseGraph(self):
        """
        Creates a new graph with all arcs of the current graph reversed
        """
        scc_graph = Graph()
        for v in self.graph:
            for w in self.graph[v]:
                scc_graph.addEdge(w,v)
        return scc_graph.graph



if __name__ == '__main__':

    #test
    g = Graph()
    g.addEdge('h', 'i')
    g.addEdge('i', 'j')
    g.addEdge('j', 'g')
    g.addEdge('j', 'k')
    g.addEdge('a', 'b')
    g.addEdge('b', 'c')
    g.addEdge('c', 'a')
    g.addEdge('b', 'd')
    g.addEdge('d', 'e')
    g.addEdge('e', 'f')
    g.addEdge('f', 'd')
    g.addEdge('g', 'f')
    g.addEdge('g', 'h')

    print(g.BFS('a', 'h'))
    print(g.FindComponents())




