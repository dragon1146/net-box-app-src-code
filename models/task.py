import sqlite3
from db import db

# the db.Model was added to the creation of the TaskModel as an
# extention
# this allows the TaskModel to inherite methods from the db.Model
# object
# this will tell the app that we are going to be saving and
# retrieving data from the database using the db.model object

class TaskModel(db.Model):
    # the below code will tell the app the name of the table that
    # will be used to store and retrieve data in the database

    __tablename__ = networking_toolbox
    manufacture = db.column(db.String)
    device = db.column(db.String)
    task = db.column(db.String)
    command = db.column(db.Text)
    notes = db.column(db.Text)

    def __init__(self, manufacture, device,  task, command, notes):
      self.task = task
      self.command = command
     
 
    def json(self):
      return {'task':self.task, 'command':self.command}    
      

    def insert(self):
        connection = sqlite3.connect('toolbox.db')
        cursor = connection.cursor()

        query = "INSERT INTO networking_toolbox VALUES (?,?)"
        cursor.execute(query, (self.task, self.command))

        connection.commit()
        connection.close()
    
    @classmethod
    def find_by_name(cls, task):
        connection = sqlite3.connect('toolbox.db')
        cursor = connection.cursor()

        query = "SELECT * FROM networking_toolbox WHERE task=?"
        result = cursor.execute(query, (task,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row)
    




# class TaskModel:
#     def __init__(self, task, command):
#       self.task = task
#       self.command = command
     
 
#     def json(self):
#       return {'task':self.task, 'command':self.command}    
      

#     def insert(self):
#         connection = sqlite3.connect('toolbox.db')
#         cursor = connection.cursor()

#         query = "INSERT INTO networking_toolbox VALUES (?,?)"
#         cursor.execute(query, (self.task, self.command))

#         connection.commit()
#         connection.close()
    
#     @classmethod
#     def find_by_name(cls, task):
#         connection = sqlite3.connect('toolbox.db')
#         cursor = connection.cursor()

#         query = "SELECT * FROM networking_toolbox WHERE task=?"
#         result = cursor.execute(query, (task,))
#         row = result.fetchone()
#         connection.close()

#         if row:
#             return cls(*row)