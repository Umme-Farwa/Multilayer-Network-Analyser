import networkx as nx
import os

# Defining path
input_file = r"D:\Projects\HPC 01\data\processed\AMZ\com-amazon.ungraph.txt.gz"
output_dir = r"D:\Projects\HPC 01\data\processed\AMZ\Multilayer_Data"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print("Loading original Amazon Graph...")
G_full = nx.read_edgelist(input_file, comments='#', nodetype=int)
all_nodes = list(G_full.nodes())
n_nodes = len(all_nodes)
num_layers = 10
nodes_per_layer = n_nodes // num_layers

# Dictionary to keep track of which node belongs to which layer
node_to_layer = {}

print(f"Creating {num_layers} layers...")

# 1. Nodes ko Layers assign karein
for i in range(num_layers):
    start_idx = i * nodes_per_layer
    end_idx = (i + 1) * nodes_per_layer if i != num_layers - 1 else n_nodes
    
    layer_nodes = all_nodes[start_idx:end_idx]
    for node in layer_nodes:
        node_to_layer[node] = i

# 2. Edges ko Intra-layer aur Inter-layer mein divide karein
layer_files = {i: open(os.path.join(output_dir, f"layer_{i}.txt"), 'w') for i in range(num_layers)}
inter_layer_file = open(os.path.join(output_dir, "inter_layer_edges.txt"), 'w')

print("Distributing edges into layers (Intra vs Inter)...")
for u, v in G_full.edges():
    layer_u = node_to_layer[u]
    layer_v = node_to_layer[v]
    
    if layer_u == layer_v:
        # Same layer edge (Intra-layer)
        layer_files[layer_u].write(f"{u} {v}\n")
    else:
        # Different layer edge (Inter-layer)
        inter_layer_file.write(f"{u} {v} {layer_u} {layer_v}\n")

# Files close karein
for f in layer_files.values():
    f.close()
    inter_layer_file.close()

print(f"SUCCESS! Data 10 layers mein divide ho gaya hai.")
print(f"Check folder: {output_dir}")