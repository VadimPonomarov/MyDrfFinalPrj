import graphene

from .schemas import SchemaQueryAll, SchemaMutationAll


class Query(*SchemaQueryAll, graphene.ObjectType):
    pass


class Mutation(*SchemaMutationAll, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
