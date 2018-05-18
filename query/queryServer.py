from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():
    conn = psycopg2.connect(user='suhrda01', host='localhost', port=2345, dbname='world')
    cur = conn.cursor()
    cur.execute("""select distinct continent from country""")
    res = cur.fetchall()
    return render_template('index.html', continents=res)

@app.route('/processform')
def processform():
    continent = request.args.get('continent')
    conn = psycopg2.connect(user='suhrda01', host='localhost', port=2345, dbname='world')
    cur = conn.cursor()
    cur.execute("""select * from country where continent = '"""+ continent +"""'""")
    cols = []
    for Column in cur.description:
        cols.append(Column.name)
    res = cur.fetchall()
    cur.execute("""select distinct continent from country""")
    cont = cur.fetchall()
    return render_template('data.html', cols=cols, data=res, continents=cont)

if __name__ == '__main__':
    app.run(debug=True)

