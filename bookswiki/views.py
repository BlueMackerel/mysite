from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.utils import timezone
from .models import Document
from .forms import DocumentForm, DeletedDocumentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q



# Create your views here.

def list(request):
    kw = request.GET.get('kw',
                         '')
    docs_list  =Document.objects.order_by('-id')

    if kw:
        docs_list = docs_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw)  # 내용검색
        ).distinct()
    else:
        docs_list = None
    return render(request, 'bookswiki/list.html', {'docs_list': docs_list})


def index(request):
    """
    대문 출력
    """
    return render(request,'bookswiki/index.html',{})


def showdocs(request,subject:str):

    docs=get_object_or_404(Document,subject=subject)
    context={'document':docs}
    return render(request,'bookswiki/Document.html',context)


from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Document
from .forms import DocumentForm
from django.contrib import messages
@login_required(login_url='accounts:login')
def docscreate(request):
    if request.method == "POST":
        doc_form = DocumentForm(request.POST)

        if doc_form.is_valid():
            subject = doc_form.cleaned_data["subject"]

            # 제목 중복 검사
            if Document.objects.filter(subject=subject).exists():
                messages.error(request,"이미 존재하는 제목입니다.")
            else:
                document = doc_form.save(commit=False)
                data = f"""
                Time:[{timezone.now()}]
                Subject:[{document.subject}]

                Content:
                [{document.content}]
                
                Author:
                [{request.user}]
            
                Comment:

                -create document
                """
                document.modify_date_list = []
                document.modify_date_list.append(data)
                document.save()
                return redirect("bookswiki:detail", subject=document.subject)

    else:
        doc_form = DocumentForm()

    context = {"form": doc_form}
    return render(request, "bookswiki/document_form.html", context)


def showdocsmodify(request,subject:str):

    docs=get_object_or_404(Document,subject=subject)
    context={'document':docs}
    return render(request,'bookswiki/modify_list.html',context)


@login_required(login_url='accounts:login')
def docsmodify(request,subject):
    docs = get_object_or_404(Document,subject=subject)
    if request.method == "POST":
        form = DocumentForm(request.POST, instance=docs)
        if form.is_valid():
            docs = form.save(commit=False)
            data = f"""
            Time:[{timezone.now()}]
            Subject:[{docs.subject}]

            Content:
            [{docs.content}]
            
            Author:
            [{request.user}]


            Comment:

            -modify document


            """
            docs.modify_date_list.append(data) # 수정일시 저장
            docs.save()
            return redirect('bookswiki:detail', subject=docs.subject)
    else:
        form = DocumentForm(instance=docs)
    context = {'form': form}
    return render(request, 'bookswiki/document_form.html', context)

@login_required(login_url='accounts:login')
def docsdelete(request, subject):
    # 주어진 subject로 Document 객체를 검색합니다. 존재하지 않으면 404 에러 발생
    document = get_object_or_404(Document, subject=subject)

    # DeletedDocumentForm 인스턴스를 생성합니다.
    doc_form = DeletedDocumentForm(request.POST)

    # 백업 데이터 생성
    backup_data = f"""
    Time: [{timezone.now()}]
    Subject: [{document.subject}]

    Content:
    [{document.content}]
    
    Deleter:
    [{request.user}]
    
    

    Comment:
    - Create deleted backup of document
    """

    # 백업 문서 인스턴스 생성 (여기서는 DeletedDocumentForm을 사용하여 백업 저장)
    backup_document = DeletedDocumentForm({
        'subject': document.subject,
        'content': document.content,
        'modify_date_list': []  # 백업 데이터를 리스트에 추가
    })

    if backup_document.is_valid():
        # 유효한 경우 백업 저장
        dd=backup_document.save(commit=False)
        dd.modify_date_list = []
        dd.modify_date_list.append(backup_data)
        dd.save()

    # 문서 삭제
    document.delete()
    return redirect('bookswiki:index')  # 삭제 후 리다이렉트