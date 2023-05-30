import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime


'''
Creamos una clase llamada Tarea
Esta clase va a ser nuestro modelo de datos de la tarea (el cual nos servirá
luego para la base de datos)
Esta clase va a almacenar toda la información referente a una tarea
'''
class Tarea(db.Base):
 __tablename__ = "tarea"
 id = Column(Integer, primary_key=True) # Identificador único de cada tarea 
 # no puede haber dos tareas con el mismo id, por eso es primary key
 contenido = Column(String(200), nullable=False) # Contenido de la tarea, un
 # texto de máximo 200 caracteres
 categoria = Column(String(20), nullable=True)
 fecha_limite = Column(String(DateTime), nullable=False)
 hecha = Column(Boolean) # Booleano que indica si una tarea ha sido hecha o no
 def __init__(self, contenido, categoria, fecha_limite, hecha):
    # Recordemos que el id no es necesario crearlo manualmente, lo añade la
    # base de datos automaticamente
    self.contenido = contenido
    self.categoria = categoria
    self.fecha_limite = fecha_limite
    self.hecha = hecha
 def __repr__(self):
    return "Tarea {}: {} ({})".format(self.id, self.contenido, self.categoria, self.fecha_limite, self.hecha)
 def __str__(self):
    return "Tarea {}: {} ({})".format(self.id, self.contenido, self.categoria, self.fecha_limite, self.hecha)