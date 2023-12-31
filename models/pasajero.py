from config.db import db, ma, app


class Pasajero(db.Model):
    __tablename__ = "tbl_pasajero"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    correo_electronico = db.Column(db.String(100))
    telefono = db.Column(db.String(10))
    direccion = db.Column(db.String(100))

    def __init__(
        self,
        nombre,
        apellido,
        correo_electronico,
        telefono,
        direccion,
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.direccion = direccion


with app.app_context():
    db.create_all()


class PasajeroSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "nombre",
            "apellido",
            "correo_electronico",
            "telefono",
            "direccion",
        )
