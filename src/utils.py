def solution_with_cost(problem, node):
    path = []
    current = node

    while current:
        step_cost = 0
        if current['parent']:
            # A ação em um nó representa a transição do pai para o estado atual
            step_cost = problem.get_cost(current['parent']['state'], current['state'])

        path_info = {
            'city': current['state'],
            'action': current['action'],
            'step_cost': step_cost,
            'total_cost': current['cost']
        }
        path.append(path_info)
        current = current['parent']

    path.reverse()
    return path


def print_solution_generic(path, total_cost, algorithm_name, limit=None):
    print("\n" + "="*60)
    if not path:
        print(f"NENHUMA SOLUÇÃO ENCONTRADA - {algorithm_name.upper()}")
        if limit is not None:
            print(f"(Com limite de profundidade: {limit})")
    else:
        print(f"SOLUÇÃO ENCONTRADA - {algorithm_name.upper()}")
        print("="*60)
        print(f"De: {path[0]['city']} → Para: {path[-1]['city']}")
        print(f"Custo total: {total_cost} km")
        print(f"Profundidade/Número de cidades: {len(path)}")
        print("\nCaminho detalhado:")
        print("-" * 40)

        for i, step in enumerate(path):
            if i == 0:
                print(f" Início em: {step['city']}")
            else:
                print(f" → para {step['city']} ({step['step_cost']} km) [Acumulado: {step['total_cost']} km]")

    print("="*60)
