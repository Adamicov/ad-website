from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from core.create_ad_form import AdForm
from django.utils.timezone import now
from core.models import Ad
from django.core.paginator import Paginator


def home_view(request, *args, **kwargs):
    ads_list = Ad.objects.all()
    paginator = Paginator(ads_list, 25)
    
    page = request.GET.get('page')
    ads = paginator.get_page(page)
    return render(request, 'index.html', {'ads': ads})


def ad_detail_view(request, ad_id):
    user = request.user
    ad = Ad.objects.get(id=ad_id)
    is_owner = False
    if ad in user.ad_set.all():
        is_owner = True
    return render(request, 'ad_detail_view.html', {'ad': ad, 'is_owner': is_owner})


@login_required
def get_user_ads(request):
    user = request.user
    user_ads = list(user.ad_set.all())
    return render(request, 'user_ads.html', {'user_ads': user_ads})


@login_required
def create_ad(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.clean_ad()
            ad.user = request.user
            ad.save()
            return redirect('user_ads')
    else:
        form = AdForm()
    return render(request, 'create_ad.html', {'form': form})


@login_required
def edit_ad(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = edit_ad_values(form, ad)
            ad.save()
            return redirect('user_ads')
    else:
        ad = Ad.objects.get(id=ad_id)
        binded_data = get_ad_data(ad) 
        form = AdForm(data=binded_data)
    return render(request, 'edit_ad.html', {'form': form})

def get_ad_data(ad):
    """Returns a dictionary to bind data to form """
    ad_dict = {}
    ad_dict['title'] = ad.title
    ad_dict['description'] = ad.description
    ad_dict['price'] = ad.price
    return ad_dict

def edit_ad_values(form, ad):
    new_ad = form.clean_ad()
    ad.title = new_ad.title
    ad.description = new_ad.description
    ad.price = new_ad.price
    return ad