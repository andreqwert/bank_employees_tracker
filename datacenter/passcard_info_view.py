from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import django
import time
from datacenter.storage_information_view import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    """Рендерим страницу всех посещений конкретного человека"""

    # получить пропуск по passcode
    passcard = Passcard.objects.get(passcode=passcode)

    # получить все визиты по пропуску
    visits_person = Visit.objects.filter(passcard_id=passcard)

    entered_at = [django.utils.timezone.localtime(visit.entered_at) for visit in visits_person]
    durations = [format_duration(get_duration(visit)) for visit in visits_person]
    long_or_not = [is_visit_long(visit) for visit in visits_person]

    this_passcard_visits = []
    for visit in range(len(visits_person)):
        curr_employee = {
            'entered_at': entered_at[visit],
            'duration': durations[visit],
            'is_strange': long_or_not[visit]
        }
        this_passcard_visits.append(curr_employee)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
