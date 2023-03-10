from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
   
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        email = request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        if len(email) < 5:
            flash('Email must be greater than 5 charaters', category='error')
            pass
        elif len(firstName)<2:
            flash('First name must be greater than 3 charaters', category='error')
            pass
        elif password1!=password2:
            flash('password don\' match', category='error')
            pass
        elif len(password1) <7:
            flash('Password must be at least 7 charaters', category='error')
            pass
        else:
            flash('Account created!', category='success')
            
    return render_template("signup.html")