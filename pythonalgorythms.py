
import math

class Graph():

    class Vertex():
        def __init__(self, label):
            self.label = label
            self.edges = [] #edge: (label, weight, ptr)

        def __str__(self):
            build = ""
            for edge in self.edges:
                build += "   "
                build += self.label
                build += " -> "
                build += edge[0]
                build += '[label="'
                build += str(edge[1])
                build += '",weight="'
                build += str(edge[1])
                build += '"];\n'
            return build

    def __init__(self):
        self._verts = []

    def Validate(self, vert_label):
        for vert in self._verts:
            if (vert_label == vert.label):
                return vert
            
        raise ValueError("Vertex not in graph")

    def add_vertex(self, label):
        if (isinstance(label, str)):
            newvert = self.Vertex(label)
            self._verts.append(newvert)
        else: raise ValueError("label must be a string")
        
        return self
        
    def add_edge(self, src, dest, w):
        source = self.Validate(src)
        destiny = self.Validate(dest)
        if (isinstance(w, float)):
            newedge = (destiny.label, w, destiny)
            source.edges.append(newedge)
            source.edges.sort()
        else: raise ValueError("weight must be a float")

    def get_weight(self, src, dest):
        source = self.Validate(src)
        destiny = self.Validate(dest).label

        for edge in source.edges:
            if (destiny == edge[0]):
                return edge[1]
        
        return math.inf
    
    def dfs(self, starting_vertex):
        first = self.Validate(starting_vertex)
        vStack = [first]
        visited = set()

        while (len(vStack) > 0):
            curr = vStack.pop(0)
            if (curr.label not in visited):
                yield curr.label
                visited.add(curr.label)
                temp = []
                for edge in curr.edges:
                    temp.append(edge)
                for e in reversed(temp):
                    vStack.insert(0, e[2])


    def bfs(self, starting_vertex):
        first = self.Validate(starting_vertex)
        frontierQ = [first]
        discoveredSet = {starting_vertex}

        while (len(frontierQ) > 0):
            curr = frontierQ.pop(0)
            yield curr.label
            for edge in curr.edges:
                if (edge[0] not in discoveredSet):
                    frontierQ.append(edge[2])
                    discoveredSet.add(edge[0])

    def unreachable(self, vert):
        pass

    def dsppath(self, src):
        start = self.Validate(src)
        queue = [start]
        checked = set()
        checking = set()

        path = dict()
        for vert in self._verts:
            path[vert.label] = (math.inf, None)
            checking.add(vert.label)

        path[start.label] = (0, None)

        while (len(queue) > 0):
            curr = queue.pop(0)

            for edge in curr.edges:
                queue.append(edge[2])  
                altpath = (path[curr.label][0] + edge[1])
                key = edge[0]
                if (path[key][0] > altpath):
                    path[key] = (altpath, curr)

            checked.add(curr.label)
            if(checked == checking):
                break

        return path

    def dsp(self, src, dest):
        start = self.Validate(src)
        destiny = self.Validate(dest)
        pathdic = self.dsppath(src)
        try: 
            pathlen = pathdic[dest][0]
        except KeyError:
            pathlen = math.inf
            return (pathlen, [])

        path = []
        curr = destiny
        while (src not in path):
            path.insert(0, curr.label)
            curr = pathdic[curr.label][1]

        return (pathlen, path)

    def dsp_all(self, src):
        start = self.Validate(src)
        pathdic = self.dsppath(src)
        dpath = dict()

        for vert in self._verts:
            curr = vert
            path = []
            while (src not in path):
                path.insert(0, curr.label)
                curr = pathdic[curr.label][1]

            dpath[vert.label] = path
        
        return dpath

    def __str__(self):
        comp_build= "digraph "
        comp_build += self.name
        comp_build += " {\n"
        for vert in self._verts:
            comp_build += str(vert)
        comp_build += "}"
        return comp_build

def main():
    G = Graph("G")
    G.add_vertex("A")
    G.add_vertex("B")
    G.add_vertex("C")
    G.add_vertex("D")
    G.add_vertex("E")
    G.add_vertex("F")

    G.add_edge("A", "B", 2.0)
    G.add_edge("A", "F", 9.0)
    G.add_edge("B", "C", 8.0)
    G.add_edge("B", "D", 15.0)
    G.add_edge("B", "F", 6.0)
    G.add_edge("C", "D", 1.0)
    G.add_edge("E", "C", 7.0)
    G.add_edge("E", "D", 3.0)
    G.add_edge("F", "E", 3.0)
    G.add_edge("F", "B", 6.0)

    print(G)
    print()

    print("Starting BFS with vertex A")
    for vertex in G.bfs("A"):
        print(vertex, end = "")
    print()

    print("starting DFS with vertex A")
    for vertex in G.dfs("A"):
        print(vertex, end = "")
    print()

    print("Dijkstra's Shortest Path:")
    print(G.dsp("A", "B"))
    print(G.dsp("A", "E"))
    print(G.dsp_all("A"))
    




if (__name__=="__main__"):
    main()