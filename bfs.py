import json

with open("friend_graph.json", "r") as file:
    graph = json.load(file)

def bfs(network, source):
    '''
    Purpose:
    Parameters:
    Return Values:
    '''

    # Three dictionaries to keep track of where we've been, distances, and
    # predecessors

    visited = {}
    distance = {}
    predecessor = {}

    for node in network:
        visited[node] = False
        distance[node] = float("inf")
        predecessor[node] = None

    visited[source] = True
    distance[source] = 0

    Q = [source]