import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class APIRootView(APIView):
    """
    API root for the Hype API. Lists the available endpoints.
    """

    def get(self, request, format=None):
        message_dump = {
            'message': 'You are here: API Root.'
        }
        data = json.dumps(message_dump)
        return Response(data, content_type='application/json')


class APISignUpView(APIView):
    """
    API endpoint to create a user. Authenticates the client and
    generates auth token.
    """

    def get(self, request, format=None):
        message_dump = {
            'message': 'POST client credentials to register.'
        }
        data = json.dumps(message_dump)
        return Response(data, content_type='application/json')

    def post(self, request, format=None):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            message = 'Credentials already exist. Use APISignInView to authenticate.'
            token = 'None'
        else:
            newremote = User.objects.create_user(username, None, password)
            newremote.save()
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                message = 'New remote client added and authenticated.'
                authtoken = Token.objects.get_or_create(user=user)
                token = authtoken[0].key

        message_dump = {
            'message': message,
            'token': token
        }
        data = json.dumps(message_dump)
        return Response(data, content_type='application/json')


class APISignInView(APIView):
    """
    API endpoint to authenticate a remote client and generate auth token.
    """

    def get(self, request, format=None):
        message_dump = {
            'message': 'POST client credentials to authenticate.'
        }
        data = json.dumps(message_dump)
        return Response(data, content_type='application/json')

    def post(self, request, format=None):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                message = 'Remote client authenticated.'
                authtoken = Token.objects.get_or_create(user=user)
                token = authtoken[0].key
        else:
            message = 'Login credentials not found. Sign upusing APISignUpView endpoint.'
            token = 'None'

        message_dump = {
            'message': message,
            'token': token
        }
        data = json.dumps(message_dump)
        return Response(data, content_type='application/json')
