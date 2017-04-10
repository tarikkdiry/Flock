from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Tarik'} # fake user
    posts = [ # fake array of posts
        {
            'author': {'nickname': 'Tarik'},
            'body': 'Jimmy is a bitch'
        },
        {
            'author': {'nickname': 'Oscar'},
            'body': 'Jimmy is a bitch'
        }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
