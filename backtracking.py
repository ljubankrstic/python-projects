# Problem nalazenja povezanih clanova (ostrva)
n = 9


class Node:
    def __init__(self, value):
        self.value = value
        self.id = None


nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")
nodeI = Node("I")
nodeJ = Node("J")
nodeK = Node("K")
nodeL = Node("L")
nodeM = Node("M")
adj_list = {
    nodeA: [nodeB, nodeC],
    nodeB: [nodeA, nodeC],
    nodeC: [nodeA, nodeB],
    nodeD: [nodeE],
    nodeE: [nodeD],
    nodeF: [nodeG, nodeH],
    nodeG: [nodeF, nodeH],
    nodeH: [nodeF, nodeG],
    nodeI: []
}
node_indices = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH, nodeI]
visited = [False for _ in range(9)]


def solution():
    n = 0
    for i in range(len(node_indices)):
        if not visited[i]:
            n += 1
        dfs(i, n, True)


def dfs(i, n, valid=False):
    if visited[i]:
        return
    node_indices[i].id = n
    visited[i] = True
    for k in adj_list[node_indices[i]]:
        dfs(node_indices.index(k), n)


solution()
for i in node_indices:
    print(i.id)
# Topolosko sortiranje
adj_list = {
    nodeA: [nodeD],
    nodeB: [nodeD],
    nodeC: [nodeA, nodeB],
    nodeD: [nodeH, nodeG],
    nodeE: [nodeA, nodeD, nodeF],
    nodeF: [nodeK, nodeJ],
    nodeG: [nodeI],
    nodeH: [nodeJ, nodeI],
    nodeI: [nodeL],
    nodeJ: [nodeM, nodeL],
    nodeK: [nodeJ],
    nodeL: [],
    nodeM: []
}
node_indices = [nodeA, nodeB, nodeC, nodeD, nodeE, nodeF,
                nodeG, nodeH, nodeI, nodeJ, nodeK, nodeL, nodeM]
sorty=[]



def dfs(i):
    if visited[node_indices.index(i)]==True:
        return
    if adj_list[i]==[]:
        sorty.append(i)
        visited[node_indices.index(i)]==True
        return
    t=0
    for k in adj_list[i]:
        if visited[node_indices.index(k)]==False:
            t+=1
    if t==0:
        sorty.append(i)
        visited[node_indices.index(i)]==True
        return
    for k in adj_list[i]:
        dfs(k)
    visited[node_indices.index(i)]=True



def topological_sort():
    visited=[False for i in range(13)]
    for i in node_indices:
        dfs(i)


topological_sort()
for i in sorty.reverse():
    print(i.value,end="->")