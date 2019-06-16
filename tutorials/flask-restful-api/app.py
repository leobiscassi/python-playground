from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.category import CategoryResource
from resources.comment import CommentResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

api.add_resource(Hello, '/Hello')
api.add_resource(CategoryResource, '/Category')
api.add_resource(CommentResource, '/Comment')