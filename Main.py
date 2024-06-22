
import time
from Clustering import Clustering

# Read the input
fp = open("input.txt", 'r')
lines = fp.readlines()

# Parse the input
k = int(lines[0])
n = int(lines[1])
distances = [[0 for i in range(n)] for j in range(n)]

for i in range(0, n):
    row = lines[i+2].split(" ")
    for j in range(0, n):
        distances[i][j] = float(row[j])

# Call the compute function passing in the
# contents of the file
start = time.time()
c = Clustering()
print(c.compute(k, distances))
end = time.time()
print("time: "+ str(end-start))
