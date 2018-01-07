from django.http import HttpResponse
from .models import Drug
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    queryset_list = Drug.objects.all().order_by('-id')

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(drug_name__icontains=query) |
            Q(drug_company__icontains=query)

        ).distinct()
    paginator = Paginator(queryset_list, 3)
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



def details(request, drug_id):
    drug = get_object_or_404(Drug, pk= drug_id)
    return render(request, 'product/detail.html', {'drug': drug})
