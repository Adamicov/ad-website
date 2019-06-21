from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from core.create_ad_form import AdForm
from django.utils.timezone import now


def home_view(request, *args, **kwargs):
    return render(request, 'index.html', {})


def ad_detail_view(request, ad_id):
    return render(request, 'ad_detail_view.html')


@login_required
def get_user_ads(request):
    return render(request, 'user_ads.html', {})
    

@login_required
def create_ad(request):
    pass

@login_required
def edit_ad(request):
    form = AdForm(request.session['ad_edit'])
    print(form)
    if request.method == 'POST':
        form = AdForm(request.POST)
    return render(request, 'user_ad_view.html', {'form': form})

@login_required
def get_user_ad(request):
    return render(request, 'user_ad_view.html')

def error_400(request):
    return render(request, 'error_400.html')
