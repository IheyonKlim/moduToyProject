from django.db import models
import json
from django.views import View
from django.http import JsonResponse

class MainView(View):
	def get(self, request):
		return JsonResponse({"Hello":"World"}, status=200)