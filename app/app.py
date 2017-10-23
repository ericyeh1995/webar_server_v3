from flask import Flask, render_template, redirect
import json

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/<path:topic>', methods=['GET'])
def machineAPI(topic):
    return render_template('machine.html',
                           topic=json.dumps(topic))

@app.route('/svgdemo')
def svgDemo():
    return render_template('svgdemo.html')

@app.route('/svgdemo2')
def svgDemo2():
    return render_template('svgdemo2.html')

@app.route('/videodemo')
def videoDemo():
    return render_template('videodemo.html')

@app.route('/videotest')
def videoTest():
    return redirect("https://www.w3schools.com/html/html5_video.asp", code=302)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
