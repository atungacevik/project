from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import first
from rest_framework import status
import uuid
import base64
import random

from rest_framework.response import Response

from cysecapp3.serializers import User3Serializer, User3FullSerializer
from .models import User3, Comment
# Create your views here.
from rest_framework.decorators import api_view
import logging

logger = logging.getLogger(__name__)

def generate_uuid():
    return uuid.uuid4().hex


@api_view(['POST'])
def api3_create(request):
    if request.method == 'POST':
        logger.info('Api3 user create started!')

        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        user = User3.objects.create(
            username=request.data['username'],
            name=request.data['name'],
            latitude=latitude,
            longitude=longitude,
            deviceId=uuid.uuid4().hex
        )
        user.save()
        all_user_serializer = User3Serializer(user, many=False)
        logger.info('Api3 user create ok!')

        return JsonResponse(all_user_serializer.data, safe=False)
    else:
        logger.info('Api3 user create failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api3_create_comment(request):
    if request.data['username'] is not None and request.data['comment'] is not None:
        logger.info('Api3 create comment started!')

        user = get_object_or_404(User3, username=request.data['username'])
        comment = Comment.objects.create(
            user=user,
            comment=request.data['comment']
        )
        logger.info('Api3 create comment ok!')

        return JsonResponse({"status": "200", "message": "Comment Created"}, safe=False,
                            status=status.HTTP_200_OK)
    else:
        logger.info('Api3 create comment failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api3_get_comments(request):
    logger.info('Api3 create comment started!')

    user_all = Comment.objects.all()
    user_all = User3FullSerializer(user_all, many=True)
    logger.info('Api3 create comment ok!')

    return JsonResponse(user_all.data, safe=False, status=status.HTTP_200_OK)


def api3_otp(request):
    return 0


def api3_logout(request):
    return 0
