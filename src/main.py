import json
from buscaEmLargura import bfs, print_solution_bfs
from dijkstra import uniform_cost_search, print_solution
from buscaEmProfundidadeLimitada import depth_limited_search
from buscaEmProfundidadeIterativa import iterative_deepening_search
from utils import solution_with_cost, print_solution_generic
from readProblem import RomaniaProblem # Importa a classe RomaniaProblem


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

    print("\nIniciando busca em profundidade limitada (limite=3)...")

    # Executa a busca em profundidade limitada
    limit = 3
    result_node = depth_limited_search(problem, limit)
    if result_node and result_node != 'cutoff':
        path_dls = solution_with_cost(problem, result_node)
        total_cost_dls = result_node['cost']
        print_solution_generic(path_dls, total_cost_dls, "Busca em Profundidade Limitada", limit)
    else:
        print_solution_generic(None, 0, "Busca em Profundidade Limitada", limit)

    print("\nIniciando busca em profundidade com profundidade iterativa...")

    # Executa a busca em profundidade com profundidade iterativa
    path_iddfs, total_cost_iddfs = iterative_deepening_search(problem)
    print_solution_generic(path_iddfs, total_cost_iddfs, "Busca com profundidade Iterativa")

if __name__ == "__main__":
    main()
