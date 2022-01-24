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

    duration_seconds = get_duration(visit)
    flag = True if duration_seconds > minutes*60 else False
    return flag


def storage_information_view(request):
    """Рендерим страницу со всеми незакрытыми визитами"""

    visits = Visit.objects.all()
    current_visits = Visit.objects.filter(leaved_at=None)

    who_entered = [visit.passcard.owner_name for visit in current_visits]
    entered_at = [django.utils.timezone.localtime(visit.entered_at) for visit in current_visits]
    duration = [format_duration(get_duration(visit)) for visit in current_visits]
    long_or_not = [is_visit_long(visit) for visit in current_visits]

    non_closed_visits = []
    for i in range(len(current_visits)):
        curr_employee = {
            'who_entered': who_entered[i],
            'entered_at': entered_at[i],
            'duration': duration[i],
            'is_strange': long_or_not[i]
        }
        non_closed_visits.append(curr_employee)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
