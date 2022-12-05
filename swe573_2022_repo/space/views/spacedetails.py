from django.shortcuts import render, get_object_or_404
from space.models import SpaceModel
from django.core.paginator import Paginator
from quiz.models import QuizModel

def spacedetails(request, slug): 
    space=get_object_or_404(SpaceModel, slug=slug)
    messages=space.messages.all().order_by('-id')
    steps=space.steps.all()
    terms=space.terms.all()
    resources=space.resources.all()
    quizes = QuizModel.objects.filter(space=space)

    page1=request.GET.get('page1', '1')
    page2=request.GET.get('page2', '1')
    paginator1=Paginator(messages,3)
    paginator2=Paginator(resources,3)

    return render(request,'pages/spacedetails.html', context={
        'space':space,
        'messages':paginator1.get_page(page1),
        'steps':steps,
        'terms':terms,
        'resources':paginator2.get_page(page2),
        'quizes': quizes
    })