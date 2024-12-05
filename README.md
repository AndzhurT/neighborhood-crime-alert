# Neighborhood Crime Alert Network

## 1. Project Goals

The **Neighborhood Crime Alert Network** (NCAN) uses graph-based algorithms to model a network of neighborhoods (nodes) connected by roads or proximity (edges). It is designed to create a system for visualizing and tracking crime alerts across a network of neighborhoods. If a crime is reported at a node, nearby nodes within a certain distance receive a notification. The core objectives of the project include:

1. **Crime Notification Simulation**: Using a graph-based model, the system simulates how crime alerts are propagated across neighborhoods.
2. **Radius-based Alerting**: Notify neighborhoods within a given radius from the crime location using Dijkstra’s algorithm.
3. **Graph Visualization**: Provide a visual representation of neighborhoods, crime alerts, and connections, with color-coded nodes and edges for better clarity.
4. **User Interaction**: Allow users to input a crime location and notification radius to see the effect of crime spread across the neighborhood network.

## 2. Significance and Novelty of the Project

The project is significant because it blends several important concepts in computer science, such as graph theory (used to represent neighborhoods and their connections) and algorithmic solutions (Dijkstra’s algorithm) to create a real-world application. Its novelty lies in the use of a **visualization** tool that not only simulates crime notifications but also provides a **graph-based representation** of how alerts would propagate geographically. This can be particularly useful for understanding crime spread and improving community safety planning.

### Why It's Meaningful

Neighborhood crime alert systems are integral to modern safety management, where real-time information is vital. By using network visualization and graph algorithms, this project offers a unique approach to model and analyze crime alert propagation, making it easier for authorities and the public to understand and act on crime data.
<hr/>

## 3. Installation and Usage Instructions

### Prerequisites
Before running the application, make sure you have Python 3.6+ installed on your machine. The project requires the following libraries:

- **NetworkX**: To represent and manipulate the graph of neighborhoods.
- **Tkinter**: For the user interface to interact with the system.

### Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/neighborhood-crime-alert-network.git
   cd neighborhood-crime-alert-network

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
3. **Run the Application**: Start the application by running:
    ```bash
    python main.py

### Usage Instructions
- **Select a Crime Location (Source Node):** Choose the neighborhood where the crime has occurred. This is the source node for the crime alert.
- **Enter a Radius:** Enter the radius (in miles) for how far crime notifications should be sent.
- **Click Visualize:** Click the "Visualize" button to see the graph representation of crime alert propagation, with neighborhoods that fall within the specified radius highlighted.

### Example Usage
- If the crime happens in the Downtown neighborhood and the radius is set to 5 miles, the system will show which neighborhoods will be notified about the crime event, displayed with different colors on the graph.

### How It Works
- **_Graph Representation:_** The neighborhoods are represented as nodes in an undirected graph, with edges indicating the distances (in miles) between neighboring areas.<br/>

- **_Dijkstra's Algorithm:_** When a user selects a neighborhood as the source node (crime location) and enters a radius, Dijkstra’s algorithm calculates which neighborhoods fall within that radius and should be notified about the crime.<br/>

- **_Visualization:_** The graph is visualized using Matplotlib and NetworkX. The nodes are color-coded, and edges between nodes are styled differently to highlight connections between notified neighborhoods.<br/>

### Examples
![image](https://github.com/user-attachments/assets/9c75a0b3-0692-4c53-8bd9-3b0690289d5c)
![image](https://github.com/user-attachments/assets/eb485a66-3b5c-4590-9164-0b6e05cabfc6)
<hr/>

## 4. Code Structure
This flowchart captures the sequence of steps the program follows from when the user provides input and presses the "Visualize" button, all the way through graph creation, algorithm application, and visualization.
### Flow chart representation:
![image](https://github.com/user-attachments/assets/1d509b8f-9770-4dc7-ae58-d9b251841885)
<hr/>

## 5. List of Functionalities and Verification Results
### Functionalities:
- **Interactive UI** with Tkinter to input the source node (crime location) and notification radius.
- **Graph visualization** using **NetworkX** to represent neighborhoods and their connections.
- **Dijkstra's algorithm** to calculate the neighborhoods within a given radius from the source node.
- **Color-coded nodes** and edges for better visual representation:
  - Red for the source node (crime location).
  - Gold for notified nodes.
  - Blue for other neighborhoods.
  - Orange-red for edges connecting notified neighborhoods.

### Verification Results:
- **Correctness of Notification**: The algorithm correctly identifies neighborhoods within the radius and marks them for notification.
- **Graph Rendering**: The visualization accurately represents the graph with color-coded nodes and edges, ensuring that the crime notification propagation is easy to understand.
- **UI Functionality**: The UI accepts inputs for source and radius, and triggers the visualization accurately.
<hr/>

## 6. Showcasing the Achievement of Project Goals

### Execution Results:
- **Crime Event in Downtown**: The crime occurred in Downtown, and the radius was set to 4 miles. The visualization correctly displayed the neighborhoods within this radius as highlighted nodes, with the edges between them showing their connections.
 **Visualization**: The nodes were displayed in various colors to distinguish between the crime source, notified neighborhoods, and others. The result clearly shows the spread of the alert.

### Achievements:
- The project successfully meets its goal of visualizing and propagating crime notifications across a network of neighborhoods.
- It provides an interactive UI that allows users to input data and see real-time results through graph visualization.
- The use of Dijkstra’s algorithm ensures efficient calculation of neighborhoods to be notified.
<hr/>

