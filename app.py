from bottle import run, route, template, view, static_file

@route('/')
@view('about')
def about():
    return {}

@route('/loyalty-and-pride')
@view('loyalty-and-pride')
def contact():
    return{}

@route('/family-spirit')
@view('family spirit')
def familyspirit():
    return{}

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)
