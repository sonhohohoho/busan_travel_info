from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
# from .models import Question, Answer, Comment
from django.utils import timezone
# from .forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Office, Content,Attraction,Shopping,Festival


import pandas as pd


def insert(request):
    with open('C:/miniproject/busan_travel_info/부산축제정보.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        
        

        for i in range(df.shape[0]):
            c=Content.objects.create(
                name=df.콘텐츠명[i],
                gugun=df.구군[i],
                latitude=df.위도[i],
                longitude=df.경도[i],
                address=df.주소[i],
                call_number=df.연락처[i],
                url=df.홈페이지[i],
                image=df.이미지URL[i],
                detail=df.상세내용[i],
                time=df['이용요일 및 시간'][i])
            
            Festival.objects.create(
                mainkey=c,
                title = df.콘텐츠명[i],
                traffic = df.교통정보[i],
                cost = df.이용요금[i],
                amenity = df.편의시설[i],
            )




        return HttpResponse('데이터 삽입 완료')


def index(request):
    """
        로그인 시도
    """

    return render(request, 'traveling/login_or_signup.html')


def main(request):
    """
        메인페이지
    """

    return render(request, 'traveling/main.html')


def result(request):
    """
        결과페이지
    """

    return render(request, 'traveling/result.html')


def detail(request, c_id):
    """
        세부 결과 페이지
    """

    content = Content.objects.get(key=c_id)
    
    if content.restaurant_set.all() :

        sub = content.restaurant_set.all()[0]
        context= {'content':content,'rsub':sub}
    elif content.attraction_set.all():
        sub = content.attraction_set.all()[0]
        context={'content':content,'asub':sub}
    elif content.shopping_set.all():
        sub = content.shopping_set.all()[0]
        context={'content':content,'ssub':sub}  
    else:
        sub = content.festival_set.all()[0]
        context={'content':content,'fsub':sub}  
    
    return render(request, 'traveling/detail.html',context)


def office(request):
    """
        관광안내소 게시
    """

    return render(request, 'traveling/office_makers.html')


""" @login_required(login_url='common:login')
def answer_create(request, question_id):
    """
# pybo 답변등록
"""
     question = get_object_or_404(Question, pk=question_id)
     if request.method == "POST":
         form = AnswerForm(request.POST)
         if form.is_valid():
             answer = form.save(commit=False)
             answer.author = request.user
             answer.create_date = timezone.now()
             answer.question = question
             answer.save()
             return redirect('pybo:detail', question_id=question.id)
     else:
         form = AnswerForm()
     context = {'question': question, 'form': form}
     return render(request, 'pybo/question_detail.html', context)


 @login_required(login_url='common:login')
 def question_create(request):
     """
#    pybo 질문등록
"""
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.create_date = timezone.now()
                question.save()
                return redirect('pybo:index')
        else:
            form = QuestionForm()
        context = {'form': form}
        return render(request, 'pybo/question_form.html', context)

        form = QuestionForm()
        return render(request, 'pybo/question_form.html', {'form': form})


    @login_required(login_url='common:login')
    def question_modify(request, question_id):
        """
# pybo 질문수정
"""
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
# pybo 질문삭제
"""
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
# pybo 답변수정
"""
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
# pybo 답변삭제
"""
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id) """

# Create your views here.
