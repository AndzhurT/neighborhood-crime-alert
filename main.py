import customtkinter as ctk
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Create the graph representing neighborhoods and distances (in miles)
def create_graph():
    G = nx.Graph()
    # Adding nodes (neighborhoods) and edges (distances in miles)
    G.add_weighted_edges_from([
        ('Times Square', 'Central Park', 2.5),
        ('Times Square', 'Empire State Building', 1.0),
        ('Central Park', 'Columbus Circle', 0.8),
        ('Empire State Building', 'Flatiron District', 1.2),
        ('Flatiron District', 'Union Square', 0.7),
        ('Union Square', 'Greenwich Village', 1.0),
        ('Columbus Circle', 'Upper West Side', 2.0),
        ('Upper West Side', 'Central Park', 1.5),
        ('Police Station', 'Times Square', 2.8),
        ('Police Station', 'Flatiron District', 3.0)
    ])
    return G

# Dijkstra's algorithm for neighborhoods
def dijkstra_notify(graph, start_node, radius):
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

# Find the shortest path to the police station
def find_shortest_path_to_police(graph, source_node):
    shortest_path = nx.shortest_path(graph, source=source_node, target="Police Station", weight="weight")
    return shortest_path

# Visualize using NetworkX 
def visualize_graph(graph, notified_nodes, source, radius, police_path):
    pos = nx.spring_layout(graph, k=0.5, seed=42)
    
    # Define color schemes
    node_color_map = []
    for node in graph.nodes():
        if node == source:
            node_color_map.append('#FF6347')  # Red for the source (crime location)
        elif node == "Police Station":
            node_color_map.append('#32CD32')  # Green for the police station
        elif node in notified_nodes:
            node_color_map.append('#FFD700')  # Golden for notified nodes
        else:
            node_color_map.append('#1E90FF')  # Blue for other nodes

    # Edge colors
    edge_color_map = []
    for u, v in graph.edges():
        if (u in police_path and v in police_path):
            edge_color_map.append('#FF4500')  # Orange-red for shortest path to police
        elif (u in notified_nodes and v in notified_nodes):
            edge_color_map.append('#FFD700')  # Yellow for notified areas
        else:
            edge_color_map.append('#A9A9A9')  # Grey for normal edges

    node_sizes = [2500 for node in graph.nodes()]
    
    plt.figure(figsize=(10, 8), facecolor='#f0f0f0')
    nx.draw(
        graph, pos, with_labels=True,
        node_size=node_sizes,
        node_color=node_color_map,
        edge_color=edge_color_map,
        font_size=12, font_color='black', font_weight='bold',
        width=2, alpha=0.8, font_family='sans-serif',
        edgecolors='black', linewidths=1.5
    )
    
    plt.title(f"Crime Notification System: Source = {source}, Radius = {radius} miles", fontsize=14, fontweight='bold', color='#333333', pad=20)
    plt.grid(False)
    plt.axis('off')
    plt.show()

# customtkinter UI
class CrimeGraphApp:
    def __init__(self, root):
        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.root = root
        self.root.title("Crime Neighborhood Alert System")
        self.root.geometry("600x400")

        self.graph = create_graph()
        self.nodes = list(self.graph.nodes())

        # Main frame
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=10)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title label
        self.title_label = ctk.CTkLabel(self.main_frame, text="Crime Neighborhood Alert System", font=ctk.CTkFont(size=18, weight="bold"))
        self.title_label.pack(pady=10)

        # Dropdown for source node
        self.source_label = ctk.CTkLabel(self.main_frame, text="Select Source Node (Crime Location):", font=ctk.CTkFont(size=12))
        self.source_label.pack(pady=5)

        self.source_var = ctk.StringVar(value=self.nodes[0])
        self.source_dropdown = ctk.CTkOptionMenu(self.main_frame, variable=self.source_var, values=self.nodes)
        self.source_dropdown.pack(pady=5)

        # Input for radius
        self.radius_label = ctk.CTkLabel(self.main_frame, text="Enter Notification Radius (in miles):", font=ctk.CTkFont(size=12))
        self.radius_label.pack(pady=5)

        self.radius_entry = ctk.CTkEntry(self.main_frame, width=200)
        self.radius_entry.insert(0, "1.0")
        self.radius_entry.pack(pady=5)

        # Visualize button
        self.visualize_button = ctk.CTkButton(self.main_frame, text="Visualize Graph", command=self.visualize_graph)
        self.visualize_button.pack(pady=20)

    def visualize_graph(self):
        source_node = self.source_var.get()
        try:
            radius = float(self.radius_entry.get())
        except ValueError:
            print("Invalid radius input. Using default value of 1.0")
            radius = 1.0
        
        notified_nodes = dijkstra_notify(self.graph, source_node, radius).keys()
        police_path = find_shortest_path_to_police(self.graph, source_node)
        
        visualize_graph(self.graph, notified_nodes, source_node, radius, police_path)

# Run the customtkinter Application
if __name__ == "__main__":
    root = ctk.CTk()
    app = CrimeGraphApp(root)
    root.mainloop()
