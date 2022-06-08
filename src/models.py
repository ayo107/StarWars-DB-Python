import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class Usuarios(Base):
    __tablename__ = "usuarios"
    ID = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Apellidos = Column(String(250))
    Direccion = Column(String(250))
    Correo = Column(String(250))
    Nombre_Usuario = Column(String(250))
    FavoritoID = Column(Integer, ForeignKey('favoritos.FavoritoID'))
    


class Personajes(Base):
    __tablename__ = 'Personajes'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    PersonajeID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    Height = Column(Integer)
    Mass = Column (Integer)
    Color_Eye = Column (String(250), nullable=False)
    FavoritoID = Column(Integer, ForeignKey('favoritos.FavoritoID'))
    UsuarioID = Column(Integer, ForeignKey('usuarios.ID'))

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    PlanetaID = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Orbita = Column(String(250))
    Population = Column(String(250), nullable=False)
    Diameter = Column(Integer)
    Gravity = Column(String(250))
    FavoritoID = Column(Integer, ForeignKey('favoritos.FavoritoID'))
    UsuarioID = Column(Integer, ForeignKey('usuarios.ID'))

    class Naves(Base):
        __tablename__ = 'naves'
        NaveID = Column(Integer, primary_key=True)
        Cost = Column(String(250))
        Capacity = Column(String(250))
        Speed = Column (String(250))
        Mass = Column (String(250))
        FavoritoID = Column(Integer, ForeignKey('favoritos.FavoritoID'))
        UsuarioID = Column(Integer, ForeignKey('usuarios.ID'))
        class Favoritos(Base):
            __tablename__ = 'favoritos'
            FavoritoID = Column(Integer, primary_key=True)
            PersonajeID = Column(Integer, ForeignKey('Personajes.PersonajeID'))
            NaveID = Column(Integer, ForeignKey('naves.NaveID'))
            PersonajeID = Column(Integer, ForeignKey('planetas.PlanetaID'))
            UsuarioID = Column(Integer, ForeignKey('usuarios.ID'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')