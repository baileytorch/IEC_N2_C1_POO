from peewee import Model, AutoField, CharField, ForeignKeyField, DateField, IntegerField, BooleanField
from datetime import datetime
from datos.modelos.pais import Pais
from datos.conexion_db import conectar_db

database = conectar_db()

class BaseModel(Model):
    class Meta:
        database = database

class Usuario(BaseModel):
    id_usuario = AutoField()
    rut = CharField(max_length=12,null=True)
    nombre = CharField(max_length=25,null=False)
    apellido = CharField(max_length=25,null=False)
    correo = CharField(max_length=255,null=False)
    pais = ForeignKeyField(Pais,null=True)
    fecha_nacimiento = DateField(null=True)
    genero = IntegerField(null=False)
    fecha_incorporacion = DateField(default=datetime.now(),null=False)
    habilitado = BooleanField(default=True,null=False)
    password = CharField(max_length=72,null=True)

    class Meta:
        table_name = 'usuarios'