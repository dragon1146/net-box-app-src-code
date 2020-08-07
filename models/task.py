import sqlite3



class TaskModel:
    def __init__(self, task, command):
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