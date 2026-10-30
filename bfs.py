import json

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

    # All nodes have not been visited
    # We don't know the distance between the source and any other node
    # There are no predecessors at this point
    for node in network:
        visited[node] = False
        distance[node] = float("inf")
        predecessor[node] = None

    # Do the setup for the source
    visited[source] = True
    distance[source] = 0

    Q = [source]

    # As long as there are nodes to be processed
    while Q != []:
        current_node = Q.pop(0)     # Getting a node off of the front of the queue

        # As long as the node has not already been visited, update the table
        # and put neighbors on the queue.
        for neighbor in network[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                predecessor[neighbor] = current_node
                distance[neighbor] = distance[current_node] + 1

                Q.append(neighbor)

    # Returning a tuple that contains two dictionaries
    return distance, predecessor

if __name__ == "__main__":
    with open("friend_graph.json", "r") as file:
        graph = json.load(file)

    graph_dist, graph_pred = bfs(graph, "Liam")

    print(graph_dist)
    print(graph_pred)