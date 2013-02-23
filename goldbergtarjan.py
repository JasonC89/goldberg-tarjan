class Sparse(object):
    def __init__(self, dic):
        self._dict = dic

    def __getitem__(self, item):
        if item in self._dict:
            return self._dict[item]
        else:
            return 0

    def __setitem__(self, item, val):
        self._dict[item] = val

    def __iter__(self):
        return self._dict.iterkeys()


def max_flow(c, start, end):
    """Calculate a max flow on a given graph
    param c: The capacity on each edge. This parameter also implies all edges
    param start: The start node, this has to be a node with only
    incoming edges.
    param end: The end node, this has to be a node with only outgoing
    edges."""
    nodes = {}
    f = Sparse({})  # current flow on the graph, keys will be tuples with nodes
    c = Sparse(c)

    for fro, to in c:
        if not fro in nodes:
            nodes[fro] = {'dist': 0, 'overflow': 0}
        if not to in nodes:
            nodes[to] = {'dist': 0, 'overflow': 0}

        nodes[fro].setdefault('neighbors', [])
        nodes[to].setdefault('neighbors', [])
        nodes[fro]['neighbors'].append(to)
        nodes[to]['neighbors'].append(fro)

    if not start in nodes or not end in nodes:
        print("Start or end node does not exist")
        return False

    active_nodes = set([])

    # Init phase
    nodes[start]['dist'] = len(nodes)

    for node in nodes[start]['neighbors']:
        f[(start, node)] = c[(start, node)]
        f[(node, start)] = -c[(start, node)]
        nodes[node]['overflow'] = c[(start, node)]

        active_nodes.add(node)

    while len(active_nodes) > 0:
        node = active_nodes.pop()

        if not can_push(node, nodes, f, c):
            nodes = relabel(node, nodes, f, c)

        nodes, f, c = push(node, nodes, f, c)

        # Check if either this node or any of his neighbors is active now
        if node != start and node != end and nodes[node]['overflow'] > 0:
            active_nodes.add(node)
        for neighbor in nodes[node]['neighbors']:
            if neighbor != start and neighbor != end and \
                    nodes[neighbor]['overflow'] > 0:
                active_nodes.add(neighbor)
        print(active_nodes)

    # Calculate the amount of flow
    sum = 0
    for neighbor in nodes[start]['neighbors']:
        sum += f[(start, neighbor)]
        sum -= f[(neighbor, start)]

    sum = sum / 2  # take the half because we also counted all backward edges

    return sum, f


def can_push(node, nodes, f, c):
    """To be able to push we need capacity on the edge and the height
    of the neighbor must be exactly one smaller than current node is"""
    for neighbor in nodes[node]['neighbors']:
        if nodes[neighbor]['dist'] + 1 == nodes[node]['dist'] and \
                c[(node, neighbor)] - f[(node, neighbor)] > 0:
            return True

    return False


def relabel(node, nodes, f, c):
    print()
    print("Relabeling %s" % node)
    nodes[node]['dist'] = 1 + \
        min([nodes[neighbor]['dist']
             for neighbor in nodes[node]['neighbors']
             if c[(node, neighbor)] - f[(node, neighbor)] > 0])

    return nodes


def push(node, nodes, f, c):
    print()
    print("Pushing on node %s (dist: %s)" % (node, nodes[node]['dist']))
    for neighbor in nodes[node]['neighbors']:
        print("neighbor %s (dist: %s)" % (neighbor, nodes[neighbor]['dist']))
        if nodes[neighbor]['dist'] + 1 == nodes[node]['dist']:
            print("pushing from %d to %d" % (node, neighbor))

            empty_capacity = c[(node, neighbor)] - f[(node, neighbor)]
            push_amount = min((empty_capacity, nodes[node]['overflow']))

            print("current overflow %d" % nodes[node]['overflow'])
            print("Amount %d" % push_amount)

            nodes[neighbor]['overflow'] += push_amount
            nodes[node]['overflow'] -= push_amount
            f[(node, neighbor)] += push_amount
            f[(neighbor, node)] -= push_amount

            print("new overflow %d" % nodes[node]['overflow'])

    return nodes, f, c
