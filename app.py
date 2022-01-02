from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app) #defining our api


#defining our class student
class Student(Resource):
    def get(self,name):   #defining the methods
        return {'student':name}

api.add_resource(Student,'/student/<string:name>')

app.run(port=5000)