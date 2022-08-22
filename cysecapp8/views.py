from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first
from rest_framework import status
import base64

from rest_framework.response import Response

from cysecapp8.serializers import User8Serializer, User8AuthTokenSerializer

from .models import User8
# Create your views here.
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)

def validate_data_create_api8(request):
    logger.info('Api8 user create validate started!')

    username = request.data['username']
    name = request.data['name']
    passwd = request.data['passwd']
    course = request.data['course']

    if not isinstance(username, str) or len(username) < 3:
        logger.info('Api8 user create validate failed!')

        return False
    elif not isinstance(name, str) or len(name) < 3:
        logger.info('Api8 user create validate failed!')

        return False
    elif not isinstance(passwd, str) or len(passwd) < 3:
        logger.info('Api8 user create validate failed!')

        return False
    elif not isinstance(course, str) or len(course) < 3:
        logger.info('Api8 user create validate failed!')

        return False
    else:
        logger.info('Api8 user create validate ok!')

        return True


@api_view(['POST'])
def api8_create(request):
    if request.method == 'POST':
        logger.info('Api8 user create started!')

        validate = validate_data_create_api8(request)
        if validate:
            message = request.data['username'] + request.data['passwd']
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            user = User8.objects.create(
                username=request.data['username'],
                name=request.data['name'],
                passwd=request.data['passwd'],
                course=request.data['course'],
                auth_token=base64_message

            )
            user.save()
            all_user_serializer = User8Serializer(user, many=False)
            logger.info('Api8 user create ok!')

            return JsonResponse(all_user_serializer.data, safe=False)
        else:
            logger.info('Api8 user create failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api8_login(request):
    if request.method == 'POST':
        logger.info('Api8 user login started!')

        username = request.data['username']
        passwd = request.data['passwd']

        if username.isalnum() or passwd.isalnum():
            logger.error("you are trying sql injection")

        user = User8.objects.raw("""SELECT * FROM cysecapp8_user8 WHERE
        username = '%s' AND passwd = '%s'""" % (username, passwd))
        if len(user) == 0:
            logger.info('Api8 user login failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
        user = User8AuthTokenSerializer(user, many=True)
        logger.info('Api8 user login ok!')

        return JsonResponse(user.data, safe=False)


# def api8_get(request, id=None):
@api_view(['GET'])
def api8_get(request):
    if request.method == 'GET':
        logger.info('Api8 get user  started!')

        username = request.data['username']
        passwd = request.data['passwd']
        print(username, passwd)
        user = User8.objects.raw("""SELECT * FROM users WHERE
username = '%s' AND password = '%s'"""%(username, passwd))
        all_user_serializer = User8Serializer(user, many=True)
        logger.info('Api8 user get user ok!')

        return JsonResponse(all_user_serializer.data, safe=False)
    else:
        logger.info('Api8 get user failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)

