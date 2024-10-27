goal_state="1w2w3w4w"
swap = str.maketrans('bw', 'wb')

def printA_star(state,all_states):
    states = []
    states.insert(0,state)
    while states[0]["parent"] is not None:
        # parent = next((state for state in all_states if state["state"] == states[0]["parent"]), None)
        parent = [state for state in all_states if state["state"] == states[0]["parent"]][0]
        parent["state"] = parent["state"][:2*states[0]["flip"]] + "|" + parent["state"][2*states[0]["flip"]:]
        states.insert(0, parent)
    for i in states:
        print("{} g:{}, h:{}".format(i["state"],i["g"],i["h"]))
    return 

def flip_state(state,flip):
    x = 2*flip
    t=""
    while x> 0:
        t += state[x-2:x]
        x -= 2
    t = t.translate(swap)
    t += state[2*flip:]
    return t

def heuristics(state):
    if not state[6]=="4":
        return 4 
    elif not state[4]=="3":
        return 3
    elif not state[2]=="2":
        return 2
    else:
        return 0
    

def tiebreaker(state:str):
    state = state.replace("w","1").replace("b","0")
    return int(state)    

def generate_paths(state):
    states=[]
    for flip in range(1,5):
        val = {
            "state": flip_state(state["state"],flip),
            "parent":state["state"],
            "flip":flip,
            "g":state["g"]+flip,
        }
        val["h"]=heuristics(val["state"])
        val["t"]=tiebreaker(val["state"])
        val["f"]=val["h"]+val["g"]
        states.append(val)
    return states    

def generate_BFS_paths(state):
    states=[]
    for flip in range(1,5):
        val = {
            "state": flip_state(state["state"],flip),
            "parent":state["state"],
            "flip":flip,
        }
        states.append(val)
    return states    

def print_BFS(state,all_states):
    states = []
    states.insert(0,state)
    while states[0]["parent"] is not None:
        parent = next((state for state in all_states if state["state"] == states[0]["parent"]), None)
        parent["state"] = parent["state"][:2*states[0]["flip"]] + "|" + parent["state"][2*states[0]["flip"]:]
        states.insert(0, parent)
    for i in states:
        print(i["state"])
    return

def A_star(start:str):
    explored=[]
    states=[]
    queue=[]
    state={
        "state":start,
        "parent":None,
        "flip":0,
        "g":0,
        "h":0,
        "f":0,
        "t":tiebreaker(start)
    }

    
    queue.append(state)
    states.append(state)
    while len(queue)>0:
        current_state=queue[0]
        explored.append(current_state["state"])
        if current_state["state"]==goal_state:
            printA_star(current_state,states)
            return
        paths = generate_paths(current_state)
        for path in paths:
            if path["state"] not in explored:
                queue.append(path)
                states.append(path)
        
        queue = queue[1:]
        queue = sorted(queue, key=lambda x: (x["f"],x["t"]))
    print("No Solution")
    return

def BFS(start:str):
    explored=[]
    states=[]
    queue=[]
    state={
        "state":start,
        "parent":None,
        "flip":0
    }
    queue.append(state)
    states.append(state)
    while len(queue)>0:
        current_state=queue[0]
        explored.append(current_state["state"])
        if current_state["state"]==goal_state:
            print_BFS(current_state,states)
            return
        paths=generate_BFS_paths(current_state)
        for path in paths:
            if path["state"] not in explored:
                queue.append(path)
                states.append(path)
        queue = queue[1:]
    print("No Solution")
    return      

def main():
    Input_order = input("Enter the order: ")
    state, method = Input_order.split('-')
    
    if method == "b":
        BFS(state)
    elif method == "a":
        A_star(state)
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()