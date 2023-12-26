from .user_schema import Mutation as UsersMutationSchema
from .user_schema import Query as UsersQuerySchema
from .auth_schema import Mutation as AuthMutationSchema

SchemaQueryAll = [UsersQuerySchema, ]
SchemaMutationAll = [UsersMutationSchema, AuthMutationSchema]
