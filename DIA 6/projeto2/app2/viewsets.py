    # viewsets.py
from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer
import requests
import certifi
class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        if not Country.objects.exists():
            response = requests.get("https://restcountries.com/v3.1/all",verify=certifi.where()  
        )
            if response.status_code == 200:
                for item in response.json():
                    Country.objects.create(
                        name=item.get("name", {}).get("common", ""),
                        capital=item.get("capital", [""])[0],
                        region=item.get("region", ""),
                        population=item.get("population", 0),
                        flag_url=item.get("flags", {}).get("png", "")
                    )
        return Country.objects.all()
