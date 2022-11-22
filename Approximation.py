
import numpy as np

#parent = list(np.zeros(100005,))

#d = list(np.zeros(100005,))
#size = list(np.zeros(100005,))

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
        parent[i] = 1
        size[i] = 1

    for i in range(noofvertices):
        s1 = []
        d1 = 0

        v = i
        for j in range(len(G[i])):
            u = G[i][j]
            if((findparent(u) != findparent(v)) and( [u,findparent(u)] not in s1)):
                d1 = d1 + 1
                s1.append([u,findparent(u)])
                # s1 = s1.update({u : findparent(u)})
    
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
    for i in inputedges:
        G[i[0]].append(i[1])
        G[i[1]].append(i[0])

    
    F = buildMaximallyLeafyForest(noofvertices,G)
    print(F)
