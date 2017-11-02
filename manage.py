from flask_script import Manager

from myapp.app import app as flask_app

manager = Manager(flask_app)

# print(dir(flask_app))

@manager.command
def hello():
    print( "hello world")

@manager.command
def runserver():
    flask_app.run()

if __name__ == "__main__":
    manager.run()
