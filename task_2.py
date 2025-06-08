from bfs_path import bfs_path
from dfs_path import dfs_path
from task_1 import build_graph


if __name__ == "__main__":
    metro_graph = build_graph()
    start_node = "Центр"
    goal_node = "Музей"

    dfs_result = dfs_path(metro_graph, start_node, goal_node)
    bfs_result = bfs_path(metro_graph, start_node, goal_node)

    print("-> DFS шлях (глибина):", " ➝ ".join(dfs_result))
    print("-> BFS шлях (ширина):", " ➝ ".join(bfs_result))

    print("\n Пояснення:")
    print("DFS занурюється якнайглибше — тому може знайти не найкоротший шлях.")
    print("BFS проходить рівнями — завжди знаходить найкоротший шлях за кількістю кроків.")