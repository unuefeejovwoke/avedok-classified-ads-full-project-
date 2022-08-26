from math import prod
from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from .models import Product, Category, Brand, Podcast
from django.core.paginator import Paginator
from .forms import AddProductForm, ReviewForm
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    category_list = Category.objects.all()
    podcast = Podcast.objects.all()
    trending_products = Product.objects.filter(isTrending=True)

    context = {
        'category_list':category_list,
        'podcast':podcast,
        'trending_products': trending_products
    }
    return render(request,'product/index.html',context)

def productList(request, category_slug=None):
    category = None
    productList = Product.objects.all() 
    categorytList = Category.objects.annotate( total_products=Count('product')) 
    trending_products = Product.objects.filter(isTrending=True)[:3]
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        productList = productList.filter(category=category)
    
    search_query = request.GET.get('q')
    if search_query:
        productList = productList.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(brand__name__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(category__name__icontains = search_query) 
        )
    
    paginator = Paginator(productList, 2)
    page = request.GET.get('page')
    productList = paginator.get_page(page)
    template ='Product/product_list.html'
    
    context = {'product_list': productList, 'category_list': categorytList, 'category': category, 'trending_products':trending_products,}  
    return render(request, template, context)


def productDetail(request, product_slug):
    
    productDetail = Product.objects.get(slug=product_slug)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.product = productDetail
        review.owner = request.user
        review.save()


        messages.success(request, 'Your review was successfully submitted!')
        return redirect('products:product_detail', product_slug=productDetail.slug)
  
    template = 'Product/product_detail.html'
    context = {'product_detail': productDetail, 'form':form}
    return render(request, template, context)


@login_required
def add_advertise(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        description = request.POST['description']
        brand = request.POST.get('brand','')
        price = request.POST['price']
        
        photo_main = request.FILES['photo_main']
        photo_1 = request.FILES.get('photo_1','')
        photo_2 = request.FILES.get('photo_2','')
        photo_3 = request.FILES.get('photo_3','')
        photo_4 = request.FILES.get('photo_4','')
        photo_5 = request.FILES.get('photo_5','')
        photo_6 = request.FILES.get('photo_5','')

        cat = Category.objects.get(name=category)
        brand = Brand.objects.get(name=brand)
        
        
        try:
            brand = Brand.objects.get(name=brand)
            
        except Brand.DoesNotExist:
            brand = None
      
        

        product = Product(name=name,
                            description=description,
                            category=cat,
                            owner=request.user,
                            brand=brand,
                            price=price,
                            
                            photo_main=photo_main,
                            photo_1=photo_1,
                            photo_2=photo_2,
                            photo_3=photo_3,
                            photo_4=photo_4,
                            photo_5=photo_5,
                            )
        print(product)
        product.save()
        messages.success(request,'you have been post your advertise successfully!')

        return redirect('products:product_list')
        


    categories = Category.objects.all()


    context={
        'categories':categories,
        
    }
    return render(request,'product/post_ad.html',context)
    
def updateAds(request, ads_slug):
    categories = Category.objects.all()
    ads = Product.objects.get(slug=ads_slug)
    form = AddProductForm(instance=ads)

    if request.method == 'POST':
        form = AddProductForm(request.POST,request.FILES, instance=ads)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {'form':form, 'categories':categories}
    return render(request, 'product/post_ad.html', context)

        
def custom_page_not_found_view(request, exception):
    return render(request, "product/404.html", {})