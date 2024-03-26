from django.shortcuts import render
#from django.http import HttpResponse

#D:\python_workspace\ict_ai_class\DjangoExam\mySite\Investar\index\templates\index.html
#inedx.html을 불러오는 함수
def main_view(request):
     return render(request, 'index.html')

