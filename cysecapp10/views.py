from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import first
from rest_framework import status
import base64

from rest_framework.response import Response

from cysecapp10.serializers import User10Serializer

from .models import User10
# Create your views here.
from rest_framework.decorators import api_view



def validate_data_create_api10(request):
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
def api10_create(request):
    if request.method == 'POST':

        validate = validate_data_create_api10(request)
        if validate:
            message = request.data['username'] + request.data['passwd']
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            user = User10.objects.create(
                username=request.data['username'],
                name=request.data['name'],
                passwd=request.data['passwd'],
                course=request.data['course'],
                auth_token=base64_message

            )
            user.save()
            all_user_serializer = User10Serializer(user, many=False)
            return JsonResponse(all_user_serializer.data, safe=False)
        else:
            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api2_login(request):
    if request.method == 'POST':

        user = User10.objects.filter(username=request.data['username'], passwd=request.data['passwd'])
        if len(user) == 0:

            return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                                status=status.HTTP_400_BAD_REQUEST)
        user = User10Serializer(user, many=True)

        return JsonResponse(first(user.data), safe=False)
