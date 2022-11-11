from flask import render_template, request, redirect
from app import app, db
from models import Employees


@app.route('/')
def index():
    employees = db.session.query(Employees).all()
    return render_template(
        'index.html',
        title='Главная',
        employees=employees
    )


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        res = request.form.to_dict()
        employee = Employees(
            name=res['name'],
            email=res['email'],
            phone=res['phone']
        )
        db.session.add(employee)
        db.session.commit()
        return redirect('/')
    return render_template(
        'index.html',
        title='Главная'
    )


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        new = request.form.to_dict()
        emp_to_upd = Employees.query.get(new['id'])

        emp_to_upd.name = new['name']
        emp_to_upd.email = new['email']
        emp_to_upd.phone = new['phone']

        db.session.add(emp_to_upd)
        db.session.commit()

        return redirect('/')
    return render_template('index.html', title='Главная')


@app.route('/delete/<int:id>')
def delete(id):
    emp_to_del = Employees.query.get(id)

    db.session.delete(emp_to_del)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
