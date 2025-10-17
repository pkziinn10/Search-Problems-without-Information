from collections import deque
from utils import solution_with_cost, print_solution_generic

def bfs(problem):
# Busca em Largura retornando o caminho de cidades e o custo total

    # Inicializa o nó raiz
    node = {
        'state': problem.initial_state,
        'parent': None,
        'action': None,
        'cost': 0
    }

    # Teste de objetivo no estado inicial
    if problem.is_goal(node['state']):
        return solution_with_cost(problem, node), node['cost']

    # Fronteira como fila FIFO e conjunto de explorados
    frontier = deque([node])
    explored = set()

    # Para otimização para eliminar estados duplicados
    frontier_states = {problem.initial_state}

    while frontier:
        node = frontier.popleft()  # Removendo o nó mais antigo da borda
        current_state = node['state']
        frontier_states.remove(current_state)
        explored.add(current_state)

        # print(f"Expandindo: {current_state} (custo acumulado: {node['cost']})")

        # Expande os filhos (cidades vizinhas)
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

            # Verifica se o estado já foi visitado
            if child_state not in explored and child_state not in frontier_states:
                if problem.is_goal(child_state):
                    # print(f"\n*** SOLUÇÃO ENCONTRADA! ***")
                    # print(f"Custo total: {total_cost} km")
                    return solution_with_cost(problem, child), total_cost

                frontier.append(child)
                frontier_states.add(child_state)
                # print(f"  → Adicionado à fronteira: {child_state} (custo: {step_cost})")

    return None, float('inf')

def print_solution_bfs(path, total_cost):
    # Wrapper para a função de impressão genérica
    print_solution_generic(path, total_cost, "Busca em Largura")
