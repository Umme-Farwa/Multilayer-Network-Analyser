import networkx as nx
import os
import time

# Rasta set karein
input_dir = r"D:\Projects\HPC 01\data\processed\AMZ\Multilayer_Data"

def analyze_layer_structural(file_path, layer_id):
    """Layer ki structural properties calculate karna"""
    # 1. Graph Load Karna
    G = nx.read_edgelist(file_path, nodetype=int)
    
    # 2. PageRank (Importance)
    pagerank = nx.pagerank(G, alpha=0.85)
    
    # 3. Clustering Coefficient (Local Density)
    clustering = nx.average_clustering(G)
    
    # 4. Degree Centrality (Popularity)
    degree_cent = nx.degree_centrality(G)
    
    # Result print karein
    avg_pagerank = sum(pagerank.values()) / len(pagerank)
    print(f"--- Layer {layer_id} Mukammal ---")
    print(f"Nodes: {G.number_of_nodes()}, Edges: {G.number_of_edges()}")
    print(f"Avg Clustering: {clustering:.4f}")
    print(f"Avg PageRank: {avg_pagerank:.6f}\n")

if __name__ == "__main__":
    print("Project Proposal ke mutabiq Serial Structural Analysis shuru...\n")
    start_time = time.time()

    for i in range(10):
        file_name = f"layer_{i}.txt"
        file_path = os.path.join(input_dir, file_name)
        
        if os.path.exists(file_path):
            analyze_layer_structural(file_path, i)
        else:
            print(f"Layer {i} ki file nahi mili!")

    end_time = time.time()
    total_time = end_time - start_time
    print(f"==========================================")
    print(f"SERIAL ANALYSIS TOTAL TIME: {total_time:.4f} seconds")
    print(f"==========================================")