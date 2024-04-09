import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
graph = {
    "1": [2, 3, 4, 7, 9, 12, 18, 22],
    "2": [1, 3, 4, 5, 6, 7, 10],
    "3": [1, 2, 4, 5, 6, 7, 8, 10],
    "4": [1, 2, 3, 5, 8, 11, 13, 14],
    "5": [2, 3, 4, 6, 7, 8],
    "6": [2, 3, 5, 7, 8],
    "7": [1, 2, 3, 5, 6, 8],
    "8": [3, 4, 5, 7, 9],
    "9": [1, 2, 4, 8],
    "10": [2, 3, 7, 11],
    "11": [4, 10, 12],
    "12": [1, 11, 13],
    "13": [4, 12],
    "14": [4, 15, 16],
    "15": [14, 16],
    "16": [14, 15],
    "17": [18, 19, 20, 21],
    "18": [1, 17, 22],
    "19": [17, 20, 21],
    "20": [17, 19, 21, 22],
    "21": [17, 19, 20, 22],
    "22": [1, 18, 20, 21, 23],
    "23": [22, 24],
    "24": [23, 25],
    "25": [24, 26, 28, 29],
    "26": [25, 27, 29, 32],
    "27": [26, 28, 32, 33],
    "28": [25, 27, 29, 32],
    "29": [25, 26, 28, 31, 32],
    "30": [31, 32, 33],
    "31": [29, 30, 32, 34],
    "32": [26, 27, 28, 29, 30, 31, 33],
    "33": [27, 30, 32, 34],
    "34": [31, 33],
    "35": [36, 37, 38, 39, 40],
    "36": [35, 37, 38, 39, 40, 41],
    "37": [35, 36, 38, 39, 40, 41],
    "38": [35, 36, 37, 39, 40, 41],
    "39": [35, 36, 37, 38, 40, 41],
    "40": [35, 36, 37, 38, 39, 41],
    "41": [35, 36, 37, 38, 39, 40],
    "42": [43, 44, 45, 46, 47],
    "43": [42, 44, 45, 46, 47],
    "44": [42, 43, 45, 46, 47],
    "45": [42, 43, 44, 46, 47],
    "46": [42, 43, 44, 45, 47],
    "47": [42, 43, 44, 45, 46],
    "48": [49, 50, 51, 52, 53],
    "49": [48, 50, 51, 52, 53],
    "50": [48, 49, 51, 52, 53],
    "51": [48, 49, 50, 52, 53],
    "52": [48, 49, 50, 51, 53],
    "53": [48, 49, 50, 51, 52],
    "54": [55, 56, 57, 58, 59],
    "55": [54, 56, 57, 58, 59],
    "56": [54, 55, 57, 58, 59],
    "57": [54, 55, 56, 58, 59],
    "58": [54, 55, 56, 57, 59],
    "59": [54, 55, 56, 57, 58],
    "60": [61, 62, 63, 64, 65],
    "61": [60, 62, 63, 64, 65],
    "62": [60, 61, 63, 64, 65],
    "63": [60, 61, 62, 64, 65],
    "64": [60, 61, 62, 63, 65],
    "65": [60, 61, 62, 63, 64],
    "66": [67, 68, 69, 70, 71],
    "67": [66, 68, 69, 70, 71],
    "68": [66, 67, 69, 70, 71],
    "69": [66, 67, 68, 70, 71],
    "70": [66, 67, 68, 69, 71],
    "71": [66, 67, 68, 69, 70],
    "72": [73, 74, 75, 76, 77],
    "73": [72, 74, 75, 76, 77],
    "74": [72, 73, 75, 76, 77],
    "75": [72, 73, 74, 76, 77],
    "76": [72, 73, 74, 75, 77],
    "77": [72, 73, 74, 75, 76],
    "78": [79, 80],
    "79": [78, 80],
    "80": [78, 79]
}


# G = nx.Graph(graph)

# # Create 3D positions for each node
# pos = {node: (np.random.rand(), np.random.rand(), np.random.rand()) for node in G.nodes()}

# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Add nodes and edges to the plot
# for node, (x, y, z) in pos.items():
#     ax.scatter(x, y, z)
# for edge in G.edges():
#     x = np.array((pos[edge[0]][0], pos[edge[1]][0]))
#     y = np.array((pos[edge[0]][1], pos[edge[1]][1]))
#     z = np.array((pos[edge[0]][2], pos[edge[1]][2]))
#     ax.plot(x, y, z, color='blue')

# # Display the plot
# plt.show()