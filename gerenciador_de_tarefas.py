# Aluno: David Victor Ferreira Soares
# Materia : Linguagens e Técnicas de Programação 1

class Usuario:
    def __init__(self, nome, email, id):
        self._nome = nome
        self._email = email
        self.__id = id  

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_id(self):
        return self.__id

class Categoria:
    def __init__(self, nome, descricao):
        self._nome = nome
        self._descricao = descricao
    
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, descricao):
        self._descricao = descricao

class Tarefa:
    def __init__(self, titulo, prioridade, status, usuario, categoria, prazo):
        self._titulo = titulo
        self._prioridade = prioridade
        self._status = status
        self._usuario = usuario
        self._categoria = categoria
        self._prazo = prazo
    
    def get_titulo(self):
        return self._titulo

    def set_titulo(self, titulo):
        self._titulo = titulo

    def get_prioridade(self):
        return self._prioridade

    def set_prioridade(self, prioridade):
        self._prioridade = prioridade

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def get_usuario(self):
        return self._usuario

    def set_usuario(self, usuario):
        self._usuario = usuario

    def get_categoria(self):    
        return self._categoria

    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_prazo(self):
        return self._prazo

    def set_prazo(self, prazo):
        self._prazo = prazo

    def __prioridade_valida(self):
        return self._prioridade >= 1 and self._prioridade <= 3

    def concluir(self):
        if self.__prioridade_valida():
            self._status = "Concluída"
            return "Tarefa concluída!"
        return "Prioridade inválida, não foi possível concluir."

class Prazo:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano

    def get_dia(self):
        return self._dia

    def set_dia(self, dia):
        self._dia = dia

    def get_mes(self):
        return self._mes

    def set_mes(self, mes):
        self._mes = mes

    def get_ano(self):
        return self._ano

    def set_ano(self, ano):
        self._ano = ano

    def prazo_valido(self):
        return self._dia >= 1 and self._dia <= 31 and self._mes >= 1 and self._mes <= 12

if __name__ == "__main__":
    
    usuario1 = Usuario("David Victor", "david.victor@example.com", 1)
    
    categoria1 = Categoria("Trabalho", "Tarefas relacionadas ao trabalho")
    
    prazo1 = Prazo(15, 12, 2023)
    
    tarefa1 = Tarefa("Desenvolver relatório", 1, "Pendente", usuario1, categoria1, prazo1)