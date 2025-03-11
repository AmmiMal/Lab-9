# Портфолио разработчика. Поля ввода данных: названием, ссылки на репозиторий (рабочая). БД: title, link
# Сделать очистку ленты сообщений, запускаемую кнопкой "Clear".

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask("Developer's portfolio")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lab.db'
db = SQLAlchemy(app)


products = [
    {'prod_name': 'sofa',
     'price': 12000,
     'in_stock': False,
     'id': 0},
    {'prod_name': 'table',
     'price': 6000,
     'in_stock': True,
     'id': 1},
    {'prod_name': 'chair',
     'price': 8000,
     'in_stock': False,
     'id': 2},
]


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.id}. {self.title} - {self.link}'


@app.route('/')
def index():
    projects = Portfolio.query.all()
    print(projects)
    return render_template('lab_9.html', project_list=projects)


# @app.route('/notes', methods=['GET'])
# def get_notes():
#     notes = Note.query.all()
#     notes_list = [{'id': note.id, 'text': note.text, 'important': note.important} for note in notes]
#     return jsonify(notes_list)


@app.route('/add', methods=['POST'])
def add_project():
    data = request.get_json()
    title = data['title']
    link = data['link']
    project = Portfolio(title=title, link=link)
    db.session.add(project)
    db.session.commit()


@app.route('/clear', methods=['POST'])
def clear_notes():
    db.session.query(Portfolio).delete()
    db.session.commit()
    return jsonify({'message': 'All notes cleared!'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)