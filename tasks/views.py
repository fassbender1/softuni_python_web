

# Create your views here.

# from django.http import HttpResponse
# from django.shortcuts import render
# from tasks.models import Task
#
# # def index(request):
# #     tasks_list = Task.objects.all()
# #     output = "; ".join(f"{t.title}: {t.text}"
# #                        for t in tasks_list)
# #     if not output:
# #         output = "There are no created tasks!"
# #     return HttpResponse(output)
#
# def index(request):
#  return render(request, 'tasks/index.html')

from django.shortcuts import render
from tasks.models import Task

def index(request):
    tasks_list = Task.objects.all()
    context = {'tasks_list': tasks_list, 'is_completed': bool}
    return render(request, 'tasks/index.html', context)