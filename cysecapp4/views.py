from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import first
from rest_framework import status
import base64
import random

from rest_framework.response import Response

from cysecapp4.serializers import User4Serializer, User4AuthTokenSerializer, User4OtpSerializer, User4StateSerializer

from .models import User4
# Create your views here.
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
def api4_create(request):
    if request.method == 'POST':
        logger.info('Api4 user create started!')

        message = request.data['username'] + request.data['passwd']
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        user = User4.objects.create(
            username=request.data['username'],
            name=request.data['name'],
            passwd=request.data['passwd'],
            auth_token=base64_message,
            try_count=0
        )
        user.save()
        all_user_serializer = User4Serializer(user, many=False)
        logger.info('Api4 user create ok!')

        return JsonResponse(all_user_serializer.data, safe=False)
    else:
        logger.info('Api4 user create failed!')
        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api4_get(request):
    logger.info('Api4 user get started!')

    all_users = User4.objects.all()
    auth_token = request.environ.get('HTTP_AUTHORIZATION')
    print(auth_token)
    if User4.objects.filter(auth_token=auth_token).exists():
        user = User4.objects.filter(auth_token=auth_token)
        state = User4StateSerializer(user, many=True)
        if first(state.data)['state'] == 1:
            all_user_serializer = User4Serializer(user, many=True)
            logger.info('Api4 user get ok!')

            return JsonResponse(all_user_serializer.data, safe=False)
        else:
            logger.info('Api4 user get failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
    else:
        logger.info('Api4 user get failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api4_login(request):
    logger.info('Api4 user login started!')

    if request.method == 'POST':
        user = User4.objects.filter(username=request.data['username'], passwd=request.data['passwd'])
        if len(user) == 0:
            logger.info('Api4 user auth_token failed otp sent failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
        auth_token = User4AuthTokenSerializer(user, many=True)
        create_otp(request.data['username'])
        logger.info('Api4 user auth_token returned otp sent')

        return JsonResponse(first(auth_token.data), safe=False)


@api_view(['POST'])
def api4_otp(request):
    logger.info('Api4 user create started!')

    auth_token = request.environ.get('HTTP_AUTHORIZATION')
    user = User4.objects.filter(auth_token=auth_token)
    user = first(user)
    user = User4OtpSerializer(user, many=False)
    otp = request.data['otp']
    if otp == user.data['otp']:
        logger.info('Api4 user create started!')

        update_state_login(user.data['username'])
        print(user.data['username'])
        return JsonResponse({"status": "200", "message": "Login successful"}, safe=False)
    logger.info('Api4 user create started!')
    user = get_object_or_404(User4, auth_token=auth_token)
    try_count = user.try_count
    if try_count > 4:
        print("you are trying brute force for lack of resource and rate limitting ")
    User4.objects.filter(auth_token=auth_token).update(try_count=try_count + 1)

    return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api4_logout(request):
    logger.info('Api4 user logout started!')
    print("kjzhjkhz")
    auth_token = request.environ.get('HTTP_AUTHORIZATION')
    user = get_object_or_404(User4, auth_token=auth_token)
    user = User4OtpSerializer(user, many=False)
    user = user.data['username']
    update_state_logout(user)
    logger.info('Api4 user logout ok!')

    return JsonResponse({"status": "200", "message": "Logout successful"}, safe=False)


def create_otp(username):
    x = random.randint(0, 15)
    user = User4.objects.filter(username=username).update(otp=x)


def update_state_login(username):
    user = User4.objects.filter(username=username).update(state=1)
    user = User4.objects.filter(username=username).update(try_count=0)



def update_state_logout(username):
    user = User4.objects.filter(username=username).update(state=0)
