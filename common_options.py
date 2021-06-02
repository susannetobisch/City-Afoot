## Color palettes

col_green = '#558a20'
col_greens_2 = ['#a0c975','#558a20']
col_greens_5 = ['#bad99c', '#a0c975','#77a845', '#558a20', '#315909']

col_darkgray = '#424242'
col_lightgray = '#808080'
col_orange = '#d9832b'
col_yellow = '#ebc567'

## Network filters

walking_filter = (
    '["highway"]'
    '["area"!~"yes"]'
    '["highway"!~"motor|proposed|construction|abandoned|platform|raceway"]'
    '["foot"!~"no"]'
    '["service"!~"private"]'
    '["access"!~"private"]'
    '["indoor"!~"yes"]'
)

# specific filter for Westbahnhof area to filter out tunnels 
walking_filter_wbh = (
    walking_filter + 
    '["tunnel"!~"building_passage"]'
)

# for network analysis 
walking_filter_network = (
    '["highway"]'
    '["area"!~"yes"]'
    '["highway"!~"motor|proposed|construction|abandoned|platform|raceway|steps|service"]'
    '["foot"!~"no"]'
    '["service"!~"private"]'
    '["access"!~"private|permissive"]'
    '["indoor"!~"yes"]'
    '["footway"!~"sidewalk"]'
)

walking_filter_network_simplified = (
    '["highway"]'
    '["area"!~"yes"]'
    '["highway"!~"motor|proposed|construction|abandoned|platform|raceway|cycleway|steps|footway|service"]'
    '["foot"!~"no"]'
    '["service"!~"private"]'
    '["access"!~"private|permissive"]'
    '["indoor"!~"yes"]'
    '["footway"!~"sidewalk"]'
)

graph_download_options = {
    'network_type': 'walk',
}

## Plotting options

graph_plot_options = {
    'edge_color': col_lightgray,
    'edge_alpha': 0.2,
    'node_size': 0,
    'bgcolor': 'white',
}

graph_plot_nodes_options = {
    'edge_color': col_lightgray,
    'edge_alpha': 0.2,
    'node_size': 6,
    'node_color': col_orange,
    'bgcolor': 'white',
}

## Areas / Bounding boxes

bb_westbahnhofareal = 48.2043, 48.1817, 16.3490, 16.3029

