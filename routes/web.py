""" Web Routes """
from masonite.routes import Get, Post
from app.resources.UserResource import UserResource
from api.routes import TokenRoutes, JWTRoutes

ROUTES = [
    Get().route('/', 'WelcomeController@show').name('welcome'),
    UserResource('/api/user').routes(),
    TokenRoutes('/token'),
    JWTRoutes('/jwt'),
]
