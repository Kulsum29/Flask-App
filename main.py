from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Blogs.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://username:password@hostname:port/dbname"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://blog_app_0vy6_user:jKymXa0X1b602FHx2X1bxWCr4rz6lx5R@dpg-d0g1ftqdbo4c73au86k0-a.oregon-postgres.render.com/blog_app_0vy6"
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    blogposts = Blog.query.all()
    return render_template('index.html',blogposts = blogposts)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)



# pip show sqlalchemy
# pip install flask-sqlalchemy
# https://sqlitebrowser.org/