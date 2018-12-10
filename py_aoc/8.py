from util import parse_file

class node:
    def __init__(self, num_children, num_meta_ent):
        self.num_children = num_children
        self.num_meta_ent = num_meta_ent
        self.child_nodes = []
        self.metadata = []
    def add_child_node(self, child_node):
        self.child_nodes.append(child_node)
    def add_metadata(self, metadata):
        self.metadata.append(metadata)

def get_nodes(seq, i):
    nodes = []
    num_children = seq[i]
    num_meta_ent = seq[i+1]
    i += 2
    thisnode = node(num_children, num_meta_ent)
    for j in range(num_children):
        (i, child_nodes) = get_nodes(seq, i)
        for cn in child_nodes:
            thisnode.add_child_node(cn)
    for k in range(num_meta_ent):
        thisnode.add_metadata(seq[i + k])
    nodes.append(thisnode)
    return(i + num_meta_ent, nodes)


def total_metadata(nodes):
    tally = 0
    for n in nodes:
        tally += sum(n.metadata)
        tally += total_metadata(n.child_nodes)
    return tally

def node_value(node):
    if node.num_children == 0:
        return sum(node.metadata)
    else:
        t = 0
        for i in node.metadata:
            try:
                t += node_value(node.child_nodes[i - 1])
            except:
                pass
        return t

def parsefunc(s):
    return s.strip()

def part1(seq):
    n = get_nodes(seq, 0)[1]
    return total_metadata(n)

def part2(seq):
    n = get_nodes(seq, 0)[1][0]
    return node_value(n)

seq = [int(c) for c in parse_file("../data/input_8", parsefunc)[0].split()]

print("P1: ", part1(seq))
print("P2: ", part2(seq))
