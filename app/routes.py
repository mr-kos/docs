from app import my_app

@my_app.route('/')
@my_app.route('/index')
def index():
    return "Hello, World!"