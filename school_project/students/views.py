from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Student



def student_list(request):
    query = request.GET.get("q", "")
    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    context = {"students": students, "query": query}
    return render(request, "students/student_list.html", context)


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    context = {"student": student}
    return render(request, "students/student_detail.html", context)


def students_by_class(request, classe):
    students = Student.objects.filter(classe=classe)
    context = {"students": students}
    return render(request, "students/student_list.html", context)