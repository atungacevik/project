from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import first
from rest_framework import status
import base64
from django.shortcuts import render, get_object_or_404

from rest_framework.response import Response

from cysecapp9.serializers import User9Serializer, User9AuthTokenSerializer

from .models import User9
# Create your views here.
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)

def validate_data_create_api9(request):
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
def api9_create(request):
    if request.method == 'POST':
        validate = validate_data_create_api9(request)
        if validate:
            message = request.data['username'] + request.data['passwd']
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            user = User9.objects.create(
                username=request.data['username'],
                name=request.data['name'],
                passwd=request.data['passwd'],
                course=request.data['course'],
                auth_token=base64_message

            )
            user.save()
            all_user_serializer = User9Serializer(user, many=False)
            return JsonResponse(all_user_serializer.data, safe=False)
        else:
            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api9_login(request):
    if request.method == 'POST':
        username = request.data['username']
        passwd = request.data['passwd']
        user = get_object_or_404(User9, username=username, passwd=passwd)
        if user is None:
            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)

        user = User9AuthTokenSerializer(user, many=False)
        return JsonResponse(user.data, safe=False)


@api_view(['POST'])
def api9_v2_login(request):
    if request.method == 'POST':
        username = request.data['username']
        passwd = request.data['passwd']
        count = 0
        user = get_object_or_404(User9, username=username)
        if user is not None:
            user = User9.objects.filter(username=username, passwd=passwd)

        else:
            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
        if len(user) == 0:
            user = get_object_or_404(User9, username=username)
            count = user.fail_count
            User9.objects.filter(username=username).update(fail_count=count + 1)

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(User9, username=username)
        count = user.fail_count
        if count > 4:
            return JsonResponse({"status": "403", "message": "TRY COUNT EXCEED"}, safe=False,
                                status=status.HTTP_403_FORBIDDEN)

        User9.objects.filter(username=username).update(fail_count=0)
        user = User9AuthTokenSerializer(user, many=False)
        return JsonResponse(user.data, safe=False)


# def api9_get(request, id=None):
@api_view(['GET'])
def api9_get(request):
    if request.method == 'GET':
        username = request.data['username']
        passwd = request.data['passwd']
        print(username, passwd)
        user = User9.objects.raw("""SELECT * FROM users WHERE
username = '%s' AND password = '%s'""" % (username, passwd))
        all_user_serializer = User9Serializer(user, many=True)
        return JsonResponse(all_user_serializer.data, safe=False)
    else:
        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)
