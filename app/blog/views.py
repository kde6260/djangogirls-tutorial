from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from os import path

from .models import Post

def post_list(request):
    """

    :param request: HTTP 요청 객체
    :return: name
    """
    # 리전에 맞는 시간 객체 할당
    current_time = timezone.now()

    # 템플릿 로더 (루트/templates 에 위치한 템플릿 파일 로드). 로드된 템플릿은 렌더링 해줘야 한다.
    # config/settings.py 에서 TEMPLATES_DIR 경로를 만들고 TEMPLATE 상수에 경로 명시했음.
    # 템플릿 로더가 get_template()으로 파일을 가져올 때 TEMPLATE 상수에 명시된 경로를 참조한다.
    # 각 애플리케이션에서 templates/을 만들 수도 있다. -> 각 애플리케이션에서 템플릿을 참조하도록 해야.

    # template = loader.get_template('blog/post_list.html')
    # context = {
    #     'name': 'kde'
    # }
    # content = template.render(context, request)
    # return HttpResponse(content)

    posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
    print("type of posts : ", type(posts))

    context = {
        'posts': posts,
    }
    return render(
        request=request,
        context=context,
        template_name='blog/post_list.html',
    )

