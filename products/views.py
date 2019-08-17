from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import Product
from django.utils import timezone
# Create your views here.
def home(request):
    products = Product.objects
    return render(request, 'products/home.html',{'products':products})

@login_required
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.POST['pub_date'] and request.FILES['image'] and request.POST['votes_total'] and request.POST['comments'] and request.POST['username']:
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = "http://" + request.POST['url']
            product.pub_date = timezone.datetime.now()
            product.image = request.FILES['image']
            product.votes_total = request.POST['votes_total']
            product.comments = request.POST['comments']
            product.username = request.user  
            product.save()
            return redirect('/products/' + str(product.id))         
        else:
            return render(request, 'products/create.html', {'error':'Warning : Please fill all of the fields'})
    else:
        return render(request, 'products/create.html')


def details(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'products/details.html', {'product':product})

@login_required
def upvotes(request,product_id):
    if request.method=='POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total +=1
        product.save()
        return redirect('/products/' + str(product.id))         
    