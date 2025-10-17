from buscaEmProfundidadeLimitada import depth_limited_search
from utils import solution_with_cost

def iterative_deepening_search(problem, limit_max=100):
    for depth in range(limit_max):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            # Se o resultado não for 'cutoff', pode ser uma solução (nó) ou falha (None)
            if result:
                path = solution_with_cost(problem, result)
                total_cost = result['cost']
                return path, total_cost
            else:
                # Se for None, significa que a busca falhou sem atingir o limite,
                # então não há solução.
                return None, float('inf')
    return None, float('inf') # Limite máximo de iteração atingido
