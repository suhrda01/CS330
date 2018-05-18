from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Daniel"
    return render_template('index.html')

@app.route('/processform')
def procform():
    name = "Daniel"
    numOdds = int(request.args.get('numodds'))
    num_list = range(1, numOdds*2, 2)
    return render_template('odds.html', odds=num_list)

if __name__ == '__main__':
    app.run(debug=True)