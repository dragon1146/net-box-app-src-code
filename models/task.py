# this line of code has been removed because it is been replaces by
# the SLQAlchemy module
# import sqlite3
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

    __tablename__ = 'net_box'

    id = db.Column(db.Integer, primary_key=True)
    manufacture = db.Column(db.String)
    device = db.Column(db.String)
    task = db.Column(db.String)
    command = db.Column(db.Text)
    notes = db.Column(db.Text)

    def __init__(self, manufacture, device,  task, command, notes):
      self.task = task
      self.command = command
     
 
    def json(self):
      return {'task':self.task, 'command':self.command}    
      
    # by using SQLAlchemy, there is no need to have 2 different
    # functions to do inserts and updates
    # this single function will perform both inserting of new data
    # and updating existing data
    # this is called "upserting"
    def save_to_db(self):
        
        # the code below will be taking the data from the body of the
        # POST request which is in a json format and convert it into
        # a SQLAlchemy object
        # it will then take that object and convert it into a row
        # input for the table in the database
        db.session.add(self)
        db.session.commit()


        # connection = sqlite3.connect('toolbox.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO networking_toolbox VALUES (?,?)"
        # cursor.execute(query, (self.task, self.command))

        # connection.commit()
        # connection.close()
    
    @classmethod
    def find_by_name(cls, task):

        # this code below is the equivalent of the following code
          # query = "SELECT * FROM networking_toolbox WHERE task=?"
          # result = cursor.execute(query, (task,))
        # it will search the table and return an object containing
        # the first result of the query
        return cls.query.filter_by(task=task).first


        # connection = sqlite3.connect('toolbox.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM networking_toolbox WHERE task=?"
        # result = cursor.execute(query, (task,))
        # row = result.fetchone()
        # connection.close()

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