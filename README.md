**Parallel Multi-Layer Social Network Analyzer**

The core motivation of this project is to provide a scalable, high-performance solution for large-scale network analysis. By moving beyond simple serial computation—which often leads to resource inefficiency—this system implements a sophisticated Hybrid Parallel High-Performance Computing (HPC) framework to analyze millions of nodes and edges efficiently.

**Technologies & Frameworks(The HPC Stack)**

To overcome the Python Global Interpreter Lock (GIL) and meet HPC standards, the following specialized tools are integrated:

**Python 3.x:** Selected for its rapid development cycle and extensive graph theory ecosystem.

**mpi4py (Inter-process Parallelism):** Provides the Message Passing Interface (MPI) to partition graphs across distributed processes.Numba (Intra-process Parallelism): A Just-In-Time (JIT) compiler used for shared-memory multithreading (similar to OpenMP) to accelerate heavy numerical loops.

**Dask (Task Scheduling):** A flexible library that coordinates True Task Parallelism by managing a Directed Acyclic Graph (DAG) of distinct algorithms.

**NetworkX:** Used for graph construction and as a baseline for serial algorithm comparison.

**NumPy & Pandas:** Utilized for high-performance numerical computations and structured result logging.

**Main Functionalities**

**1. Graph Construction & Data Management**

**Network Generation:** Creates synthetic topologies using Barabási-Albert, Erdos-Renyi, and Watts-Strogatz models.

**Dataset Integration:** Supports large-scale edge-lists from real-world sources like SNAP and Kaggle.

**Layered Architecture:** Maps nodes across unified interaction layers, specifically Friendship, Follower, and Message layers.

**2. Advanced Graph Metrics**

**Influence Ranking:** Implements a custom iterative PageRank optimized for parallel matrix operations.

**Structural Metrics:** Computes Degree, Betweenness, and Eigenvector centrality measures.

**Clustering:** Executes community detection via Label Propagation or the Louvain method.

**3. Hybrid Parallel Execution**

**Hybrid Data Parallelism:** Combines MPI-based process distribution with Numba-based multithreading for local computations.

**True Task Parallelism:** Utilizes a concurrent pipeline to execute algorithmically diverse tasks (e.g., Ranking vs. Clustering) on separate cores simultaneously.

**4. Performance & Scalability Analysis**

**Benchmarking:** Automatically records and compares execution times for Serial vs. Parallel runs.

**HPC Metrics:** Calculates critical performance indicators including Speedup, Efficiency, and Resource Utilization.

**Scalability Testing:** Conducts both Strong Scaling and Weak Scaling to validate hardware utilization.


**Expected Outcomes**

**Significant Speedup:** A measurable reduction in total execution time compared to serial processing.

**Optimal Scalability:** Improved performance as CPU cores increase from 1 to 8.

**Algorithmic Concurrency:** Successful simultaneous execution of PageRank, Community Detection, and Structural Analysis.

**Analytical Visualization:** Generating Speedup graphs, Scalability plots, and network maps of influential users.


**Performance Goals**


The system is designed to provide significant speedup as CPU cores increase from 1 to 12, ensuring optimal hardware utilization for big data workloads.

