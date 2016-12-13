#!/usr/local/bin/python3
import sfp


start = "s"
end = "v"
G = {'s':{'u':10, 'x':5}, 'u':{'v':1, 'x':2}, 'v':{'y':4}, 'x':{'u':3, 'v':9, 'y':2}, 'y':{'s':7, 'v':6}}

print("Shortest Length: ", sfp.Dijkstra(G, start)[0][end])
print("Shortest Path: ", sfp.shortestPath(G, start, end))




