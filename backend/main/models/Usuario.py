from .. import db
from sqlalchemy import Float

class Usuario(db.Model):
    __tablename__ = 'usuario'

    dni = db.Column(db.Integer, primary_key=True, autoincrement=False)
    nombre = db.Column(db.String(50), nullable=False, default=lambda: str(Usuario.dni))
    apellido = db.Column(db.String(50), nullable=False, default=lambda: str(Usuario.dni))
    email = db.Column(db.String(50), nullable=False, unique=True)
    fecha_nacimiento = db.Column(db.Date, nullable=True)
    estado = db.Column(db.Boolean, nullable=False, default=False)
    rol = db.Column(db.String(10), nullable=False)
    nombre_usuario = db.Column(db.String(50), db.ForeignKey('usuario_contrasegna.nombre_usuario'))
    altura = db.Column(Float, nullable=True)
    peso = db.Column(Float, nullable=True)
    contrasegna= db.Column(db.String(50), nullable=False)

    # Definimos la relación uno a uno con la tabla Alumno
    alumno = db.relationship('Alumno', back_populates='usuario', uselist=False)
    profesor = db.relationship('Profesor', back_populates='usuario', uselist=False)
    #usuario_contrasegna = db.relationship('Usuario_Contrasegna', back_populates='usuario', uselist=False)
    usuario_pagos = db.relationship('Pagos', back_populates='pagos_usuario',cascade='all, delete-orphan', single_parent=True)
    login1= db.relationship('Login_usuario', back_populates='login_usuario_contrasegna',uselist=False)
   




# class Usuario(db.Model):
#     __tablename__ = 'usuario'

#     dni = db.Column(db.Integer, primary_key=True, autoincrement=False)
#     nombre = db.Column(db.String(50), nullable=False, default=lambda: str(Usuario.dni))
#     apellido = db.Column(db.String(50), nullable=False, default=lambda: str(Usuario.dni))
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     fecha_nacimiento = db.Column(db.Date, nullable=True)
#     estado = db.Column(db.Boolean, nullable=False, default=False)
#     # Recordar que para crear la contraseña necesitamos llamar al método crear_contraseña para que compute el hash y lo almacene
#     rol = db.Column(db.String(10), nullable=False)
#     nombre_usuario = db.Column(db.String(50), db.ForeignKey('usuario_contrasegna.nombre_usuario'))
#     altura = db.Column(Float, nullable=True)
#     peso = db.Column(Float, nullable=True)

#     #   ** RELACIONES de Usuario
#     usuario_alumno = db.relationship('Alumno', uselist=False, back_populates='alumno_usuario', single_parent=True)
#     usuario_profesor = db.relationship('Profesor', uselist=False, back_populates='profesor_usuario',  single_parent=True)
#     usuario_usuario_contrasegna = db.relationship('Usuario_Contrasegna', uselist=False, back_populates='usuario_contrasegna_usuario')
#     usuario_pagos = db.relationship('Pagos', uselist=False, back_populates='pagos_usuario')
#     # Valor por defecto alumno

    def __init__(self, **kwargs):
        super(Usuario, self).__init__(**kwargs)
        if self.rol is None:
            self.rol = 'alumno'

    def establecer_rol(self, rol):
        if rol not in ['alumno', 'profesor', 'admin']:
            raise ValueError('Rol inválido')
        self.rol = rol

    def __repr__(self):
        return f'<Usuario: {self.nombre} {self.apellido} {self.estado}>'

    def to_json(self):

        usuario_json = {
            'dni': self.dni,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'fecha_nacimiento': self.fecha_nacimiento,
            'estado': self.estado,
            'rol': self.rol,
            'nombre_usuario': self.nombre_usuario,
            'altura': self.altura,
            'peso': self.peso
        }
        return usuario_json

    @staticmethod
    def from_json(usuario_json):
        dni = usuario_json.get('dni')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        fecha_nacimiento = usuario_json.get('fecha_nacimiento')
        estado = usuario_json.get('estado')
        rol = usuario_json.get('rol')
        nombre_usuario = usuario_json.get('nombre_usuario')
        altura = usuario_json.get('altura')
        peso = usuario_json.get('peso')

        return Usuario(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            estado=estado,
            rol=rol,
            nombre_usuario=nombre_usuario,
            altura=altura,
            peso=peso,
        )
