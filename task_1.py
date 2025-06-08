import networkx as nx
import matplotlib.pyplot as plt

def build_graph():
    # Створюємо граф
    metro_graph = nx.Graph()

    # Додаємо вершини (станції метро)
    stations = [
        "Центр", "Університет", "Площа Ринок", "Вокзал", "Парк", "Музей", "Театр", "Бібліотека"
    ]
    metro_graph.add_nodes_from(stations)

    # Додаємо ребра (лінії метро)
    metro_graph.add_edges_from([
        ("Центр", "Університет", {"weight": 3}),
        ("Центр", "Площа Ринок", {"weight": 2}),
        ("Університет", "Площа Ринок", {"weight": 4}),
        ("Університет", "Вокзал", {"weight": 4}),
        ("Площа Ринок", "Парк", {"weight": 2}),
        ("Вокзал", "Парк", {"weight": 4}),
        ("Парк", "Музей", {"weight": 3}),
        ("Музей", "Театр", {"weight": 5}),
        ("Театр", "Бібліотека", {"weight": 2}),
        ("Центр", "Бібліотека", {"weight": 1}),
    ])

    return metro_graph

def print_graph(metro_graph):
    # Аналіз характеристик
    print("Кількість вершин (станцій):", metro_graph.number_of_nodes())
    print("Кількість ребер (ліній):", metro_graph.number_of_edges())

    # Ступінь кожної вершини
    print("\n Ступінь вершин:")
    for node, degree in metro_graph.degree():
        print(f"   {node}: {degree}")


if __name__ == "__main__":
    metro_graph = build_graph()
    #Візуалізація графа
    plt.figure(figsize=(8, 6))
    nx.draw(metro_graph, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, font_weight='bold')
    plt.title("Транспортна мережа: Станції метро")
    plt.show()

    print_graph(metro_graph)

    


