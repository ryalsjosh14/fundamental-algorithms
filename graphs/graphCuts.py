import random
import math
import copy


def minCut(vertices, edgs):
    """
    Finds the minimum cut of a given graph. A Cut is a separation of a graph into two graphs. A minimum cut is
    the cut which has the minimum number of crossing edges between the two newly-formed graphs. This function computes
    the mincut using a random contraction algorithm
    :param vertices: List of all vertices of graph
    :param edges: List of all edges of the graph. Each edge is represented only once in list - [vertex1, vertex2]
    :return: The final 2 merged vertices, and number of edges between the 2 (crossing edges)
    """
    #Make copies of args in order to avoid mutating arg references
    verts = copy.deepcopy(vertices)
    edges = copy.deepcopy(edgs)

    #Perform algorithm until there are only two vertices left (there is a cut)
    while len(verts) > 2:

        #Pick random vertex
        rand_idx = random.randint(0, len(edges)-1)
        [first_vertex, merge_vertex] = edges.pop(rand_idx)

        #merge edges for vertices to be merged (first_Vertex, random_vertex)
        new_edges = []
        for edge in edges:
            if edge[0] == merge_vertex:
                edge[0] = first_vertex
            elif edge[1] == merge_vertex:
                edge[1] = first_vertex

            #If the edge is self-loop, remove it
            if edge[0] != edge[1]:
                new_edges.append(edge)

        edges = new_edges

        #Remove the vertex which has now been merged to first vertex
        verts.remove(merge_vertex)

    return verts, len(edges)


if __name__ == '__main__':
    """
    Since this is a random contraction algorithm, it must be ran multiple times to ensure accuracy. Through some math,
    it can be proven that P(finding the true mincut) = (n-1)/n if the algorithm is run n^2*log(n) times.
    """
    #tests
    verts = [1, 2, 3, 4, 5, 6, 7, 8]
    edgs = [[1,2], [3,1], [4,1], [2,3], [6,3], [5,6], [4,6], [5,4], [6,8], [4,8], [1,7]]
    n = len(verts)

    min = len(edgs)
    mincut_vertices = verts

    # Run algo n^2 ln(n) times
    for i in range(math.floor((n**2) * math.log(n))):
        final_verts, num_edges = minCut(verts, edgs)
        if num_edges < 2:
            mincut_vertices = final_verts
            min = 1
            print("min of iteration {}: {}".format(i, num_edges))
            break
        elif num_edges < min:
            min = num_edges
            mincut_vertices = final_verts

        print("min of iteration {}: {}".format(i, num_edges))

    print("Mincut, final vertices: {}, final edges: {}".format(mincut_vertices, min))
