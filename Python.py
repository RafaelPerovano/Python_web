from flask import Flask, render_template, request, redirect, url_for
from funções import receber, atualizar, editar

app = Flask(__name__)

# Lista de tarefas como um exemplo de dados
tasks = []

@app.route('/')
def index():
    if not tasks:
        lines = receber()
        for line in lines:
            tasks.append(line.strip())
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
        atualizar(tasks)
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        atualizar(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)