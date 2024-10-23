import json

# Classe para gerenciar as tarefas
class GerenciadorTarefas:
    def __init__(self, arquivo='tarefas.json'):
        self.arquivo = arquivo
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        try:
            with open(self.arquivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvar_tarefas(self):
        with open(self.arquivo, 'w') as f:
            json.dump(self.tarefas, f, indent=4)

    def adicionar_tarefa(self, descricao, prazo, prioridade):
        tarefa = {
            "descricao": descricao,
            "prazo": prazo,
            "prioridade": prioridade,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        self.salvar_tarefas()

    def listar_tarefas(self, concluida=False):
        for tarefa in self.tarefas:
            if tarefa['concluida'] == concluida:
                print(f"Descrição: {tarefa['descricao']}, Prazo: {tarefa['prazo']}, Prioridade: {tarefa['prioridade']}")

    def marcar_concluida(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]['concluida'] = True
            self.salvar_tarefas()

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            self.salvar_tarefas()

    def filtrar_por_prioridade(self, prioridade):
        return [tarefa for tarefa in self.tarefas if tarefa['prioridade'] == prioridade]
