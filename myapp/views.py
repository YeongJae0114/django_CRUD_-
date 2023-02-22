from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from datetime import datetime

def index(request):
    posts = Post.objects.filter().order_by('-date')
    return render(request,'index.html',{'posts':posts})


def modelformcreate(request):
    if request.method == 'POST': #POST 방식으로 요청이 들어왔을 때
        form = PostForm(request.POST) # 입력된 내용들을 form이라는 변수에 저장
        if form.is_valid(): #form이 유효하다면 (정의한 models 필드와 적합하다면)
            form.save() #form 데이터를 DB에 저장한다
            return redirect('index')
    else: #GET방식으로 요청이 들어왔을 때
        form = PostForm()
    return render(request, 'form_create.html', {'form':form})

def detail(request, post_id):
    # post_id 번째 블로그 글을 데이터베이스로부터 갖고와서
    post_detail = get_object_or_404(Post,pk=post_id)
    # post_id 번째 블로그 글을 detail.html로 띄우주는 코드
    return render(request, 'detail.html', {'post_detail':post_detail })

