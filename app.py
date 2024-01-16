from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('loginPage.html')

@app.route('/dashboardPage')
def dashboard():
    return 'This is dashboardPage'

# Uncomment the following routes if needed
# @app.route('/modifyPage')
# def page3():
#     return 'This is modifyPage'

# @app.route('/requestPage')
# def page4():
#     return 'This is requestPage'

if __name__ == '__main__':
    app.run()
