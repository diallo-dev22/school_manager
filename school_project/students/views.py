from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_classes": 12,
    }
    return render(request, "students/home.html", context)


def student_list(request):
    return HttpResponse("Liste des étudiants")


def student_detail(request, id):
    return HttpResponse(f"Détail de l'étudiant {id}")