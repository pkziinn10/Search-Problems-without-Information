def depth_limited_search(problem, limit):
    initial_node = {
        'state': problem.initial_state,
        'parent': None,
        'action': None,
        'cost': 0
    }
    return recursive_dls(initial_node, problem, limit)


def recursive_dls(node, problem, limit):
    if problem.is_goal(node['state']):
        return node  # Retorna o nó da solução

    if limit == 0:
        return 'cutoff'  # Limite de profundidade atingido

    cutoff_occurred = False
    for action in problem.actions(node['state']):
        child_state = problem.result(node['state'], action)
        step_cost = problem.get_cost(node['state'], action)

        child_node = {
            'state': child_state,
            'parent': node,
            'action': action,
            'cost': node['cost'] + step_cost
        }

        result = recursive_dls(child_node, problem, limit - 1)

        if result == 'cutoff':
            cutoff_occurred = True
        elif result is not None:
            return result  # Solução encontrada

    return 'cutoff' if cutoff_occurred else None
