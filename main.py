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
        ('A', 'B', 4), ('A', 'C', 3), ('B', 'D', 5),
        ('C', 'D', 1), ('C', 'E', 6), ('D', 'E', 2),
        ('E', 'F', 7), ('D', 'F', 3)
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

# Visualize using NetworkX 
def visualize_graph(graph, notified_nodes, source, radius):
    # Use spring layout with added parameters for better spacing
    pos = nx.spring_layout(graph, k=0.5, seed=42)  # The 'k' parameter controls node distance
    
    # Define color schemes
    node_color_map = []
    for node in graph.nodes():
        if node == source:
            node_color_map.append('#FF6347')  # Red for the source (crime location)
        elif node in notified_nodes:
            node_color_map.append('#FFD700')  # Golden for notified nodes
        else:
            node_color_map.append('#1E90FF')  # Blue for other nodes

    # Edge colors: Highlight edges that connect notified nodes
    edge_color_map = []
    for u, v in graph.edges():
        if (u in notified_nodes and v in notified_nodes):
            edge_color_map.append('#FF4500')  # Orange-red for highlighted edges
        else:
            edge_color_map.append('#A9A9A9')  # Grey for normal edges

    # Set node size based on degree or other metrics (can be adjusted)
    node_sizes = [2500 for node in graph.nodes()]
    
    # Adjust font size and color for better readability
    font_size = 12
    font_color = 'black'
    font_weight = 'bold'
    
    # Set up the plot with a more attractive background
    plt.figure(figsize=(10, 8), facecolor='#f0f0f0')

    # Draw the graph with the improved color palette and styling
    nx.draw(
        graph, pos, with_labels=True,
        node_size=node_sizes,
        node_color=node_color_map,
        edge_color=edge_color_map,
        font_size=font_size, font_color=font_color, font_weight=font_weight,
        width=2, alpha=0.8, font_family='sans-serif',
        edgecolors='black', linewidths=1.5  # Node border color and thickness
    )
    
    # Title for better context and positioning
    plt.title(f"Crime Notification System: Source = {source}, Radius = {radius} miles", fontsize=14, fontweight='bold', color='#333333', pad=20)
    
    # Remove grid and axes for a cleaner look
    plt.grid(False)  # Hide gridlines
    plt.axis('off')  # Hide axis ticks and labels
    
    # Show the plot
    plt.show()

# Tkinter UI
class CrimeGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crime Neighborhood Alert System")
        
        # Create the graph and get the list of nodes
        self.graph = create_graph()
        self.nodes = list(self.graph.nodes())
        
        # Add dropdown for source node
        self.source_label = tk.Label(self.root, text="Select Source Node (Crime Location):")
        self.source_label.pack(pady=10)
        
        self.source_var = tk.StringVar(value=self.nodes[0])  # Default value to the first node in the graph
        self.source_dropdown = ttk.Combobox(self.root, textvariable=self.source_var, values=self.nodes)
        self.source_dropdown.pack(pady=10)
        
        # Add input for radius
        self.radius_label = tk.Label(self.root, text="Enter Notification Radius (in miles):")
        self.radius_label.pack(pady=10)
        
        self.radius_entry = tk.Entry(self.root)
        self.radius_entry.insert(0, "4.0")  # Default value
        self.radius_entry.pack(pady=10)
        
        # Add button to visualize
        self.visualize_button = tk.Button(self.root, text="Visualize", command=self.visualize_graph)
        self.visualize_button.pack(pady=20)
    
    def visualize_graph(self):
        # Get source node and radius from the UI
        source_node = self.source_var.get()
        try:
            radius = float(self.radius_entry.get())
        except ValueError:
            print("Invalid radius input. Using default value of 4.0")
            radius = 4.0
        
        # Find notified nodes
        notified_nodes = dijkstra_notify(self.graph, source_node, radius).keys()
        
        # Visualize the graph
        visualize_graph(self.graph, notified_nodes, source_node, radius)

# Run the Tkinter Application
if __name__ == "__main__":
    root = tk.Tk()
    app = CrimeGraphApp(root)
    root.mainloop()
