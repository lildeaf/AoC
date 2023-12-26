import time
import random


def update_egde(g, old_comp, other, new_comp):
    connections = g["connections"].get(other)
    connections.remove(old_comp)
    connections.append(new_comp)
    g["edges"].append((new_comp, other))


def remove_edge(g, edge):
    comp1, comp2 = edge
    vertices = g["vertices"]
    vertices.remove(comp1)
    vertices.remove(comp2)
    vertices.add(edge)

    connections1 = g["connections"].pop(comp1, [])
    connections2 = g["connections"].pop(comp2, [])

    connections1.extend(connections2)
    while comp1 in connections1:
        connections1.remove(comp1)
    while comp2 in connections1:
        connections1.remove(comp2)

    edges = g["edges"]
    i = 0
    while i < len(edges):
        e = edges[i]
        if comp1 in e and comp2 in e:
            edges.remove(e)
            continue
        if comp1 in e:
            c1, c2 = e
            if c1 == comp1:
                update_egde(g, c1, c2, edge)
            else:
                update_egde(g, c2, c1, edge)
            edges.remove(e)
            continue
        if comp2 in e:
            c1, c2 = e
            if c1 == comp2:
                update_egde(g, c1, c2, edge)
            else:
                update_egde(g, c2, c1, edge)
            edges.remove(e)
            continue
        i += 1

    g["connections"][edge] = connections1


def karger(g):
    edges = g["edges"].copy()
    component_set = g["vertices"].copy()
    connections = {k: v.copy() for k, v in g["connections"].items()}
    graph = {"connections": connections,
             "edges": edges,
             "vertices": component_set}

    while len(component_set) > 2:
        rand_edge = edges.pop(random.randint(0, len(edges) - 1))
        remove_edge(graph, rand_edge)

    return connections.keys(), len(edges)


def count(sub):
    if len(sub) == 1:
        return 1

    return count(sub[0]) + count(sub[1])


def task():
    input_file = open('input.txt' if not testing else 'example.txt', 'r')
    lines = input_file.readlines()

    connections = {}
    component_set = set()
    edges = []

    graph = {"connections": connections,
             "edges": edges,
             "vertices": component_set}

    for line in lines:
        component, comp_edges = line.strip().split(': ')
        comp_edges = [(c,) for c in comp_edges.split(' ')]
        component = (component,)
        comp_connection = connections.get(component, [])

        for connection in comp_edges:
            if component not in (con_con := connections.get(connection, [])):
                con_con.append(component)
                connections[connection] = con_con
            if connection not in comp_connection:
                comp_connection.append(connection)
            if not (connection, component) in edges:
                edges.append((component, connection))

        connections[component] = comp_connection

    component_set.update(list(connections.keys()))

    sub_graphs, num_edges = None, 0
    while num_edges != 3:
        sub_graphs, num_edges = karger(graph)

    lens = []
    for sub in sub_graphs:
        lens.append(count(sub))
    print("Stage 1:", lens[0] * lens[1])


if __name__ == '__main__':
    testing = True
    stage = 1
    start = time.time()
    task()
    print(time.time() - start)
