from authapp.models import ShopUser
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm, ProductCategoryCreateForm, ProductCategoryEditForm, ProductCreateForm, \
    ProductEditForm


def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)


def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


def categories(request):
    title = 'админка/категории'

    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


def category_create(request):
    title = 'категории/создание'

    if request.method == 'POST':
        user_form = ProductCategoryCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        user_form = ProductCategoryEditForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/category_update.html', content)


def category_update(request, pk):
    title = 'категории/редактирование'

    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:category_update', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/category_update.html', content)


def category_delete(request, pk):
    title = 'категории/удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        # category.delete()
        # вместо удаления лучше сделаем неактивным
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


def product_create(request, pk):
    title = 'Продукты/создание'

    if request.method == 'POST':
        user_form = ProductCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:products'))
    else:
        user_form = ProductEditForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/product_update.html', content)


def product_read(request, pk):
    title = 'продукты/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/product_read.html', content)


def product_update(request, pk):
    title = 'продукты/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/product_update.html', content)


def product_delete(request, pk):
    title = 'продукты/удаление'

    category = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        # category.delete()
        # вместо удаления лучше сделаем неактивным
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'product_to_delete': category}

    return render(request, 'adminapp/product_delete.html', content)