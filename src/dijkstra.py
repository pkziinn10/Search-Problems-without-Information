import heapq
from utils import solution_with_cost, print_solution_generic

def uniform_cost_search(problem):
    frontier = []
    node = {
        'state': problem.initial_state,
        'parent': None,
        'action': None,
        'cost': 0
    }
    # Usamos um dicionário para rastrear o melhor custo e o nó correspondente
    frontier_dict = {problem.initial_state: node}
    heapq.heappush(frontier, (0, id(node), node))

    explored = set()

    while frontier:
        current_cost, _, node = heapq.heappop(frontier)
        current_state = node['state']

        # Verifica se este nó ainda é o melhor conhecido para este estado
        if current_state in frontier_dict and frontier_dict[current_state] is not node:
            if node['cost'] > frontier_dict[current_state]['cost']:
                continue

        if problem.is_goal(current_state):
            return solution_with_cost(problem, node), node['cost']

        if current_state in explored:
            continue

        explored.add(current_state)

        for action in problem.actions(current_state):

            # Descobre qual é o estado do filho
            child_state = problem.result(current_state, action)

            # Obtém o custo para ir da cidade atual até essa cidade vizinha
            step_cost = problem.get_cost(current_state, action)

            # Calcula o custo total do caminho desde a origem até o filho
            total_cost = node['cost'] + step_cost

            child = {
                'state': child_state,
                'parent': node,
                'action': action,
                'cost': total_cost
            }

            if child_state in explored:
                continue

            if child_state not in frontier_dict:
                # Adiciona à fronteira
                frontier_dict[child_state] = child
                heapq.heappush(frontier, (total_cost, id(child), child))
            elif total_cost < frontier_dict[child_state]['cost']:
                # Encontrou caminho melhor
                old_node = frontier_dict[child_state]
                frontier_dict[child_state] = child
                heapq.heappush(frontier, (total_cost, id(child), child))

    return None, float('inf')

def print_solution(path_dijkstra, total_cost_dijkstra):
    # Wrapper para a função de impressão genérica
    print_solution_generic(path_dijkstra, total_cost_dijkstra, "Busca de Custo Uniforme")
