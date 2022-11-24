
import numpy as np


parent = list(np.zeros(100005,))
d = list(np.zeros(100005,))
size = list(np.zeros(100005,))

def findparent(v):
    if(v == parent[v]):
        return v
    parent[v] = findparent(parent[v])
    return parent[v]

def unionbyrank(u,v):
    a = findparent(u)
    b = findparent(v)
    if(a!=b):
        if(size[a] > size[b]):
            parent[b] = a
            size[a] = size[a] + size[b]
        else:
            parent[a] = b
            size[b] = size[a] + size[b]

def buildMaximallyLeafyForest(noofvertices,G):
    F = []
    for i in range(noofvertices):
        d[i] = 0
        parent[i] = i
        size[i] = 1

    for i in range(noofvertices):
        s1 = []
        d1 = 0

        v = i
        for j in range(len(G[i])):
            u = G[i][j]
            if(findparent(u) != findparent(v) and [u,findparent(u)] not in s1):
                d1 = d1 + 1
                s1.append([u,findparent(u)])
                
    
        if(d[v] + d1 >= 3):
            for i in s1:
          
                F.append([v,i[0]])
                F.append([i[0],v]) 
                unionbyrank(v,i[1])
                d[i[0]] = d[i[0]] + 1
                d[v] = d[v] + 1
    return F




parent1 = list(np.zeros(100005,))
size1 = list(np.zeros(100005,))

def findparent1(x):
    if(parent1[x] == x):
        return x
    parent1[x] = findparent1(parent1[x])
    return parent1[x]

def unionbyrank1(u,v):
    a = findparent1(u)
    b = findparent1(v)
    if(a!=b):
        if(size1[a] > size1[b]):
            parent1[b] = a
            size1[a] = size1[a] + size1[b]
        else:
            parent1[a] = b
            size1[b] = size1[a] + size1[b]


def kruskal(noofvertices,F):
    spanningtree = []
    for i in range(noofvertices):
        parent1[i] = i
    for i in F:
        x = i[0]
        y = i[1]
        if(findparent1(x) != findparent1(y)):
            spanningtree.append([x,y])
            unionbyrank1(x,y)
    return spanningtree


if __name__ == "__main__":
    noofvertices = int(input("Enter no of vertices : "))
    noofedges = int(input("No of edges : "))

    inputedges = []

    for i in range(noofedges):
        x,y = map(int, input().split())

        inputedges.append([x,y])

    G=[]
    for i in range(100005):
      G.append([]) 
    for i in range(noofedges):
        x = inputedges[i]
        G[x[0]].append(x[1])
        G[x[1]].append(x[0])

    
    F = buildMaximallyLeafyForest(noofvertices,G)
    print(F)
    verticesinF = []

    for i in F:
        verticesinF.append(i[0])
        verticesinF.append(i[1])
    
    for i in range(noofvertices):
        for j in range(len(G[i])):
            u = i
            v = G[i][j]

            if((u not in verticesinF) and (v not in verticesinF)):
                F.append([u,v])
                F.append([v,u])
                
            elif(findparent(u) != findparent(v)):
                F.append([u,v])
                F.append([v,u])
                
result = kruskal(noofvertices,F)
print("Result : ")
for i in result:
    print(str(i[0]) + " " + str(i[1]))
