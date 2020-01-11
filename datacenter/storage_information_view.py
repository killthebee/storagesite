from datacenter.models import Visit, format_duration, check_visit
from django.shortcuts import render


def storage_information_view(request):
    continues_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in continues_visits:
        visiter = visit.passcard
        duration = visit.get_duration()
        visit_info = {
                "who_entered": visiter.owner_name,
                "entered_at": visit.entered_at,
                "duration": format_duration(duration),
                "is_strange": check_visit(duration),
                "passcode": visiter.passcode,
            }
        non_closed_visits.append(visit_info)



    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
