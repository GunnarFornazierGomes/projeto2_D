from flask import Flask, render_template, request, get_template_attribute
import roman





app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('main.html')

@app.route('/resultado', methods=['GET','POST'])
def resultado():
    response = request.form['numeroRomano']
    response_str = str(response)
    response_upper = response_str.upper()
    transformResponse = roman.fromRoman(response_upper)
    
    return render_template('resultado.html', result=transformResponse)

if __name__ == '__main__':
    app.run(debug=True)
