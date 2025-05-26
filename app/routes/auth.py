from flask import app, render_template

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    pass