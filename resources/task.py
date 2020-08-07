# import sqlite3
from flask_restful import Resource, reqparse
# from flask_jwt import JWT, jwt_required

from models.task import TaskModel





class Task(Resource):
   
    parser = reqparse.RequestParser()
    parser.add_argument('command',
        # type=string,
        required=True,
        help="this field cannot be left blank"
    )

    # @jwt_required()
    def get(self, task):
        try:
            task = TaskModel.find_by_name(task)
        except:
            return {'message':"there was a problem with SQL while retrieving the item."}, 500
        
        if task:
            return task.json()
        return {'message':"Task not found"}, 404 
    
    def post(self, task):
        if TaskModel.find_by_name(task):
            return {'message':"A task already exist with '{}'".format(task),},400
       
        data = Task.parser.parse_args()
        task = TaskModel(task, data['command'])
        

        try:
            task.insert()
        except:
            return {'message':"an error occurred when inserting that new task"}, 500
        
        return task.json(), 201

  


# class Task(Resource):
   
#     parser = reqparse.RequestParser()
#     parser.add_argument('command',
#         # type=string,
#         required=True,
#         help="this field cannot be left blank"
#     )

#     # @jwt_required()
#     def get(self, task):
#         try:
#             task = TaskModel.find_by_name(task)
#         except:
#             return {'message':"there was a problem with SQL while retrieving the item."}, 500
        
#         if task:
#             return task.json()
#         return {'message':"Task not found"}, 404 
    
#     def post(self, task):
#         if TaskModel.find_by_name(task):
#             return {'message':"A task already exist with '{}'".format(task),},400
       
#         data = Task.parser.parse_args()
#         task = TaskModel(task, data['command'])
        

#         try:
#             task.insert()
#         except:
#             return {'message':"an error occurred when inserting that new task"}, 500
        
#         return task.json(), 201
