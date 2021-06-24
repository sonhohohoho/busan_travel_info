from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
# from .models import Question, Answer, Comment
from django.utils import timezone
# from .forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Restaurant, Office


import pandas as pd


def insert(request):
    with open('C:/django/busan_travel_info/부산관광안내소정보.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        axis_zero, axis_one = df.shape
        y = [i for i in range(axis_one)]
        for x in range(axis_zero):
            for j in range(axis_one):
                if str(type(df.iloc[x, y[j]])) != "<class 'str'>":
                    df.iloc[x, y[j]] = str(df.iloc[x, y[j]])
            Office.objects.create(call_number=df.iloc[x, y[1]],
                                  time=df.iloc[x, y[2]],
                                  latitude=df.iloc[x, y[3]],
                                  longitude=df.iloc[x, y[4]],
                                  name=df.iloc[x, y[5]],
                                  address=df.iloc[x, y[6]],
                                  foreign=df.iloc[x, y[7]],
                                  introduction=df.iloc[x, y[8]])

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


def detail(request):
    """
        세부 결과 페이지
    """

    return render(request, 'traveling/detail.html')


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
