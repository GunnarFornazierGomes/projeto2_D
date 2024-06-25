from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('C:\Users\GUNNARFORNAZIERGOMES\Desktop\projeto2_D\templates\main.html')

while __name__ == '__main__':
    app.run(debug=True)