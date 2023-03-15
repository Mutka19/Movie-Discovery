import flask

app = flask.Flask('Movie Discovery')

@app.route('/')
def index():
    return flask.render_template('index.html')