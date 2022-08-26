from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import first
from rest_framework import status
import base64
import random

from rest_framework.response import Response

from cysecapp5.serializers import User5Serializer

from .models import User5
# Create your views here.
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)

@api_view(['POST'])
def api5_create(request):
    if request.method == 'POST':
        logger.info('Api5 user create started!')

        message = request.data['username'] + request.data['passwd']
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        user = User5.objects.create(
            username=request.data['username'],
            name=request.data['name'],
            passwd=request.data['passwd'],
            auth_token=base64_message,
            user_role=request.data['user_role'],
        )
        user.save()
        all_user_serializer = User5Serializer(user, many=False)
        logger.info('Api5 user create ok!')

        return JsonResponse(all_user_serializer.data, safe=False)
    else:
        logger.info('Api5 user create failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def api5_update_passwd(request, id=None):
    if request.method == 'POST':
        logger.info('Api5 user update password started!')

        user = User5.objects.filter(id=id).update(passwd=request.data['passwd'])
        if user == 1:
            all_user_serializer = User5Serializer(first(User5.objects.filter(id=id)), many=False)
            logger.info('Api5 user update password ok!')

            return JsonResponse(all_user_serializer.data, safe=False)
        logger.info('Api5 user update password failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)





@api_view(['GET'])
def api5_get_by_id(request, id=None):
    logger.info('Api5 user get by id started!')

    auth_token = request.environ.get('HTTP_AUTHORIZATION')
    user = get_object_or_404(User5, id=id, auth_token=auth_token)
    user = User5Serializer(user, many=False)
    if 'Not Found:' not in user:
        logger.info('Api5 user get by id ok!')

        return JsonResponse(user.data, safe=False)


@api_view(['GET'])
def api5_get_all(request):
    logger.info('Api5 user get all started!')

    auth_token = request.environ.get('HTTP_AUTHORIZATION')
    request_user = get_object_or_404(User5, auth_token=auth_token)
    role = request_user.user_role
    if role != 'Admin':
        print("you are trying to do something you don't authorized-->broken-function-level-authorization")
    user = User5.objects.all()
    user = User5Serializer(user, many=True)
    logger.info('Api5 user get all ok!')

    return JsonResponse(user.data, safe=False)
