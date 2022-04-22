from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import django
import time
from datacenter.storage_information_view import get_duration, format_duration, is_visit_long


def get_employee_visits_info(visit):
    """Получаем информацию визитах: во сколько человек зашел в хранилище,
    как долго и допустимо ли долго находился"""

    return {
            'entered_at': django.utils.timezone.localtime(visit.entered_at),
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
    }


def passcard_info_view(request, passcode):
    """Рендерим страницу всех посещений конкретного человека"""

    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard_id=passcard)
    this_passcard_visits = [get_employee_visits_info(visit) for visit in visits]

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
