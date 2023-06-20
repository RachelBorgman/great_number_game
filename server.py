from flask import Flask, render_template, request, redirect, session
# , redirect

app = Flask(__name__)
app.secret_key = 'secret and safe'

@app.route('/')
def random_number():
    import random
    if "number" not in session:
        session['number'] = random.randint(1, 100)
    # session['number'] = request.form['number']
    return render_template('number.html')

@app.route('/guess', methods=["POST"])
def guess_number():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True, host="localhost", port=8000)