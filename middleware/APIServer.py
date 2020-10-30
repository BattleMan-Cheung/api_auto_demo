from flask import Flask

app = Flask(__name__)


@app.route("/login", methods=['GET', 'POST'])
def login():
    return 'this is an api！'


if __name__ == '__main__':
    app.run()
