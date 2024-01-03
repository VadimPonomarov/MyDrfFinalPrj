from channels.middleware import BaseMiddleware


class AuthSocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        print('Middleware')
        return await super().__call__(scope, receive, send)
