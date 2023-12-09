from django.shortcuts import render
from django import template

def custom_view(request):
    predicate_age = request.GET.get('age')
    persons = [{"name": "Oleg", "age": 22, "date": "02.02.1987"},
               {"name": "Vitaliy", "age": 98, "date": "02.02.1931"},
               {"name": "Ivan", "age": 12, "date": "02.02.2009"},
               {"name": "Vsevolod", "age": 58, "date": "02.02.1921"}
               ]

    context = {"persons": persons, "predicate_age": int(predicate_age)}
    return render(
        request,
        "bd_site/index.html",
        context=context,
    )