from datetime import datetime
from .forms import UserForm
from django.contrib.auth import authenticate, login

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AddForm
from .models import DiaryModel

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def entry(request):
    form = AddForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            note = request.POST['note']
            content = request.POST['content']
            posted_date = datetime.now()
            productivity = request.POST['productivity']
            author = request.user

            todays_diary = DiaryModel()
            todays_diary.note = note
            todays_diary.author = author
            todays_diary.posted_date = posted_date
            todays_diary.content = content
            todays_diary.productivity = productivity

            todays_diary.save()

     
        return HttpResponseRedirect('')

    return render(
        request,
        'entry/add.html',
        {
            'title': 'Eat Write Sleep',
            'subtitle': '잠들기전 하루 마침표를 영어 일기로',
            'add_highlight': True,
            'addform': form,
        }
    )


def show(request):
    diaries = DiaryModel.objects.order_by('posted_date')
    icon = True if len(diaries) == 0 else None
    return render(
        request,
        'entry/show.html',
        {
            'show_highlight': True,
            'title': 'Eat Write Sleep',
            'subtitle': '잠들기전 하루 마침표를 영어 일기로',
            'diaries': reversed(diaries),
            'icon': icon
        }
    )


def detail(request, diary_id):
    diary = get_object_or_404(DiaryModel, pk=diary_id)

    return render(
        request,
        'entry/detail.html',
        {
            'show_highlight': True,
            'title': diary.note,
            'subtitle': diary.posted_date,
            'diary': diary
        }
    )


def productivity(request):
    
    data = DiaryModel.objects.order_by('posted_date')[:10]
    icon = True if len(data) == 0 else None

    return render(
        request,
        'entry/productivity.html',
        {
            'title': '감정 차트',
            'subtitle': '0부터 10까지 본인이 생각한 하루 감정을 축적하여 그래프로 나타냅니다.',
            'data': data,
            'icon': icon
        }
    )
    
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('entry')
    else:
        form = UserForm()
    return render(request, 'entry/signup.html', {'form': form})    

