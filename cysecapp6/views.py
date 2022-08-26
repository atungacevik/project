from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import first
from rest_framework import status
import base64
import random

from rest_framework.response import Response

from cysecapp6.serializers import User6Serializer

from .models import User6
# Create your views here.
from rest_framework.decorators import api_view

import logging

logger = logging.getLogger(__name__)


@api_view(['POST'])
def api6_create(request):
    logger.info('Api6 user create started!')

    if request.method == 'POST':
        if 'credit' in request.data:
            credit = request.data['credit']
            logger.error("you are trying to mass assignment")
        else:
            credit = 0

        user = User6.objects.create(
            username=request.data['username'],
            name=request.data['name'],
            passwd=request.data['passwd'],
            credit=credit

        )
        user.save()
        all_user_serializer = User6Serializer(user, many=False)
        logger.info('Api6 user create ok!')

        return JsonResponse(all_user_serializer.data, safe=False)
    else:
        logger.info('Api6 user create failed!')

        return JsonResponse({"status": "400", "message": "Failed Request"}, safe=False,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api6_get_by_id(request, id=None):
    logger.info('Api6 user get by id started!')

    auth_token = request.environ.get('HTTP_AUTHORIZATION')
    user = get_object_or_404(User6, id=id)
    user = User6Serializer(user, many=False)
    if 'Not Found:' not in user:
        logger.info('Api6 get by id failed!')

        return JsonResponse(user.data, safe=False)
