from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/plantillas')
def plantillas():
    return render_template('plantillas.html')

if __name__ == '__main__':
    app.run(debug = True)