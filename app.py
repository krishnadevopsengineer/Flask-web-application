from flask import Flask, render_template, request, redirect, url_for

# WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/submit_name', methods=['GET','POST'])
def submit_name():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}!"
    return render_template('form.html')

# Route for handling total score submission
@app.route('/totalscore', methods=['GET', 'POST'])
def totalscore():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4
        return redirect(url_for('successres', score=total_score))
    
    return render_template('form.html')

# Success route for score calculation
@app.route('/successres/<int:score>')
def successres(score):
    res = "PASSED" if score >= 50 else "FAILED"
    exp = {'score': score, 'res': res}
    return render_template('result1.html', results=exp)

if __name__ == "__main__":
    app.run(debug=True)
