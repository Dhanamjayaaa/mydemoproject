from flask import Flask
from flask_restful import Api,Resource


app = Flask(__name__)
api = Api(app)

user_details = {"Adithya": ['Netflix','AmazonPrime','Hotstar'],
                "Prakash": ['Netflix','AmazonPrime','Hotstar','SONYLIV'],
                "Pavan": ['Netflix','AmazonPrime','Hotstar','SONYLIV','Discover'],
                "Rajesh": ['AmazonPrime','JioTV']}




class OttProviders(Resource):
    def get(self): user_details
    def post(self): return "post"
    def put(self): return "put"
    def delete(self): return"delete"
    
api.add_resource(OttProviders,'/ottProviders/')

if __name__== '__main__':
         app.run(debug=True)
                     
