from flask import Flask, render_template, json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/results')
def about():
    return render_template('results.html')

@app.route('/test')
def test():
    my_dict = {"title": "Bayside", "genre": "Alternative"}
    return json.dumps(my_dict)

if __name__ == '__main__':
    print("server is running on localhost!!")
    app.run()