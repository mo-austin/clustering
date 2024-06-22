# Clustering
This repository contains a greedy algorithm for clustering items based on their pairwise distances. The goal is to form clusters that maximize the spacing between clusters. The spacing of a clustering is defined as the minimum distance between any pair of points lying in different clusters. The algorithm seeks to maximize this spacing to ensure the best separation between clusters.

## Installation and Use
1. Cloning the repository:
   ```sh
   git clone https://github.com/mo-austin/clustering.git
   cd clustering
2. Run main script:
   '''sh
   python main.py


## Problem Description
The algorithm processes an input file containing:

1. The number of clusters k
2. The number of items n
3. An n x n adjacency matrix representing the pairwise distances between items
   
The algorithm constructs a clustering that maximizes the spacing value, which is the smallest distance between any two clusters.

## Solution
Greedy algo using MST
1. Using Kruskal's algorithm, construct an MST from the adjacency matrix.
2. Form k clusters by removing the k - 1 most significant edges from the MST.
3. Determine the maximum spacing, which is the smallest edge weight connecting any two clusters after forming k clusters.
