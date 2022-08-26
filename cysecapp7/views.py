from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import first
import time
from rest_framework import status
import base64
import random

from rest_framework.response import Response
import requests
from cysecapp7.serializers import User7Serializer, User7CookieSerializer, User7AuthTokenSerializer

from .models import User7
# Create your views here.
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def api7_create(request):
    if request.method == 'POST':
        logger.info('Api7 user create started!')

        if 'credit' in request.data:
            credit = request.data['credit']
        else:
            credit = 0

        user = User7.objects.create(
            username=request.data['username'],
            name=request.data['name'],
            passwd=request.data['passwd'],
            credit=credit
        )
        user.save()
        all_user_serializer = User7Serializer(user, many=False)
        logger.info('Api7 user create ok!')

        return JsonResponse(all_user_serializer.data, safe=False)
    else:
        logger.info('Api7 user create failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api7_get_by_id(request, id=None):
    logger.info('Api7 user get by id  started!')

    auth_token = request.environ.get('HTTP_AUTHORIZATION')
    user = get_object_or_404(User7, id=id)
    user = User7Serializer(user, many=False)
    if 'Not Found:' not in user:
        logger.info('Api7 user create ok!')

        return JsonResponse(user.data, safe=False)


@api_view(['POST'])
def api7_login(request):
    logger.info('Api7 user login started!')

    if request.method == 'POST':
        user = User7.objects.filter(username=request.data['username'], passwd=request.data['passwd'])
        if len(user) == 0:
            logger.info('Api7 user login failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)

        User7.objects.filter(username=request.data['username']).update(
            sessionCookie=request.data['username'] + str(round(time.time() * 1000)))
        user = User7.objects.filter(username=request.data['username'])
        user = User7CookieSerializer(user, many=True)
        logger.info('Api7 user login ok!')

        return JsonResponse(first(user.data), safe=False)


@api_view(['GET'])
def api7_auth_token(request):
    if request.method == 'GET':
        logger.info('Api7 user auth_token started!')

        session = request.COOKIES['SESSIONID']
        print(request.headers)
        if 'Origin' not in request.headers:
            user = get_object_or_404(User7, sessionCookie=session)
            print(user)
            User7.objects.filter(sessionCookie=session).update(
                auth_token=str(round(time.time() * 1000)))
            user = User7.objects.filter(sessionCookie=session)
            user = User7AuthTokenSerializer(user, many=True)
            logger.info('Api7 user create auth_token ok!')

            return JsonResponse(first(user.data), safe=False)
        else:
            r = requests.get(request.headers['Origin'])
            logger.error('YOU ARE USING CROSS ORIGIN !')

            logger.info('Api7 user create auth_token cross used!')

            return JsonResponse(r.text, safe=False)

