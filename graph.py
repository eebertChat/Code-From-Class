import json

# Friend Network Graph
# Every key is a node for the person
# Every value is a list of the individual's friends

graph = {
    "Liam" : ["Emma", "Raj"],
    "Emma" : ["Chen", "Liam", "Sofia"],
    "Raj"  : ["Liam","Priya"],
    "Priya" : ["Raj", "Aiko"],
    "Aiko" : ["Noah", "Priya", "Sofia"],
    "Sofia" : ["Aiko", "Emma", "Chen"],
    "Chen" : ["Emma", "Noah", "Sofia"],
    "Noah" : ["Aiko", "Chen"]
}

# Another way to handle files
# with will automatically close the file when file operations are completed
# or the program ends.
with open("friend_graph.json", "w") as file:
    json.dump(graph, file, indent=4)

