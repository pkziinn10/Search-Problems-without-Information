import heapq


def uniform_cost_search(problem):
    # Busca de Custo Uniforme - encontra o caminho com menor custo total
    # Fila de prioridade (custo, estado, nó)
    frontier = []
    node = {
        'state': problem.initial_state,
        'parent': None,
        'action': None,
        'cost': 0
    }
    heapq.heappush(frontier, (0, id(node), node))

    explored = set()
    frontier_states = {problem.initial_state: 0}  # estado: melhor_custo

    while frontier:
        current_cost, _, node = heapq.heappop(frontier)
        current_state = node['state']

        if problem.is_goal(current_state):
            return solution_with_cost(problem, node), node['cost']

        if current_state in explored:
            continue

        explored.add(current_state)

        # print(f"Expandindo: {current_state} (custo acumulado: {node['cost']})")

        for action in problem.actions(current_state):
            child_state = problem.result(current_state, action)
            step_cost = problem.get_cost(current_state, action)
            total_cost_dijkstra = node['cost'] + step_cost

            child = {
                'state': child_state,
                'parent': node,
                'action': action,
                'cost': total_cost_dijkstra
            }

            # Se é um estado novo ou encontramos um caminho mais barato
            if child_state not in explored and (child_state not in frontier_states or total_cost_dijkstra < frontier_states[child_state]):
                heapq.heappush(frontier, (total_cost_dijkstra, id(child), child))
                frontier_states[child_state] = total_cost_dijkstra
                # print(f"  → Adicionado à fronteira: {child_state} (custo: {step_cost}, acumulado: {total_cost_dijkstra})")

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
