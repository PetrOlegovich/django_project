from django.http import HttpResponse
from random import choice, randint
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Succsess')
    return HttpResponse('Привет мир !!!')


def game_1(request):
    answer = choice(['орел', 'решка'])
    logger.info(f'ответ = {answer}')
    return HttpResponse(answer)

def game_2(request):
    answer = randint(1, 6)
    logger.info(f'ответ = {answer}')
    return HttpResponse(answer)

def game_3(request):
    answer = randint(0, 100)
    logger.info(f'ответ = {answer}')
    return HttpResponse(answer)