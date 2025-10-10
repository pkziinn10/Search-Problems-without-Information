import json
from collections import deque

class RomaniaProblem:
    def __init__(self, json_file):
        # Carrega os dados do arquivo JSON
        with open(json_file, 'r') as f:
            data = json.load(f)

        self.initial_state = data['initial_state']
        self.goal_state = data['goal']
        self.edges = data['edges']
        self.heuristics = data.get('h', {})
        self.coords = data.get('coords', {})

    def is_goal(self, state):
        # Verifica se o estado atual é o estado objetivo
        return state == self.goal_state

    def actions(self, state):
        # Retorna todas as cidades conectadas à cidade atual
        if state in self.edges:
            return list(self.edges[state].keys())
        return []

    def result(self, state, action):
        # Dada uma cidade e uma ação (cidade destino), retorna a cidade destino
        return action

    def get_cost(self, state, action):
        # Retorna o custo de ir de 'state' para 'action'
        if state in self.edges and action in self.edges[state]:
            return self.edges[state][action]
        return 0
