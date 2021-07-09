# Code for view website with link also -1
# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse("hello harry bhai")
#
# def about(request):
#     return HttpResponse("about harry bhai")
#
# def link(request):
#     return HttpResponse('''<h1> Harry </h1> <a href = "https://www.codewithharry.com/"> sejal link </a> <a href = "https://www.codewithharry.com/"> sejal link </a>''')




#  pipeline for django
# def index(request):
#     return HttpResponse("home")
#
#
# def removepunc(request):
#     return HttpResponse('''remove punc <a href = "http://127.0.0.1:8000"> button </a>''')
#
#
# def capfirst(request):
#     return HttpResponse("capfirst")
#
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
#
# def spaceremove(request):
#     return HttpResponse("spaceremover")
#
#
# def charcount(request):
#     return HttpResponse("charcount")

#     basic of templates
# def index(request):
#     params = {'name':'sejal','place':'gwalior'}
#     return render(request,'index.html',params)




# urls
#     code for starting -1
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', views.index, name='index'),
#     path('about/', views.about, name='about'),
#     path('', views.link, name='link')
# ]


#   pipeline for django
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('removepunc', views.removepunc, name='rempun'),
#     path('capitalizefirt', views.capfirst, name='capfirst'),
#     path('newlineremove', views.newlineremove, name='newlineremove'),
#     path('spaceremove', views.spaceremove, name='spaceremove'),
#     path('charcount', views.charcount, name='charcount')
# ]



# analysefile
<!--<!DOCTYPE html>-->
<!--<html lang="en">-->
<!--<head>-->
<!--    <meta charset="UTF-8">-->
<!--    <title>Analyzing your text</title>-->
<!--</head>-->
<!--<body>-->
<!--<h1>Your analyzed text - {{ purpose }}</h1>-->
<!--<p>-->
<!--<pre> {{analysed_text}} </pre>-->
<!--</p>-->

<!--</body>-->
<!--</html>-->



<!--<!DOCTYPE html>-->
<!--<html lang="en">-->
<!--<head>-->
<!--    <meta charset="UTF-8">-->
<!--    <title>template is working</title>-->
<!--</head>-->
<!--<body>-->
<!--<h1>Welcome to text analyser.Enter your text below</h1>-->
<!--    <textarea name = 'text' style="margin: 0px; width: 1370px; height: 271px;"> </textarea><br>-->
<!--    <input type ="checkbox" name = "removepunc" > Remove Punctuations <br>-->
<!--    <input type ="checkbox" name = "removenumber" > Remove Numbers <br>-->
<!--    <input type ="checkbox" name = "newlineremover" > New line remover <br>-->
<!--    <input type = "checkbox" name = "extraspaceremover"> Extra space remover <br>-->
<!--    <input type = "checkbox" name = "charactercounter" > character counter <br>-->
<!--    <button type="submit"> Analyze text</button>-->