from django.views import View
import requests
from django.shortcuts import render
from django.conf import settings

class HomeView(View):

    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        try:
            data = None
            if 'location' in request.GET:
                location = request.GET['location']
                url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={settings.OPENWEATHER_API_KEY}'
                response = requests.get(url)
                data = response.json()
            return render(request, self.template_name, {'data': data})
        except Exception as e:
            print(e)
            return render(request, "error.html")
