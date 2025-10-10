import heapq


def uniform_cost_search_corrected(problem):
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

def solution_with_cost(problem, node):
    # Reconstrói o caminho completo
    path_dijkstra = []
    current = node

    while current:
        path_info = {
            'city': current['state'],
            'action': current['action'],
            'step_cost': 0 if current['parent'] is None else
                        problem.get_cost(current['parent']['state'], current['state']),
            'total_cost_dijkstra': current['cost']
        }
        path_dijkstra.append(path_info)
        current = current['parent']

    path_dijkstra.reverse()
    return path_dijkstra

def print_solution(path_dijkstra, total_cost_dijkstra):
    # Imprime a solução de forma organizada
    if not path_dijkstra:
        print("Nenhuma solução encontrada!")
        return

    print("\n" + "="*60)
    print("SOLUÇÃO - BUSCA DE CUSTO UNIFORME")
    print("="*60)

    print(f"De: {path_dijkstra[0]['city']} → Para: {path_dijkstra[-1]['city']}")
    print(f"Custo total: {total_cost_dijkstra} km")
    print(f"Número de cidades no caminho: {len(path_dijkstra)}")
    print("\nCaminho detalhado:")
    print("-" * 40)

    for i, step in enumerate(path_dijkstra):
        if i == 0:
            print(f" Início em: {step['city']}")
        else:
            prev_city = path_dijkstra[i-1]['city']
            print(f"  → {step['action']} para {step['city']} "
                  f"({step['step_cost']} km) "
                  f"[Acumulado: {step['total_cost_dijkstra']} km]")

    print("="*60)
