from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # 지정한 pk와 일치하는 게시글 객체를 가져롬
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    if request.method == "POST": # 글 입력하고 세이브 버튼 누를 시!
        form = PostForm(request.POST) # 입력한 데이터 저장
        if form.is_valid(): # 사용자가 입력한 값이 유효한 데이터인지 확인
            post = form.save(commit=False) # 세이브 함수가 호출된 시점에 바로 저장하지 않음!
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # 저장
            return redirect('blog:post_detail', pk=post.pk) # 저장하고 상세화면으로 넘어감
    else: # "GET"일 경우
        form = PostForm() # 입력 폼 만들기
    return render(request, 'blog/post_edit.html', {'form':form})


def post_edit(request, pk): # url로부터 받은 pk 변수로 몇 번째 글인지 확인
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST": # 세이브 버튼 눌렀을 때
        form = PostForm(request.POST, instance=post) # 변경된 데이터 가져오기
        if form.is_valid(): # 변경된 값이 유효한다면
            post = form.save(commit=False) # 변경 내용 저장 지연
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else: # "GET" 메서드일 때
        form = PostForm(instance=post) # 이전에 있던 데이터를 넣어서 보여줌
    return render(request, 'blog/post_edit.html', {'form':form})

class PostDeleteView(DeleteView):
    model = Post
    # 제너릭 클래스뷰 안에서는 reverse_lazy() 함수 사용, 삭제 완료하면 리스트로 돌아감
    success_url = reverse_lazy('blog:post_list')
