# Kuruskal-Python

```

KRUSKAL(G):
A = ∅
For each vertex v ∈ G.V:
    MAKE-SET(v)
For each edge (u, v) ∈ G.E ordered by increasing order by weight(u, v):
    if FIND-SET(u) ≠ FIND-SET(v):       
    A = A ∪ {(u, v)}
    UNION(u, v)
return A

```
- Data is given in a file
- First line of file contain ```NOV <no of vertices>```
- Follwing lines consists of edges and their weights ```<vertice1> <vertice2> <weight>```
- Some example given here

```
NOV 6
0  1  4
0  2  4
1  2  2
1  0  4
2  0  4
2  1  2
2  3  3
2  5  2
2  4  4
3  2  3
3  4  3
4  2  4
4  3  3
5  2  2
5  4  3
```
## Run the programme
```
python Kuruskal.py <file name>
```
