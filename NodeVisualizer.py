## 🔍 Blockchain Node Visualizer (Python)
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = ['Firewall Node', 'Habit Agent 1', 'Habit Agent 2', 'Solana Node', 'User Wallet']

G.add_edges_from([
    ('User Wallet', 'Firewall Node'),
    ('Firewall Node', 'Habit Agent 1'),
    ('Firewall Node', 'Habit Agent 2'),
    ('Habit Agent 1', 'Solana Node'),
    ('Habit Agent 2', 'Solana Node')
])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='cyan', edge_color='gray', node_size=2000, font_size=10)
plt.title("LoopZero Blockchain-AI Node Flow")
plt.show()
