from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = ["Contoh"]

def get_tasks():
    # Fungsi untuk mendapatkan daftar tugas
    return ["Contoh"]

def add_task(tasks, new_task):
    # Fungsi untuk menambahkan tugas ke daftar
    return tasks + [new_task]

def delete_task(tasks, index):
    # Fungsi untuk menghapus tugas dari daftar berdasarkan indeks
    return tasks[:index] + tasks[index+1:]

def update_task(tasks, index, updated_task):
    # Fungsi untuk memperbarui tugas dalam daftar berdasarkan indeks
    return tasks[:index] + [updated_task] + tasks[index+1:]

@app.route('/')
def todo_list():
    return render_template('todo_list.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form.get('task')
    tasks.append(new_task)
    return redirect('/')

@app.route('/delete_task/<int:index>')
def delete_task(index):
    del tasks[index]
    return redirect('/')

@app.route('/update_task/<int:index>', methods=['GET', 'POST'])
def update_task(index):
    if request.method == 'POST':
        updated_task = request.form.get('updatedTask')
        tasks[index] = updated_task
        return redirect('/')
    else:
        return render_template('update_task.html', index=index, task=tasks[index])


if __name__ == '__main__':
    app.run(debug=True)
