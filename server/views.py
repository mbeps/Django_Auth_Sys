from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer

@api_view(['POST'])
def signup(request: Request) -> Response:
    """Allows the user to sign up for an account.
    If the user is successfully created, the user is saved to the database and a token is created for the user.
    If the user is not successfully created, the errors are returned.

    Args:
        request (Request): The request object from the client to the server containing signup data.

    Returns:
        Response: Response with token and user data if user is successfully created, otherwise errors.
    """
    serializer: UserSerializer = UserSerializer(data=request.data) # initialize serializer with data from request
    if serializer.is_valid(): # check if serializer is valid
        serializer.save() # save serializer to database
        user: User = User.objects.get(username=request.data['username']) # retrieve user from database
        user.set_password(request.data['password']) # set hashed password
        user.save() # save user to database with all fields
        token: Token = Token.objects.create(user=user) # create token for user to use for authentication
        return Response({'token': token.key, 'user': serializer.data}) # return token and user data
    return Response(serializer.errors, status=status.HTTP_200_OK) # return errors if serializer is not valid

@api_view(['POST'])
def login(request: Request) -> Response:
    """Allows the user to login to their account.
    If the user is successfully logged in, a token is created for the user.
    If the user is not successfully logged in, an error is returned.

    Args:
        request (Request): The request object from the client to the server containing login data.

    Returns:
        Response: The response with token and user data if user is successfully logged in, otherwise error.
    """
    user: User = get_object_or_404(User, username=request.data['username']) # retrieve user from database
    if not user.check_password(request.data['password']): # check if password is correct
        # do not give away information about why login failed
        return Response("missing user", status=status.HTTP_404_NOT_FOUND) # return error if password is incorrect
    token, created = Token.objects.get_or_create(user=user) # create token for user to use for authentication
    serializer: UserSerializer = UserSerializer(user) # initialize serializer with user data
    return Response({'token': token.key, 'user': serializer.data}) # return token and user data

@api_view(['GET']) # only allow GET requests
@authentication_classes([SessionAuthentication, TokenAuthentication]) # allow authentication with session and token
@permission_classes([IsAuthenticated]) # only allow authenticated users
def test_token(request: Request) -> Response:
    """Test if the user is authenticated.
    If the user is authenticated, return "passed!".

    Args:
        request (Request): The request object from the client to the server.

    Returns:
        Response: if user is authenticated, return "passed!", otherwise return error.
    """
    return Response("passed!") # return passed if user is authenticated