from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template('index.html')
    return render_template('termscond.html')
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')