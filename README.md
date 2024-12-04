# neighborhood-crime-alert

### Project Description:
The Neighborhood Crime Alert Network (NCAN) uses graph-based algorithms to model a network of neighborhoods (nodes) connected by roads or proximity (edges). If a crime is reported at a node, nearby nodes within a certain distance receive a notification. The graph also provides a visual representation of alerts, helping law enforcement or community members take action.

### Features

- **Interactive UI** with Tkinter to input the source node (crime location) and notification radius.
- **Graph visualization** using **NetworkX** to represent neighborhoods and their connections.
- **Dijkstra's algorithm** to calculate the neighborhoods within a given radius from the source node.
- **Color-coded nodes** and edges for better visual representation:
  - Red for the source node (crime location).
  - Gold for notified nodes.
  - Blue for other neighborhoods.
  - Orange-red for edges connecting notified neighborhoods.
  
### Requirements

- Python 3.6+
- Tkinter
- NetworkX
- Matplotlib

You can install the necessary Python libraries using the following:

```bash
pip install networkx matplotlib
```
<hr/>

### How It Works
- **_Graph Representation:_** The neighborhoods are represented as nodes in an undirected graph, with edges indicating the distances (in miles) between neighboring areas.<br/>

- **_Dijkstra's Algorithm:_** When a user selects a neighborhood as the source node (crime location) and enters a radius, Dijkstra’s algorithm calculates which neighborhoods fall within that radius and should be notified about the crime.<br/>

- **_Visualization:_** The graph is visualized using Matplotlib and NetworkX. The nodes are color-coded, and edges between nodes are styled differently to highlight connections between notified neighborhoods.<br/>

### Examples
![image](https://github.com/user-attachments/assets/9c75a0b3-0692-4c53-8bd9-3b0690289d5c)
![image](https://github.com/user-attachments/assets/eb485a66-3b5c-4590-9164-0b6e05cabfc6)


