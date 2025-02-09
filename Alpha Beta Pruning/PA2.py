pruned=[]

def max_prune(node,index,alpha,beta):
    for i in range(len(node["children"])):
        node["value"] = max(node["value"],min_prune(node["children"][i],index*2+i,alpha,beta))
        if node["value"]>=beta and i==0:
            pruned.append(index*2+1)
            return node["value"]
        alpha=max(node["value"],alpha)

    return node["value"]
    
        
def min_prune(node,index,alpha,beta):
    for i in range(len(node["children"])):
        node["value"] = min(node["value"],max_prune(node["children"][i],index*2+i,alpha,beta))
        if node["value"]<=alpha and i==0:
            pruned.append(index*4+2)
            pruned.append(index*4+3)
            return node["value"]
        beta=min(node["value"],beta)

    return node["value"]


values = input()
values = list(map(int,values.split()))

#Generating Leaf nodes
leaf = []
for i in range(len(values)):
    node = {"value": values[i], "children":[]}
    leaf.append(node)

#Generating max nodes
max_nodes = []
for i in range(6):
    node = {"value":-float('inf'),"children":[leaf[2*i].copy(),leaf[2*i+1].copy()]}
    max_nodes.append(node)

#Generating min nodes
min_nodes = []
for i in range(3):
    node = {"value":float('inf'),"children":[max_nodes[2*i].copy(),max_nodes[2*i+1].copy()]}
    min_nodes.append(node)

#Generating root node
root = {"value":-float('inf'),"children":min_nodes}
max_prune(root,0,-float('inf'),float('inf'))

#Printing pruned nodes
print(" ".join(list(map(str,pruned))))