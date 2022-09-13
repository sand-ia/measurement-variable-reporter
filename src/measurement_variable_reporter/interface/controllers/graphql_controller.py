from flask import Blueprint, request, Response
from json import dumps
import graphene


class Query(graphene.ObjectType):
    query = graphene.String(name=graphene.String(default_value="World"))

    def resolve_hello(self, info, name):
        return "Hello " + name


schema = graphene.Schema(query=Query)


graphql_controller = Blueprint("graphql_controller", __name__)


@graphql_controller.route("/graphql", methods=["POST"])
def graphql():

    query = json.loads(request.data)["query"]
    try:
        result = schema.execute(query).data
    except Exception as error:
        print(error)

    response = dumps(result)
    return Response(response, mimetype="application/json", status=200)
