from flask import Flask, render_template, request

app = Flask(__name__)

def get_user_role():
    return request.args.get('role', 'unknown')

@app.route('/')
def welcome():
    role = get_user_role()
    return render_template('welcome.html', role=role)

if __name__ == '__main__':
    app.run(debug=True)
