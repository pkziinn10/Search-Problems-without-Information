import json
from buscaEmLargura import bfs, print_solution_bfs
from dijkstra import uniform_cost_search, print_solution
from readProblem import RomaniaProblem


def main():
    # Carrega o problema da Romênia
    try:
        problem = RomaniaProblem('romenia.json')
        print(f"Problema carregado:")
        print(f"  Cidade inicial: {problem.initial_state}")
        print(f"  Cidade objetivo: {problem.goal_state}")
        print(f"  Total de cidades: {len(problem.edges)}")
    except FileNotFoundError:
        print("Erro: Arquivo 'romenia.json' não encontrado!")
        return
    except json.JSONDecodeError:
        print("Erro: Arquivo JSON inválido!")
        return

    print("\nIniciando busca em largura...")

    # Executa a busca em largura
    path, total_cost = bfs(problem)
    print_solution_bfs(path, total_cost)

    print("\nIniciando busca de custo uniforme...")

    # Executa a busca de custo uniforme
    path_dijkstra, total_cost_dikstra = uniform_cost_search(problem)
    print_solution(path_dijkstra, total_cost_dikstra)

if __name__ == "__main__":
    main()
