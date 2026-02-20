from django.shortcuts import render, get_object_or_404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  # las 5 preguntas más recientes
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)