from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources
from flask_sqlalchemy import SQLAlchemy
import os

api = Api()
# Inicialización de la App
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # variables de entono
    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getenv('DATABASE_PATH')}{os.getenv('DATABASE_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if not os.path.exists(f"{os.getenv('DATABASE_PATH')}{os.getenv('DATABASE_NAME')}"):
        db.create_all()

    api.add_resource(resources.UsuariosRec, '/usuarios')

    api.add_resource(resources.UsuarioRec, '/usuario/<user_id>')

    api.add_resource(resources.UsrsAlumnosRec, '/alumnos')

    api.add_resource(resources.UsrAlumnoRec, '/alumno/<user_id>')

    api.add_resource(resources.UsrProfesorRec, '/profesor/<user_id>')

    api.add_resource(resources.PlanAlumnoRec, '/planificacion/<user_id>')

    api.add_resource(resources.PlanProfesorRec, '/planificacion_profesor/<user_id>')  # noqa: E501

    api.add_resource(resources.PlansProfesoresRec, '/planificaciones_profesores')  # noqa: E501

    api.add_resource(resources.ProfesorClasesRec, '/profesor_clases/<user_id>')

    api.add_resource(resources.PagoRec, '/pago/<user_id>')

    api.add_resource(resources.LoginRec, '/login')
    api.init_app(app)
    return app
