from django.shortcuts import render, redirect
from rest_framework.decorators import api_view,permission_classes
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.forms import UserCreationForm
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from Login import models,serializer
from . import serializer


def register(request):
    print(request.headers)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'Login/register.html ', {'form': form})

def index(request):
    return render(request, 'Login/index.html ',)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(username = username, password = password)
    if not user :
        return Response({'error': 'Invalid user'})
    token, _ = Token.objects.get_or_create(user = user)
    return Response({'token': token.key})


@csrf_exempt
@api_view(["GET"])
def test(request):
    username = request.data.get('username')
    data = { username : "Ohh. A valid User"}
    return Response(data)

# 
# class UserProfileViewSet(viewsets.ModelViewSet):
#     """docstring for """
#     serializer_class =serializer.UserProfileSerializer
#     queryset = models.UserProfile.objects.all()
