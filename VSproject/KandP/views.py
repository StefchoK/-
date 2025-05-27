from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Comment
from .forms import ProductForm, CommentForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def buy_view(request):
    products = Product.objects.all()
    return render(request, 'buy.html', {'products': products})

@login_required
def sell_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('buy')
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = Comment.objects.filter(product=product)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.product = product
            comment.author = request.user
            comment.save()
            return redirect('product_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'product_detail.html', {
        'product': product, 'comments': comments, 'form': form
    })

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.owner == request.user:
        product.delete()
    return redirect('buy')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('buy')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')