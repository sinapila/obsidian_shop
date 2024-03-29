from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from order_module.models import Order
from .forms import EditUserForm, ChangePasswordForm


# Create your views here.

class UserDashbordPanel(TemplateView):
    template_name = 'user_module/user_dashbord.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        now_user = User.objects.filter(id=request.user.id).first()
        edit_user_form = EditUserForm(instance=now_user)
        return render(request, 'user_module/edit_profile_page.html', {
            'form': edit_user_form,
            'now': now_user
        })

    def post(self, request: HttpRequest):
        now_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditUserForm(request.POST, request.FILES, instance=now_user)
        return render(request, 'user_module/edit_profile_page.html', {
            'form': edit_form,
            'now': now_user
        })


class ChangePassworldPage(View):
    def get(self, request: HttpRequest):
        form = ChangePasswordForm()
        return render(request, 'user_module/change_passworld_page.html', {'form': form})

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        now_user: User = User.objects.filter(id=request.user.id).first()

        if form.is_valid():
            if form.cleaned_data.get('password') == form.cleaned_data.get('confirm_password'):
                if now_user.check_password(form.cleaned_data.get('password')):
                    now_user.set_password(form.cleaned_data.get('password'))
                    now_user.save()
                    logout(request)
                    return redirect(reverse('login page'))
                else:
                    form.add_error('password', 'کلمه عبور وارد شده اشتباه میباشد')

        else:
            form.add_error('password', 'خطایی ناشناخته روی داد')


def user_basket(request: HttpRequest):

    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)

    total_amount = 0
    for order_detail in current_order.orderdetail_set.all():
        total_amount += order_detail.product.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_module/user_basket.html', context)
