from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
# from .models import Question, Answer, Comment
from django.utils import timezone
# from .forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
