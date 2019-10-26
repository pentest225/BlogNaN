import graphene

import blogApp.schema
import Utilisateurs.schema
import Statistique.schema
import Contacts.schema
import allConfig.schema
class Query(blogApp.schema.Query,
        Utilisateurs.schema.Query,
        Statistique.schema.Query,
        Contacts.schema.Query,
        allConfig.schema.Query,
        graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
class Mutation(blogApp.schema.RelayMutation,graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query,mutation=Mutation)