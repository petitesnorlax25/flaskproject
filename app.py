from flask import Flask, render_template

app = Flask(__name__)

@app.route('/helloflask')
def home():
    return render_template('index.htmlkk')

if __name__ == '__main__':
    app.run(debug=True)
