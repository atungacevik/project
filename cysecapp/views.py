from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first
from rest_framework import status
import base64
import logging


from rest_framework.response import Response

from cysecapp.serializers import User1Serializer

from .models import User1
# Create your views here.
from rest_framework.decorators import api_view


logger = logging.getLogger(__name__)


def validate_data_create_api1(request):
    username = request.data['username']
    name = request.data['name']
    passwd = request.data['passwd']
    course = request.data['course']

    if not isinstance(username, str) or len(username) < 3:
        return False
    elif not isinstance(name, str) or len(name) < 3:
        return False
    elif not isinstance(passwd, str) or len(passwd) < 3:
        return False
    elif not isinstance(course, str) or len(course) < 3:
        return False
    else:
        return True


@api_view(['POST'])
def api1_create(request):
    if request.method == 'POST':
        logger.info('Api1 user create started!')

        validate = validate_data_create_api1(request)
        if validate:
            message = request.data['username'] + request.data['passwd']
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            user = User1.objects.create(
                username=request.data['username'],
                name=request.data['name'],
                passwd=request.data['passwd'],
                course=request.data['course'],
                auth_token=base64_message

            )
            user.save()
            all_user_serializer = User1Serializer(user, many=False)
            logger.info('Api1 user created!')
            return JsonResponse(all_user_serializer.data, safe=False)
        else:
            logger.info('Api1 create failed!')
            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api1_get(request, id=None):
    if request.method == 'GET':
        logger.info('Api1 user get started!')

        all_users = User1.objects.all()
        auth_token = request.environ.get('HTTP_AUTHORIZATION')
        if User1.objects.filter(auth_token=auth_token).exists():
            if not User1.object.filter(auth_token=auth_token,id=id).exist():
                logger.error("You are trying broken object level authorization")
            user = User1.objects.filter(id=id)
            all_user_serializer = User1Serializer(user, many=True)
            logger.info('Api1 user get successful!')

            return JsonResponse(first(all_user_serializer.data), safe=False)
        else:
            logger.info('Api1 user get failed!')
            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
