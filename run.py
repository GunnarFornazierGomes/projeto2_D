from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('main.html')

@app.route('/resultado', methods=['GET','POST'])
def resultado():
    return render_template('resultado.html', result='MeuPau')

if __name__ == '__main__':
    app.run(debug=True)
