from django.http import HttpResponse, Http404
from django.shortcuts import render

# Données temporaires : elles viendront de la base de données plus tard
STUDENTS = [
    {"id": 1, "first_name": "Awa", "last_name": "Diop",
     "classe": "L1", "active": True},
    {"id": 2, "first_name": "Moussa", "last_name": "Fall",
     "classe": "L2", "active": True},
    {"id": 3, "first_name": "Fatou", "last_name": "Ndiaye",
     "classe": "L1", "active": False},
    {"id": 4, "first_name": "Ibrahima", "last_name": "Sow",
     "classe": "L3", "active": True},
]


def home(request):
    context = {
        "school_name": "Lycée d'Excellence de Dakar",
        "nb_classes": 12,
    }
    return render(request, "students/home.html", context)


def student_list(request):
    context = {"students": STUDENTS}
    return render(request, "students/student_list.html", context)


def student_detail(request, id):
    for student in STUDENTS:
        if student["id"] == id:
            context = {"student": student}
            return render(request, "students/student_detail.html", context)
    raise Http404("Étudiant introuvable")