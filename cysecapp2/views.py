from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import first
from rest_framework import status
import base64

from rest_framework.response import Response

from cysecapp2.serializers import User2Serializer, User2AuthTokenSerializer

from .models import User2
# Create your views here.
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)


def validate_data_create_api2(request):
    username = request.data['username']
    name = request.data['name']
    passwd = request.data['passwd']
    course = request.data['course']
    logger.info('Api2 user validate started!')

    if not isinstance(username, str) or len(username) < 3:
        logger.info('Api2 validate failed!')

        return False
    elif not isinstance(name, str) or len(name) < 3:
        logger.info('Api2 validate failed!')

        return False
    elif not isinstance(passwd, str) or len(passwd) < 3:
        logger.info('Api2 validate failed!')

        return False
    elif not isinstance(course, str) or len(course) < 3:
        logger.info('Api2 validate failed!')

        return False
    else:
        logger.info('Api2 user validated!')

        return True


@api_view(['POST'])
def api2_create(request):
    if request.method == 'POST':
        validate = validate_data_create_api2(request)
        if validate:
            logger.info('Api2 user started!')
            message = request.data['username'] + request.data['passwd']
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            user = User2.objects.create(
                username=request.data['username'],
                name=request.data['name'],
                passwd=request.data['passwd'],
                course=request.data['course'],
                auth_token=base64_message,
                user_role=request.data['user_role'],

            )
            user.save()
            all_user_serializer = User2Serializer(user, many=False)
            logger.info('Api2 user successful!')

            return JsonResponse(all_user_serializer.data, safe=False)

        else:
            logger.info('Api2 user failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api2_login(request):
    if request.method == 'POST':
        logger.info('Api2 login started!!')

        user = User2.objects.filter(username=request.data['username'], passwd=request.data['passwd'])
        if len(user) == 0:
            logger.info('Api2 login failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
        user = User2AuthTokenSerializer(user, many=True)
        logger.info('Api2 login ok!')

        return JsonResponse(first(user.data), safe=False)


# def api2_get(request, id=None):
@api_view(['GET'])
def api2_get(request):
    if request.method == 'GET':
        logger.info('Api2 get user started!')

        all_users = User2.objects.all()
        auth_token = request.environ.get('HTTP_AUTHORIZATION')
        if User2.objects.filter(auth_token=auth_token).exists():
            a = get_object_or_404(User2, auth_token=auth_token)
            if a.user_role != 'Admin':
                logger.error("you are trying broken user authentication")

            user = User2.objects.all()

            all_user_serializer = User2Serializer(user, many=True)
            logger.info('Api2 get user ok!')

            return JsonResponse(all_user_serializer.data, safe=False)
        else:
            logger.info('Api2 get user failed!')

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
