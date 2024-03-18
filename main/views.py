from rest_framework.views import APIView, Response
from .serializers import *
from .models import *
from .algorithms import *

ish_xona_r = 70
ish_xona_x =  39.6513963
ish_xona_y = 66.9653502

def check_user(login, password):
    if User.objects.filter(login=login, password=password).exists():
        return True
    return False
class Login(APIView):
    def get(self, r):
        serializer = LoginSerializer(data=r.data)
        if not serializer.is_valid():
            return Response({'error': 1, 'data': serializer.errors})
        if not check_user(serializer.data['login'], serializer.data['password']):
            return Response({'error': 1, 'data': 'user not found'})
        response = UserInfoSerializer(User.objects.get(login=serializer.data['login'], password=serializer.data['password']))
        return Response({'error':0, 'data': response.data})


class Get_Distance(APIView): # get zaprosda distansiyani hisoblab yuboradi lekin ish xonada bulsa ham yangilamaydi/ post zaprosda get zaprosda qiladigan ishni qiladi faqat ish xonada eknaligini ham tekshiradi
    def get(self, r):
        serializer = Get_DistanceSerializer(data=r.data)
        if not serializer.is_valid():
            return Response({'error': 1, 'data': serializer.errors})
        if not check_user(serializer.data['login'], serializer.data['password']):
            return Response({'error': 1, 'data': 'user not found'})
        lon = float(r.POST.get('lon'))
        lat = float(r.POST.get('lat'))
        distance = calculate_distance(lat, lon, ish_xona_x, ish_xona_y)
        return Response({'error': 0, 'distance': distance})

    def post(self, r):
        serializer = Get_DistanceSerializer(data=r.data)
        if not serializer.is_valid():
            return Response({'error': 1, 'data': serializer.errors})
        if not check_user(serializer.data['login'], serializer.data['password']):
            return Response({'error': 1, 'data': 'user not found'})
        lon = float(r.POST.get('lon'))
        lat = float(r.POST.get('lat'))
        distance = calculate_distance(lat, lon, ish_xona_x, ish_xona_y)
        if distance < ish_xona_r:
            user = User.objects.get(login=serializer.data['login'], password=serializer.data['password'])
            user.ishdami = True
            user.save()
        return Response({'error': 0, 'distance': distance})
