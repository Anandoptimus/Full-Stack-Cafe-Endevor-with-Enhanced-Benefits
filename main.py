from flask import Flask, jsonify, url_for, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__, static_url_path='/static')

# CREATE DB
# class Base(DeclarativeBase):
#     pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


class Deleted_history(db.Model):
    __tablename__ = "Deleted History"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


class user(db.Model):
    __tablename__ = "user_authentication"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), unique=True, nullable=False)

with app.app_context():
    db.create_all()


@app.route("/home/<u_id>")
def home(u_id):
    query = db.session.execute(select([Cafe])).scalars().all()
    post = []
    for i in query:
        post.append(i)
    print(f"user is {u_id}")
    return render_template("index.html", all_post=post, useri=u_id)


@app.route("/", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        query = db.session.execute(select([user]).where(user.email == request.form['email'])).scalar()
        if not query:
            error = "Email is not registered, Please sign in"
            return render_template('login.html', error=error)
        elif not check_password_hash(query.password, request.form['password']):
            error = "Invalid password! Try again"
            return render_template('login.html', error=error)
        else:
            user_id = query.id
            return redirect(url_for('home', u_id=user_id))
    return render_template('login.html')

# HTTP GET - Read Record


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        password_hash = generate_password_hash(request.form['password'], salt_length=8)

        user_auth = user(
            name=request.form['name'],
            email=request.form['email'],
            password=password_hash
        )
        db.session.add(user_auth)
        db.session.commit()
        query = db.session.execute(select([user]).where(user.email == request.form['email'])).scalar()
        id = query.id
        return redirect(url_for('home', u_id=id))

    return render_template("signup.html")

# HTTP POST - Create Record


@app.route("/delete/<u_id>", methods=["GET", "POST"])
def delete(u_id):
    query = Cafe.query.get_or_404(u_id)
    print(query.name)
    query1 = Deleted_history(
        name=query.name,
        img_url=query.img_url,
        map_url=query.map_url,
        location=query.location,
        seats=query.seats,
        has_toilet=query.has_toilet,
        has_wifi=query.has_wifi,
        has_sockets=query.has_sockets,
        can_take_calls=query.can_take_calls,
        coffee_price=query.coffee_price
    )
    db.session.add(query1)
    db.session.delete(query)
    db.session.commit()
    return redirect(url_for('home', u_id=u_id))


# HTTP PUT/PATCH - Update Record
@app.route('/add', methods=['GET', 'POST'])
def add():
    return render_template("add.html")
# HTTP DELETE - Delete Record

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "POST":
        query = Cafe(
            name=request.form['name'],
            img_url=request.form['img_url'],
            map_url=request.form['map_url'],
            location=request.form['location'],
            seats=request.form['seats'],
            has_toilet=bool(request.form.get('has_toilet', False)),
            has_sockets=bool(request.form.get('has_sockets', False)),
            can_take_calls=bool(request.form.get('can_take_calls', False)),
            has_wifi=bool(request.form.get('has_wifi', False)),
            coffee_price=request.form['coffee_price']
        )
        db.session.add(query)
        db.session.commit()
        return redirect(url_for('home', u_id=1))


if __name__ == '__main__':
    app.run(debug=True)
