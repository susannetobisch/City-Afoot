import osmnx as ox

from shapely.geometry import LineString
from shapely.geometry import Point


def redistribute_graph(G, length=25):
    G = G.copy()
    rem_edges = []
    add_edges = []
    add_nodes = []

    for orig_edge in G.edges(data=True):
        orig_attrs = orig_edge[2]
        geometry = LineString(
                [Point(G.nodes[node]["x"], G.nodes[node]["y"]) for node in orig_edge[:2]]
            )
        points = ox.utils_geo.redistribute_vertices(geometry, length)
        if len(points) != 2:
            rem_edges.append((orig_edge[0], orig_edge[1]))

            f = points.pop(0)
            start_s = orig_edge[0]
            start = G.nodes[start_s]

            i = 0
            for end in points[:-1]:
                end_s = '_'.join([str(e) for e in [orig_edge]]) + '_' + str(i)
                end = {'y': end.y, 'x': end.x}

                add_nodes.append((end_s, end))
                attrs = orig_attrs.copy()

                attrs['length'] = LineString([Point(start["x"], start["y"]), Point(end["x"], end["y"])]).length

                add_edges.append((start_s, end_s, attrs))

                start = end
                start_s = end_s

                i += 1
            
            attrs = orig_attrs.copy()
            end_s = orig_edge[1]
            end = G.nodes[end_s]
            attrs['length'] = LineString([Point(start["x"], start["y"]), Point(end["x"], end["y"])]).length
            add_edges.append((start_s, end_s, attrs))

    for node, node_attr in add_nodes:
        G.add_node(node, **node_attr)

    for edge in rem_edges:
        G.remove_edge(*edge)

    for u, v, attr in add_edges:
        G.add_edge(u, v, **attr)
    
    return G
    