from flask import Flask,jsonify
from src.robot.robot import robot_main
app = Flask(__name__)

@app.route('/<cpf>')
def show_user_profile(cpf):
    resultado = robot_main(cpf)
    return jsonify({"dados":resultado.splitlines()})

if __name__ == '__main__':
    app.run(debug=True)