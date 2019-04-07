import uuid
from datetime import datetime
from cassandra.cqlengine import columns, ValidationError
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from marshmallow import Schema, fields

class PeopleModel(Model):
    '''
    Model for people resource.
    '''
    __table_name__ = "people"
    connection.setup(["172.17.0.2"], "api_test", protocol_version=3)

    id = columns.UUID(primary_key=True)
    first_name = columns.Text(required=True)
    last_name = columns.Text(required=True, index=True)
    dt_insert = columns.DateTime(required=True)

    def validate(self):
        '''
        Validation method for people model
        :return: None
        '''
        super(PeopleModel, self).validate()
        if len(self.first_name) == 0:
            raise ValidationError("first_name field must be suplied")
        if len(self.last_name) == 0:
            raise ValidationError("last_name field must be suplied")


class PeopleSchema(Schema):
    '''
    Schema to serializing model to json object.
    '''
    id = fields.Str(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    dt_insert = fields.Str()