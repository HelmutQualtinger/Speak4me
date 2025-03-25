import networkx as nx
import matplotlib.pyplot as plt
import math
def collatz_sequence(n):
    """Generate the Collatz sequence starting from n."""
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)  # Append the last element (1)
    return sequence

def create_collatz_graph(sequence):
    """Create a directed graph from the Collatz sequence."""
    G = nx.DiGraph()
    for i in range(len(sequence) - 1):
        if sequence[i] != 1:
            G.add_edge(sequence[i], sequence[i + 1])
    return G

def display_graph(G, filename="collatz_graph.png"):
    """Display the graph using matplotlib and save it as a PNG file."""
    pos = nx.spring_layout(G)       # positions for all nodes
    # Create a dictionary to store vertical positions based on sequence order
    pos_y = {}
    pos_x = {}
    for i, node in enumerate(G.nodes()):
        pos_y[node] = -i  # Negative to have sequence flow downwards
        pos_x[node] = node
       
    # Update positions to have vertical ordering match sequence
    for node in pos:
        pos[node] = (math.log(pos_x[node], 2), pos_y[node])
    
    # Create edge lists for rising and non-rising edges
    rising_edges = [(u,v) for (u,v) in G.edges() if v > u]
    other_edges = [(u,v) for (u,v) in G.edges() if v <= u]
    
    # Draw the regular edges
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color='green',arrows=True, arrowstyle='-|>', arrowsize=20, connectionstyle='arc3,rad=-0.1')
    
    # Draw rising edges in red and thicker with curved edges
    nx.draw_networkx_edges(G, pos, edgelist=rising_edges, edge_color='red', width=2.0, arrows=True, connectionstyle='arc3,rad=-0.1')
    
    # Draw nodes and labels
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')
    
    plt.style.use('seaborn-v0_8')
    plt.title("Collatz Sequence Graph", color='white', fontsize=14, pad=20)
    plt.axis('off')
    plt.tight_layout()
    
    # Save the figure as a PNG file
    plt.savefig(filename, format='png', bbox_inches='tight')
    plt.show()

def main():
    n = int(input("Enter a positive integer to generate its Collatz sequence: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    sequence = []
    for i in range(1, n+1):
        sequence.extend(collatz_sequence(i))
    print("Collatz sequence:", sequence)

    G = create_collatz_graph(sequence)
    display_graph(G)

if __name__ == "__main__":
    main()