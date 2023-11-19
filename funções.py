import os

# Função que recebe do arquivo
def receber():
    if verifica_arquivo():
        with open('tarefas.txt', 'r') as arquivo:
            conteudo = arquivo.read()
        return conteudo
    else:
        with open('tarefas.txt', 'w') as arquivos:
            pass
        return receber()

# Função que verifica se o arquivo existe
def verifica_arquivo():
    return os.path.exists('tarefas.txt')

# Função para atualizar tarefas à lista
def atualizar(tarefas):
    with open('tarefas.txt', 'w') as arquivos:
        for tarefa in tarefas:
            arquivos.write('{}\n'.format(tarefa))

# Função para editar os contatos da agenda
def editar(tarefa, tarefa_cha):
    tarefas = receber()
    tarefas[tarefa] = tarefa_cha

    with open('tarefas.txt', 'w') as arquivos:
        for tarefa in tarefas():
            arquivos.write('{}\n'.format(tarefa))
