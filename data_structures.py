print("-----------------------------LINKED LISTS-----------------------------")
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return self.value
class LinkedList:
    def __init__(self,node):
        self.head=node
    def __str__(self):
        curr=self.head
        txt=""
        while curr:
            txt+=str(curr.value)+" "
            curr=curr.next
        return txt
    def contains(self,val):
        curr=self.head
        while curr:
            if curr.value==val:
                return True
            curr=curr.next
        return False
    def append(self,val):
        node=Node(val)
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=node
        node.prev=curr
        return 1
    def delVal(self,val):
        if self.head.value==val:
            self.head=self.head.next
        curr=self.head
        while curr:
            if curr.value==val:
                curr.prev.next=curr.next
                curr.next.prev=curr.prev
                return 1
            curr=curr.next
        return -1
a=Node(4)

lista=LinkedList(a)

lista.append(6)
lista.append(5)
print(lista)
print(lista.contains(5))
print(lista.contains(78))
lista.delVal(6)
print(lista)

print("----------------------------------STACK-------------------------------")
class StackNode:
    def __init__(self,val):
        self.next=None
        self.value=val
    def __str__(self):
        return str(self.value)
class Stack:
    size=0
    def _init__(self):
        self.top=None
        self.size=0
    def push(self,val):
        node=StackNode(val)
        if self.size !=0:
            node.next=self.top
        self.top=node
        self.size+=1
    def pop(self):
        if self.size==0:
            return None
        curr=self.top
        self.top=self.top.next
        return curr
    def __str__(self):
        txt=""
        if self.size==0:
            return txt
        curr=self.top
        while curr:
            txt=txt+str(curr.value)+"\n"+"v"+"\n"
            curr=curr.next
        return txt
stek=Stack()
stek.push(3)
stek.push(4)
stek.push(6)
print(stek.top)
print(stek.size)
print(stek.pop())
print(stek)
print("----------------------------------QUEUE-------------------------------")
class QueueNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.back=None
        self.size=0
    def enqueue(self,val):
        node=QueueNode(val)
        if self.size==0:
            self.front=node
            self.back=node
        else:
            self.back.next=node
            self.back=node
        self.size+=1
        return 1
    def dequeue(self):
        if self.size==0:
            return None
        if self.size==1:
            head=self.front
            self.back=None
            self.front=None
            head.next=None
            self.size-=1
            return head.val
        head=self.front
        self.size-=1
        self.front=self.front.next
        head.next=None
        return head.val
    def __str__(self):
        if self.size==0:
            return ""
        txt=""
        curr=self.front
        while curr:
            txt=txt+str(curr.val)+"<-"
            curr=curr.next
        return txt


a=Queue()
a.enqueue(5)
a.enqueue(8)
a.enqueue(9)
a.dequeue()
a.dequeue()
a.dequeue()
a.dequeue()
a.dequeue()
a.enqueue(4)
a.enqueue(5)
print(a)


print("-----------------------------------------BINARY TREE-------------------------------------")
class TreeNode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.value=val

#ne treba nam posebna klasa za drvo, nego treba samo da pratimo korijen drveta
#Breadth first traversal-Posmatramo nivo po nivo
def BreadthFirstSearch(root):
    queue=Queue()
    queue.enqueue(root)
    while queue.size>0:
        curr=queue.dequeue()
        print(curr.value)
        if(curr.left):
            queue.enqueue(curr.left)
        if(curr.right):
            queue.enqueue(curr.right)
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)
g=TreeNode(7)
h=TreeNode(8)
i=TreeNode(9)

a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
d.left=h
d.right=i

#                 a(1)
#            /           \
#             b(2)           c(3)
#          /       \      /           \ 
#         d(4)     e(5)  f(6)         g(7)
#     /         \   
#    h(8)       i(9)



BreadthFirstSearch(a)

print("####")
#Depth first ce prvo zavrsiti sa jednom rutom u drvetu pa onda preci na drugu stranu(pogledaj primjer)
'''def DepthFirstPrint(root):
    stack=[root]
    while len(stack)>0:
        curr=stack.pop()
        print(curr.value)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)'''
#rekurzivna verzija
def preOrder(root):
    #self,left,right(prvo parent node, pa lijevo, pa desno)
    if not root:
        return
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)
preOrder(a)
print("####")
def inOrder(root):
    #left,self,right
    if not root:
        return
    inOrder(root.left)
    print(root.value)
    inOrder(root.right)
inOrder(a)
print("####")
def postOrder(root):
    #left,right,self
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.value)
postOrder(a)

print("------------------------------------GRAPHS----------------------------------------------")
#GRAPHS
'''there are few ways you can represent graph data structure. Graphs are used fro representing 
social networks, map of roads, internet etc. There are a few terms to remember when talking about graphs
UNDIRECTED GRAPH
DIRECTED GRAPH
CYCLIC GRAPH
WEIGHTED GRAPH'''


class GraphNode:
    def __init__(self,val):
        self.value=val
'''        C---A---B------
           |   |   |     |
           ----D----     |
               |         |
               ----------E
'''

nodeA=GraphNode("A")
nodeB=GraphNode("B")
nodeC=GraphNode("C")
nodeD=GraphNode("D")
nodeE=GraphNode("E")





#REPRESENTATION THROUGH LISTS OF EDGES AND NODES
list_of_nodes=[nodeA,nodeB,nodeC,nodeD,nodeE]
list_of_edges=[
    [nodeA,nodeC],
    [nodeA,nodeB],
    [nodeA,nodeD],
    [nodeC,nodeD],
    [nodeB,nodeD],
    [nodeD,nodeE],
    [nodeE,nodeB]
]



#FUNKCIJA KOJA ZA DATI CVOR VRACA SVE SUSJEDNE
def adjecent_nodes(node):
    arej=[]
    for i in list_of_edges:
        if node in i:
            if i[0]==node:
                arej.append(i[1])
            else:
                arej.append(i[0])
    return arej

for i in adjecent_nodes(nodeA):
    print(i.value)


#FUNKCIJA KOJA PROVJERAVA DA LI SU DVA CVORA SUSJEDNA
def is_connected(node_a,node_b):
    return node_b in adjecent_nodes(node_a)
print(is_connected(nodeA,nodeE))
print(is_connected(nodeB,nodeD))







#MATRICA KOMSIJA-dobra sto se tice vremena, losa sto se tice prostora


#napomena: kreiramo rjecnik sa indeksima cvorova da bi odzali vremensku efikasnost
node_indices={nodeA:0,
              nodeB:1,
              nodeC:2,
              nodeD:3,
              nodeE:4}


adjecency_matrix=[[0,1,1,1,0],
                  [1,0,0,1,1],
                  [1,0,0,1,0],
                  [1,1,1,0,1],
                  [0,1,0,1,0]]
#FUNKCIJA KOJA VRACA SUSJEDNE CVOROVE
def adjecent_nodes_am(node):
    t=node_indices[node]
    arr=[]
    for i in range(len(adjecency_matrix)):
        if adjecency_matrix[t][i]==1:
            arr.append(list_of_nodes[i])
    return arr
for i in adjecent_nodes_am(nodeA):
    print(i.value)
#FUNKCIJA KOJA PROVJERAVA DA LI SU DVA CVORA SUSJEDNA
def is_adjecent(node_a,node_b):
    return adjecency_matrix[node_indices[node_a]][node_indices[node_b]]==1

print(is_adjecent(nodeA,nodeE))
#LISTA KOMSIJA-malcice prostorno efikasnja od prosle
adjecency_list=[[nodeB,nodeC,nodeD],
                [nodeA,nodeD,nodeE],
                [nodeA,nodeD],
                [nodeA,nodeB,nodeC,nodeE],
                [nodeB,nodeD]]
def adjecent_nodes_al(adj_list,node,node_indices):
    return  adj_list[node_indices[node]]




def is_adjecent_al(node_a,node_b,adj_list):
    return node_b in adjecent_nodes_al(adj_list,node_a,node_indices)

def depth_first_search_graph(root,adj_list):
    kju=Queue()
    kju.enqueue(root)
    list_visited=set()
    while kju.size>0:
        curr=kju.dequeue()
        print(curr.value,end="->")
        list_visited.add(curr)
        for i in adjecent_nodes_al(adj_list,curr,node_indices):
            if not i in list_visited:
                list_visited.add(i)
                kju.enqueue(i)
    print()
depth_first_search_graph(nodeA,adjecency_list)





#EXERCISE: Given the graph of friends on facebook, find the shortest route between two people
Mario=GraphNode("Mario")
Anna=GraphNode("Anna")
Jelena=GraphNode("Jelena")
Vladimir=GraphNode("Vladimir")
Pero=GraphNode("Pero")
Luz=GraphNode("Luz")

adjecency_list2=[[Anna,Pero,Vladimir,Luz],
                 [Luz,Mario],
                 [Pero,Luz],
                 [Mario,Pero],
                 [Jelena,Mario,Vladimir],
                 [Anna,Mario,Jelena]]
list_of_nodes2=[Mario,Anna,Jelena,Vladimir,Pero,Luz]

node_indices2={Mario:0,
              Anna:1,
              Jelena:2,
              Vladimir:3,
              Pero:4,
              Luz:5}





def path(start,end,visited):
    curr=end
    route=[]
    while curr:
        route.append(curr)
        curr=visited[curr]
    return route[::-1]




def find_shortest(start,end,adj_list):
    kju=Queue()
    kju.enqueue(start)
    visited={}
    visited[start]=None
    while kju.size>0:
        node=kju.dequeue()
        adjecent=adjecent_nodes_al(adj_list,node,node_indices2)
        for i in adjecent:
            if not i in visited.keys():
                kju.enqueue(i)
                visited[i]=node
            if i==end:
                return path(start,end,visited)
t=find_shortest(Vladimir,Anna,adjecency_list2)
for i in t:
    print(i.value,end="<->")
#PROBLEM: Create a function for floodfill algorithm
t=[["C","C","Y","Y","Y","B"],
   ["C","Y","Y","Y","B","B"],
   ["C","C","Y","B","B","Y"],
   ["C","G","Y","Y","B","Y"],
   ["G","G","G","Y","Y","Y"],
   ["G","G","G","G","G","Y"]]
def checkValid(table,processed,x,y):
    return 0<=x<len(table[0]) and 0<=y<len(table) and processed[y][x]
def floodfill(table,color,y,x,processed=[[]],curr_color=""):
    if processed==[[]]:
        processed=[[False for x in range(len(table[0]))] for y in range(len(table))]
        curr_color=table[y][x]
    
    table[y][x]=color
    processed[y][x]=True


    for i in range(-1,2):
        for k in range(-1,2):
            if checkValid(table,processed,x+i,y+k):
                table=floodfill(table,color,y,x,processed,curr_color)
    return table

t=floodfill(t,"X",2,2)
for i in t:
    for k in i:
        print(t[i][k], end=" ")
    print()
