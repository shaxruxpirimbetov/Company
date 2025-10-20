from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .funcs import check_phone
from .serializers import OrderSerializer
from .models import Order


class OrderView(LoginRequiredMixin, View):
	login_url = "/user/login/"
	def get(self, request):
		order_id = request.GET.get("order_id")
		if order_id:
			order = Order.objects.filter(id=order_id).first()
			if not order:
				return render(request, "orders/orders.html", {"error": "Order not found"})
			order = OrderSerializer(order).data
			return render(request, "orders/order-view.html", {"order": order})
		
		orders = Order.objects.filter(user=request.user).all()
		orders = OrderSerializer(orders, many=True).data
		return render(request, "orders/orders.html", {"orders": orders})


class CreateOrderView(LoginRequiredMixin, View):
	login_url = "/user/login/"
	def get(self, request):
		return render(request, "orders/order-form.html")
	
	def post(self, request):
		title = request.POST.get("title")
		description = request.POST.get("description")
		phone = request.POST.get("phone")
		
		if not all([title, description, phone]):
			return render(request, "orders/order-form.html", {"error": "Заполните все поли"})
		
		phone_status = check_phone(phone)
		if not phone_status["status"]:
			return render(request, "orders/order-form.html", {"error": phone_status["message"]})
		
		order = Order.objects.create(user=request.user, title=title, description=description, phone=phone)
		return redirect("main:home")


