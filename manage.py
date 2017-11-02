from flask_script import Manager

from myapp import app

# print(dir(app))

manager = Manager(app.flask_app)

@manager.command
def hello():
    print( "hello world")

manager.add_command('runserver', app.flask_app.run())

if __name__ == "__main__":
    manager.run()
