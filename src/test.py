from bottle import run, route, template

@route('/')
def index():
    return template('index')


if __name__ == "__main__":
    run(debug=True, reloader=True)
