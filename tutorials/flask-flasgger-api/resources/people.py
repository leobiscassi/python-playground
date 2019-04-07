from models.people import PeopleModel, PeopleSchema
from flask_restful import Resource, abort
from flask import request

class People(Resource):
    '''
    Interface with people resources.
    '''
    def get(self):
        '''
        Return all persons that are in database
        ---
        tags:
            - people
        summary: Return all the persons that are in database
        description: Return the persons in people list
        responses:
            200:
                schema:
                    id: resource.People.get
                    properties:
                        id:
                            type: string
                        first_name:
                            type: string
                        last_name:
                            type: string
                        dt_insert:
                            type: string
        '''
        people = PeopleModel()
        rows = people.objects.all()
        schema = PeopleSchema(many=True)
        result = schema.dump(rows)

        if not result:
            abort(404, message="0 rows encountered!")

        return result


    def post(self):
        '''
        Create a new person in database
        ---
        operationId: people.post
        tags:
            - people
        summary: Create a new person in the people list
        description: Create a new person in the people list
        parameters:
            - in: body
              name: person
              description: Person to create
              required: True
              schema:
                  type: object
                  properties:
                      first_name:
                          type: string
                          description: First name of person
                      last_name:
                          type: string
                          description: Last name of person
        responses:
            201:
                description: Successfully created person in list
        '''
        data = request.get_json(force=True)
        people = PeopleModel()

        try:
            person = people.create(first_name=data.get('first_name'), last_name=data.get('last_name'))
        except:
            abort(406, message="Verify your data!")

        schema = PeopleSchema()
        result = schema.dump(person)

        return result


    def delete(self):
        '''
        Remove a person from people list.
        ---
        operationId: people.delete
        tags:
            - people
        summary: Remove a person from people list
        description: Remove a person from people list by ID.
        parameters:
            - in: body
              name: person
              description: Person to remove
              required: True
              schema:
                  type: object
                  properties:
                      id:
                          type: string
                          description: ID of the person
        responses:
            200:
                description: Person removed of the list successfully
        '''
        data = request.get_json(force=True)
        people = PeopleModel()

        try:
            people.filter(id=data.get("id")).delete()
        except:
            abort(400, "It's not possible delete this person, check it out!")

        return "Person removed of the list successfully"

