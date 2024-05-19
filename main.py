from friends import graph
from data import data
import heapq
from utils import similarity_score
import networkx as nx

class UnionFind:
    def __init__(self, n : int) -> None:
        self.parent = [i for i in range(n + 1)]
        self.size = [0] * (n + 1)
        self.count : int  = n
    
    def find(self, x : int) -> int:
        if(self.parent[x] != x):
            self.parent[x] =  self.find(self.parent[x])
        return self.parent[x]

    def union(self, x : int, y : int) -> bool :
        parx = self.find(x)
        pary = self.find(y)
        if(parx == pary):
            return False
        if(self.size[parx] < self.size[pary]):
            self.parent[parx] = pary
            self.size[pary] += self.size[parx]
        else :
            self.parent[pary] = parx
            self.size[parx] += self.size[pary]
        self.count -= 1
        return True



def get_friends(user):
    return graph[str(user)]

# Function to recommend friends using collaborative filtering and BFS
def recommend_friends(user):
    friends = get_friends(user)
    queue = []
    visited = set()
    for friend in friends:
        queue.append(friend)
        visited.add(friend)
    while queue:
        current = queue.pop(0)
        current_friends = get_friends(current)
        for friend in current_friends:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
    return visited - set(friends) - {user}


# Function to recommend friends using common interests and BFS
def recommend_friends_interests(user):
    interests = data[user]['hobbies']
    friends = get_friends(user)
    queue = []
    visited = set()
    for friends in friends:
        queue.append(friends)
        visited.add(friends)
    
    while queue:
        current = queue.pop(0)
        current_friends = get_friends(current)
        for friend in current_friends:
            if friend not in visited:
                visited.add(friend)
                friend_interest = data[friend]['hobbies']
                if len(set(interests).intersection(set(friend_interest))) > 0:
                    queue.append(friend)
    return visited - {user}


# Function to calculate the degree of centrality of a user
def centrality(user):
    friends = get_friends(user)
    queue = []
    visited = set()
    for friend in friends:
        queue.append(friend)
        visited.add(friend)
    while queue:
        current = queue.pop(0)
        current_friends = get_friends(current)
        for friend in current_friends:
            if friend not in visited:
                visited.add(friend)
                queue.append(friend)
    return len(visited)


# Function to create cluster of user having similar interests indicating a community
def create_cluster():
    clusters = []
    visited = set()
    for user in data:
        if user not in visited:
            interests = data[user]['hobbies']
            queue = []
            cluster = []
            queue.append(user)
            visited.add(user)
            while queue:
                current = queue.pop(0)
                cluster.append(current)
                current_friends = get_friends(current)
                for friend in current_friends:
                    if friend not in visited:
                        visited.add(friend)
                        friend_interest = data[friend]['hobbies']
                        if len(set(interests).intersection(set(friend_interest))) > 0:
                            queue.append(friend)
            clusters.append(cluster)
    return clusters

# Create communities based on friends cycle
def identify_cycle():
    uf = UnionFind(len(graph)) 
    for user in graph:
        for friend in graph[user]:
            uf.union(int(user), friend)

    map = {}

    for i in range(len(uf.parent)):
        if uf.parent[i] not in map:
            map[uf.parent[i]] = []
        map[uf.parent[i]].append(i)

    return map


    
    

# Identify shortest path between two users 
def calculate_min_path(user1, user2):
    distances = [float('inf') for i in range(len(graph) + 1)]
    distances[user1] = 0

    priority_queue = [(0, user1, [user1])]

    while priority_queue:
        current_distance, current_node, path = heapq.heappop(priority_queue)

        if current_node == user2:
            return path, current_distance
        
        if current_distance > distances[current_node]:
            continue
        for index, neighbour in enumerate(get_friends(current_node)):
            distance = current_distance + similarity_score[current_node - 1][index] 

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(priority_queue, (distance, neighbour, path + [neighbour]))


    return None, float('inf')

# Identify all the different paths that are available between two users
def identify_paths(user2, ans, visited, paths, current_user):
    print(1)
    if(current_user == user2):
        paths.append(ans[:])
        return
    friends = get_friends(current_user)
    for friend in friends:
        if friend not in visited and friend not in ans:
            visited.add(friend)
            identify_paths(user2, ans + [friend], visited.copy(), paths, friend)



id = int(input("Enter the user id::"))
print("Friends of the user are::", get_friends(id))
print("Friends recommended using collaborative filtering are::", recommend_friends(id))
print("Friends recommended using common interests are::", recommend_friends_interests(id))
print("Degree of centrality of user is::", centrality(id))
print("Cluster of users having similar interests are::", create_cluster())

for i in range(1, 81):
    if(i == id):
        continue
    path, distance = calculate_min_path(id, i)
    print(f"Shortest path between {id} and {i} is {path} ")

print("Finding out all paths between two users")


# for i in range(1, 81):
#     if(i == id):
#         continue
#     visited = set([id])
#     ans = [id]
#     paths = []
#     identify_paths(i, ans, visited, paths, id)
#     print(f"Paths between {id} and {i} are {paths}")


print("Identifying cycles in the graph")
print(identify_cycle())


