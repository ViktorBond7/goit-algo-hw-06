import networkx as nx
import matplotlib.pyplot as plt
from task_1 import build_graph


if __name__ == "__main__":
    metro_graph = build_graph()

    # Застосування алгоритму Дейкстри
    shortest_paths = nx.single_source_dijkstra_path(metro_graph, source='Центр')
    shortest_path_lengths = nx.single_source_dijkstra_path_length(metro_graph, source='Центр')

    print(shortest_paths)  # виведе найкоротші шляхи від вузла 'Центр' до всіх інших вузлів
    print(shortest_path_lengths)  # виведе довжини найкоротших шляхів від вузла 'Центр' до всіх інших вузлів
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(metro_graph, seed=42)
    nx.draw(metro_graph, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(metro_graph, 'weight')
    nx.draw_networkx_edge_labels(metro_graph, pos, edge_labels=edge_labels, font_color='black')
    plt.show()