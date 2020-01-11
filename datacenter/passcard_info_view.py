from datacenter.models import Passcard, Visit, format_duration, check_visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    not_fromated_this_passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in not_fromated_this_passcard_visits:
        duration = visit.get_duration()
        this_visit = {
            "entered_at": visit.entered_at,
            "duration": format_duration(duration),
            "is_strange": check_visit(duration),
        }
        this_passcard_visits.append(this_visit)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
