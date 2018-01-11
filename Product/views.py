from django.http import HttpResponse
from .models import Drug,Comment
from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartADDDrugForm
from .forms import CommentForm,ChildCommentForm


def index(request):
    queryset_list = Drug.objects.all().order_by('-id')

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(drug_name__icontains=query) |
            Q(drug_company__icontains=query) |
            Q(drug_usage__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 12)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:

        queryset = paginator.page(1)
    except EmptyPage:

        queryset = paginator.page(paginator.num_pages)

    context = {
        "drugs": queryset,

        "page_request_var": page_request_var,

    }
    return render(request, "product/index.html", context)



def details(request, drug_slug):
    drug = get_object_or_404(Drug, slug= drug_slug)
    cart_drug_form =CartADDDrugForm()
    comments=Comment.objects.filter(drug_slug=drug_slug)
    return render(request, 'product/detail.html', {'drug': drug,'cart_drug_form': cart_drug_form,'comments':comments})



def Add_comment(request):
    if request.method=="POST":
        # age comment parrent dashte bashe be onvane child comment save mishe
        if request.POST['parrent']:
            if request.user.is_authenticated:
                form=ChildCommentForm(request.POST)
                if form.is_valid():
                    post=form.save(commit=False)
                    parrent=Comment.objects.get(pk=request.POST['parrent'])
                    post.parrent=parrent
                    post.user=request.user
                    post.save()
                else:
                    return HttpResponse(form.errors)
        else:
            form=CommentForm(request.POST)
            if form.is_valid():
                post=form.save(commit=False)
                if request.user.is_authenticated:
                    post.user=request.user
                post.save()
            else:
                return HttpResponse(form.errors)
        return redirect(request.POST['redirect'])
    else:
        return HttpResponse('get')

