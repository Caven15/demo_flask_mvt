from flask import redirect, render_template, url_for
from app import app
from app.models.db.db_model import Task
from app.models.forms.task_form import Task_form
from app.tools.session_scope import session_scope


@app.route('/tasks', methods=['GET'])
def get_tasks():
    with session_scope() as session:
        tasks = session.query(Task).all()
    return render_template('task/tasks.html', tasks=tasks)

# Create
@app.route('/task/create', methods=['GET', 'POST'])
def create_Task():
    form = Task_form()
    print("test")
    if form.validate_on_submit():
        nouvelle_tache = Task(description= form.description.data)
        with session_scope() as session:
            session.add(nouvelle_tache)
        return  redirect(url_for('get_tasks'))
    return render_template('task/create_task.html', form=form)

# update
@app.route('/task/update/<int:id>', methods=['GET', 'POST'])
def update_task(id):
    # recherche de l'élément à mettre à jour
    pass



# delete