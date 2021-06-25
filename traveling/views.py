from typing import ContextManager
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
# from .models import Question, Answer, Comment
from django.utils import timezone
# from .forms import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.db.models import Q
import json

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

    with open('C:/django/busan_travel_info/부산맛집정보.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        for i in range(df.shape[0]):
            c = Content.objects.create(
                name=df.콘텐츠명[i],
                gugun=df.구군[i],
                latitude=df.위도[i],
                longitude=df.경도[i],
                address=df.주소[i],
                call_number=df.연락처[i],
                url=df.홈페이지[i],
                image=df.이미지URL[i],
                detail=df.상세내용[i],
                time=df['운영 및 시간'][i])

            Restaurant.objects.create(
                mainkey=c,
                represent=df.대표메뉴[i]
            )

    with open('C:/django/busan_travel_info/부산명소정보.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        for i in range(df.shape[0]):
            c = Content.objects.create(
                name=df.콘텐츠명[i],
                gugun=df.구군[i],
                latitude=df.위도[i],
                longitude=df.경도[i],
                address=df.주소[i],
                call_number=df.연락처[i],
                url=df.홈페이지[i],
                image=df.이미지URL[i],
                detail=df.상세내용[i],
                time=df['운영 및 시간'][i])

            Attraction.objects.create(
                mainkey=c,
                name=df.콘텐츠명[i],
                title=df.콘텐츠명[i],
                traffic=df.교통정보[i],
                break_time=df.휴무일[i],
                cost=df.이용요금[i],
                amenity=df.편의시설[i]
            )

    with open('C:/django/busan_travel_info/부산쇼핑정보.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)
        for i in range(df.shape[0]):
            c = Content.objects.create(
                name=df.콘텐츠명[i],
                gugun=df.구군[i],
                latitude=df.위도[i],
                longitude=df.경도[i],
                address=df.주소[i],
                call_number=df.연락처[i],
                url=df.홈페이지[i],
                image=df.이미지URL[i],
                detail=df.상세내용[i],
                time=df['운영 및 시간'][i])

            Shopping.objects.create(
                mainkey=c,
                name=df.콘텐츠명[i],
                title=df.콘텐츠명[i],
                traffic=df.교통정보[i],
                break_time=df.휴무일[i],
                amenity=df.편의시설[i],
            )

    with open('C:/django/busan_travel_info/부산축제정보.csv', 'r', encoding='utf-8') as f:
        df = pd.read_csv(f)

        for i in range(df.shape[0]):
            c = Content.objects.create(
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
                title=df.콘텐츠명[i],
                traffic=df.교통정보[i],
                cost=df.이용요금[i],
                amenity=df.편의시설[i],
            )
        return HttpResponse('데이터 삽입 완료')


def index(request):
    """
        로그인 시도
    """

    return render(request, 'traveling/index.html')


def main(request):
    """
        메인페이지
    """

    csv_file = 'C:/django/busan_travel_info/부산맛집정보.csv'
    taste = pd.read_csv(csv_file)
    csv_file = 'C:/django/busan_travel_info/부산축제정보.csv'
    festival = pd.read_csv(csv_file)
    csv_file = 'C:/django/busan_travel_info/부산쇼핑정보.csv'
    shopping = pd.read_csv(csv_file)
    csv_file = 'C:/django/busan_travel_info/부산명소정보.csv'
    travel = pd.read_csv(csv_file)

    df = taste.groupby('구군').count()[['콘텐츠ID']]
    df = df.rename(columns={'콘텐츠ID': '맛집'})

    df1 = festival.groupby('구군').count()[['콘텐츠ID']]
    df1 = df1.rename(columns={'콘텐츠ID': '축제'})

    df2 = travel.groupby('구군').count()[['콘텐츠ID']]
    df2 = df2.rename(columns={'콘텐츠ID': '관광명소'})

    df3 = shopping.groupby('구군').count()[['콘텐츠ID']]
    df3 = df3.rename(columns={'콘텐츠ID': '쇼핑'})

    df = pd.merge(df, df1, on='구군', how='outer')
    df = pd.merge(df, df2, on='구군', how='outer')
    df = pd.merge(df, df3, on='구군', how='outer')

    df = df.fillna(0)

    datasets = list()

    back = ["#3e95cd", "#8e5ea2", "#4287f5", "#23ebbc"]

    i = 0
    for tmp in list(df.columns):
        dt = {
            'data': list(df[tmp]),
            'label': tmp,
            'backgroundColor': back[i]
        }
        datasets.append(dt)
        i += 1

    data = {'labels': list(df.index), 'datasets': datasets}

    data = json.dumps(data)

    print(data)

    context = {'da': data}

    return render(request, 'traveling/main.html', context)


def result(request):
    """
        결과페이지
    """
    gugun_v = request.GET.get('gugun')
    theme_v = request.GET.get('theme')

    if theme_v == '맛집':
        finding = Restaurant.objects.select_related(
            'mainkey').filter(mainkey__gugun=gugun_v)
    elif theme_v == '축제':
        finding = Festival.objects.select_related(
            'mainkey').filter(mainkey__gugun=gugun_v)
    elif theme_v == '관광명소':
        finding = Attraction.objects.select_related(
            'mainkey').filter(mainkey__gugun=gugun_v)
    else:
        finding = Shopping.objects.select_related(
            'mainkey').filter(mainkey__gugun=gugun_v)

    # if theme_v == "맛집":
    #     finding = Content.objects.filter(Q(gugun=gugun_v))
    # else:
    #     return render(request, 'traveling/main.html')
    # tmp = Content.objects.all()[:180]
    context = {'finding': finding, 'gugun': gugun_v, 'theme': theme_v}


#     finding = .objects.filter(Q(gugun=gugun_v))
#     print(finding)
#     return HttpResponse('검색결과')
#  # 네임이 backpack 이거나 가격이 9900원인 것

    return render(request, 'traveling/result.html', context)


def detail(request, c_id):
    """
        세부 결과 페이지
    """

    content = Content.objects.get(id=c_id)

    if content.restaurant_set.all():

        sub = content.restaurant_set.all()[0]
        context = {'content': content, 'rsub': sub}
    elif content.attraction_set.all():
        sub = content.attraction_set.all()[0]
        context = {'content': content, 'asub': sub}
    elif content.shopping_set.all():
        sub = content.shopping_set.all()[0]
        context = {'content': content, 'ssub': sub}
    else:
        sub = content.festival_set.all()[0]
        context = {'content': content, 'fsub': sub}

    return render(request, 'traveling/detail.html', context)


def office(request):
    """
        관광안내소 게시
    """

    return render(request, 'traveling/office_makers.html')


def search(request):
    """ 지역구 및 구군 검색 """
    # kw = request.GET.get('region', 'gugun')  # 검색어
    # if kw:
    #     question_list = question_list.filter(
    #         Q(subject__icontains=kw) |  # 제목검색
    #         Q(content__icontains=kw) |  # 내용검색
    #         Q(author__username__icontains=kw) |  # 질문 글쓴이검색
    #         Q(answer__author__username__icontains=kw)  # 답글 글쓴이검색
    #     ).distinct()

    return render(request, 'traveling/search.html')


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
