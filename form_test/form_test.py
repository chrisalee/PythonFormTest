from flask import Flask, render_template, request, redirect, session # added request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'  #set up a secret key for security purposes


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(f"adding user {request.form['username']} to the database")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['username']
    session['useremail'] = request.form['useremail']
    print(f"username submitted: {request.form['username']}")
    print(f"email submitted: {request.form['useremail']}")
    return redirect('/show')

@app.route("/show")
def show_user():
    return render_template("show.html", name=session['username'], em=session['useremail'])




if __name__=="__main__":
    app.run(debug=True)