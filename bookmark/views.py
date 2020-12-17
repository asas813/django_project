from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
class BookmarkListView(ListView):  # ListView를 상속받은 클래스형 뷰 생성
    model = Bookmark
    paginate_by = 6  # 한 페이지에 6개의 리스트를 보여줌

class BookmarkCreateView(CreateView):
    model = Bookmark # 어떤 모델의 입력을 받을지 설정
    fields = ['site_name', 'url'] # 어떤 필드들을 입력받을지 설정
    success_url = reverse_lazy('bookmark:list') # 북마크 추가를 완료하고 목록페이지로 이동
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

# 11주차
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']  # 실제로 수정하고자 하는 필드 입력
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    # 제너릭 클래스뷰 안에서는 reverse_lazy() 함수 사용, 삭제 완료하면 리스트로 돌아감
    success_url = reverse_lazy('bookmark:list')