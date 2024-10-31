graph = {
    'S': ['A', 'B' , 'D'],
    'A': ['C'],
    'B' : ['D'],
    'C' : ['D','G'],
    'D' : ['G'],
}

def DFS(graph , start , goal):
    stack =[[start]]
    while stack :
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        else:
            child = graph.get(node,[])
            for node2 in child:
                if node2 not in path:
                    new_path = list(path)
                    new_path.append(node2)
                    stack.append(new_path)
                    
                    
path = DFS(graph,'S','G')
print(path)     