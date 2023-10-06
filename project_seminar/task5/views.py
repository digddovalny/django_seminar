import logging
import random

from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def one(request):
    logger.info('Frist page Startted')
    answer = ['Орел', 'Решка']
    i = random.randint(0, 1)
    return HttpResponse(f'{answer[i]}')


def two(request):
    logger.info('second page Startted')
    answer = random.randint(1, 6)
    return HttpResponse(f'{answer}')


def three(request):
    logger.info('third page Startted')
    answer = random.randint(1, 100)
    return HttpResponse(f'{answer}')
