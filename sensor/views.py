from django.shortcuts import render
from django.utils import timezone
from .models import Temperature,Humidity

# Create your views here.

def sensor(request):
	sensor1 = Temperature.objects.order_by('-id')[:5]
	sensor2 = Humidity.objects.order_by('-id')[:5]
	temperature = Temperature.objects.latest('Date_and_Time')
	humidity = Humidity.objects.latest('Date_and_Time')
	return render(request, 'sensor/sensor.html', {'sensor1':sensor1,'sensor2':sensor2,'temperature': temperature,'humidity':humidity})


