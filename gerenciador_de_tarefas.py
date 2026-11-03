# Aluno: David Victor Ferreira Soares
# Materia : Liguagens e Técnicas de Programação 1

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Categoria:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Prazo:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Tarefa:
    def __init__(self, titulo, prioridade, status, usuario, categoria, prazo):
        self.titulo = titulo
        self.prioridade = prioridade
        self.status = status
        self.usuario = usuario
        self.categoria = categoria
        self.prazo = prazo

class Prazo:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


if __name__ == "__main__":
    
    usuario1 = Usuario("David Victor", "david.victor@example.com")
    
    categoria1 = Categoria("Trabalho", "Tarefas relacionadas ao trabalho")
    
    prazo1 = Prazo(15, 12, 2023)
    
    tarefa1 = Tarefa("Desenvolver relatório", 1, "Pendente", usuario1, categoria1, prazo1)