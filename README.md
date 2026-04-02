**Parallel Multi-Layer Social Network Analyzer**
This project is a Hybrid Parallel High-Performance Computing (HPC) framework built in Python to analyze large-scale, multi-layer social networks. As networks scale to millions of nodes, traditional serial processing fails ; this system overcomes those bottlenecks by combining distributed data handling with thread-level optimization.

**Key Features**

**Hybrid Parallelism:** Combines MPI-like inter-process communication (via mpi4py) for distributed data and OpenMP-like intra-process threading (via Numba) for numerical loops.
**True Task Parallelism:** Uses Dask to execute algorithmically distinct tasks—like PageRank and Community Detection—concurrently on separate cores.
**Multi-Layer Analytics:** Supports complex structures where entities are mapped across distinct geographic or interaction layers, specifically utilizing Kaktovi, Venetie, and Wainwright network datasets.
**High-Performance Metrics:** Optimized implementations of PageRank, Centrality measures, and Clustering (Louvain/Label Propagation).
**Benchmarking:** Built-in tools to measure Speedup, Efficiency, and Scalability (Strong and Weak scaling).

**Tech Stack**

Core: Python 3.x, NumPy, Pandas 
Graph Engine: NetworkX 
Parallelization: mpi4py, Numba (JIT Compiler), Dask 
Visualization: Matplotlib

