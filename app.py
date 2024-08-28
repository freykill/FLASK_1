from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unidad1')
def unidad1():
    return render_template('unidad1.html')

@app.route('/unidad2')
def unidad2():
    return render_template('unidad2.html')

@app.route('/unidad3')
def unidad3():
    return render_template('unidad3.html')

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
