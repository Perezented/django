from django.shortcuts import render

# Create your views here.
from .models import Question


# def index(request):
#     return HttpResponse('Hello, world. You\'re at the polls index.')


# Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_quesiton_list': latest_question_list}
    return render(request, 'polls/index.html', context)
