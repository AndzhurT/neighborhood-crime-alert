import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Create the graph representing neighborhoods and distances (in miles)
def create_graph():
    G = nx.Graph()
    # Adding nodes (neighborhoods) and edges (distances in miles)
    G.add_weighted_edges_from([
        ('Downtown', 'Uptown', 3.0), 
        ('Downtown', 'Brooklyn', 5.0), 
        ('Uptown', 'Queens', 4.0),
        ('Uptown', 'Soho', 2.0), 
        ('Brooklyn', 'Queens', 3.5), 
        ('Soho', 'Chelsea', 1.5),
        ('Chelsea', 'Times Square', 2.0),
        ('Times Square', 'Midtown', 1.2),
        ('Midtown', 'Central Park', 1.8),
        ('Central Park', 'Harlem', 3.0),
        ('Harlem', 'Bronx', 4.5),
        ('Bronx', 'Brooklyn', 7.0),
        ('Downtown', 'Battery Park', 1.0),
        ('Battery Park', 'Financial District', 0.5),
        ('Financial District', 'Chinatown', 1.0)
    ])
    return G

# Dijkstra's algorithm
def dijkstra_notify(graph, start_node, radius):
    # Min-heap to store the nodes and their distances
    priority_queue = [(0, start_node)]
    visited = {}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        visited[current_node] = current_distance
        
        for neighbor, attributes in graph[current_node].items():
            distance = attributes['weight']
            new_distance = current_distance + distance
            if neighbor not in visited and new_distance <= radius:
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return visited
