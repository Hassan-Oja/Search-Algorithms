graph = {
    'S': ['A', 'B' , 'D'],
    'A': ['C'],
    'B' : ['D'],
    'C' : ['D','G'],
    'D' : ['G'],
}

def BFS(graph , start , goal):
    queue =[[start]]
    while queue :
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        else:
            child = graph.get(node,[])
            for node2 in child:
                if node2 not in path:
                    new_path = list(path)
                    new_path.append(node2)
                    queue.append(new_path)
                    
                    
path = BFS(graph,'S','G')
print(path)                    