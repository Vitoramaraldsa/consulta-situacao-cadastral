from flask import Flask
from src.robot.robot import robot_main

app = Flask(__name__)

@app.route('/<cpf>')
def show_user_profile(cpf):
    resultado = robot_main(cpf)
    return {"teste":resultado}