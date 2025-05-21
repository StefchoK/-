from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Comment

def buy_view(request):
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'buy.html', {'products': products})

def sell_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buy')
    else:
        form = ProductForm()
    return render(request, 'sell.html', {'form': form})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = Comment.objects.filter(product=product)

    if request.method == "POST" and request.user.is_authenticated:
        content = request.POST.get("content")
        if content:
            Comment.objects.create(
                product=product,
                author=request.user,
                content=content
            )
            return redirect('product_detail', pk=pk)

    return render(request, 'product_detail.html', {
        'product': product,
        'comments': comments
    })
