from datacenter.models import Passcard, Visit
from datetime import datetime
from django.shortcuts import render
import django
import pytz
import time


def format_duration(duration):
    return time.strftime('%H:%M:%S', time.gmtime(duration))


def get_duration(visit):
    """Вычисляем длительность визита"""

    if visit.leaved_at:
        duration = (visit.leaved_at - visit.entered_at).total_seconds()
    else:
        localtime = django.utils.timezone.localtime()
        duration = (localtime - visit.entered_at).total_seconds()
    return duration


def is_visit_long(visit, minutes=60):
    """Выясняем, длительный ли визит (на выходе булева переменная - true/false).
    Визит является длительным, если он больше mintues минут."""

    return get_duration(visit) > minutes*60


def get_current_visit_info(visit):
    """Получаем информацию о совершившем визит: во сколько и допустимо ли долго находился"""
    
    return {
            'who_entered': visit.passcard.owner_name,
            'entered_at': django.utils.timezone.localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
    }



def storage_information_view(request):
    """Рендерим страницу со всеми незакрытыми визитами"""

    visits = Visit.objects.all()
    current_visits = Visit.objects.filter(leaved_at=None)

    context = {
        'non_closed_visits': [get_current_visit_info(visit) for visit in current_visits],
    }
    return render(request, 'storage_information.html', context)
