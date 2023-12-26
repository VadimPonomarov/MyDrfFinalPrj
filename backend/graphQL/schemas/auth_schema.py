from typing import Type

import graphene
import graphql_jwt
from graphene.types import ResolveInfo
from graphql_jwt.decorators import login_required, staff_member_required

from ..gql_types import UserModel, UserType


class Query(graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    # delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    # delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
