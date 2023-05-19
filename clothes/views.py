from pstats import Stats, StatsProfile
from django.http import Http404
from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class MenShirtAPIView(APIView):
    def get(self,request,format=None):
        shirts = Men_Shirt.objects.all()
        serializer = MenShirtSerializer(shirts,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MenShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class MenShirtDetailAPIView(APIView):
    def get(self,request,id=None):
        shirts = Men_Shirt.objects.filter(id=id)
        serializer = MenShirtSerializer(shirts,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        shirts = Men_Shirt.objects.get(id=id)
        serializer = MenShirtSerializer(shirts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        shirts = Men_Shirt.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class MenJacketAPIView(APIView):
    def get(self,request,format=None):
        Jacket = Men_Jacket.objects.all()
        serializer = MenJacketSerializer(Jacket,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MenJacketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class MenJacketDetailAPIView(APIView):
    def get(self,request,id=None):
        Jackets = Men_Jacket.objects.filter(id=id)
        serializer = MenJacketSerializer(Jackets,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Jackets = Men_Jacket.objects.get(id=id)
        serializer = MenJacketSerializer(Jackets,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        shirts = Men_Jacket.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MenPantsAPIView(APIView):
    def get(self,request,format=None):
        Pantss = Men_Pants.objects.all()
        serializer = MenPantsSerializer(Pantss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MenPantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class MenPantsDetailAPIView(APIView):
    def get(self,request,id=None):
        Pantss = Men_Pants.objects.filter(id=id)
        serializer = MenPantsSerializer(Pantss,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Pantss = Men_Pants.objects.get(id=id)
        serializer = MenPantsSerializer(Pantss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Men_Pants.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MenJoggersAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Men_Joggers.objects.all()
        serializer = MenJoggersSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = MenJoggersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class MenJoggersDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Men_Joggers.objects.filter(id=id)
        serializer = MenJoggersSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Joggerss = Men_Joggers.objects.get(id=id)
        serializer = MenJoggersSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Men_Joggers.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GlassesAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Glasses.objects.all()
        serializer = GlassesSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = GlassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
class GlassesDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Glasses.objects.filter(id=id)
        serializer = GlassesSerializer(Joggerss,many=True)
        return Response(serializer.data)
    def put(self,request,id=None):
        Joggerss = Glasses.objects.get(id=id)
        serializer = GlassesSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Glasses.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class EarringAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Earring.objects.all()
        serializer = EarringSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = EarringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class EarringDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Earring.objects.filter(id=id)
        serializer = EarringSerializer(Joggerss,many=True)
        return Response(serializer.data)
    def put(self,request,id=None):
        Joggerss = Earring.objects.get(id=id)
        serializer = EarringSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Earring.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class NecklaceAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Necklace.objects.all()
        serializer = NecklaceSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = NecklaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class NecklaceDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Necklace.objects.filter(id=id)
        serializer = NecklaceSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Joggerss = Necklace.objects.get(id=id)
        serializer = NecklaceSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Necklace.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Women_ShirtAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Women_Shirt.objects.all()
        serializer = WomenShirtSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = WomenShirtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class Women_ShirtDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Women_Shirt.objects.filter(id=id)
        serializer = WomenShirtSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Joggerss = Women_Shirt.objects.get(id=id)
        serializer = WomenShirtSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Women_Shirt.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Women_JacketAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Women_Jacket.objects.all()
        serializer = WomenJacketSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = WomenJacketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class Women_JacketDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Women_Jacket.objects.filter(id=id)
        serializer = WomenJacketSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Joggerss = Women_Jacket.objects.get(id=id)
        serializer = WomenJacketSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Women_Jacket.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Women_PantsAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Women_Pants.objects.all()
        serializer = WomenPantsSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = WomenPantsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class Women_PantsDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Women_Pants.objects.filter(id=id)
        serializer = WomenPantsSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Joggerss = Women_Pants.objects.get(id=id)
        serializer = WomenPantsSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Women_Pants.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Women_JoggersAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Women_Joggers.objects.all()
        serializer = WomenJoggersSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = WomenJoggersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class Women_JoggersDetailAPIView(APIView):
    def get(self,request,id=None):
        Joggerss = Women_Joggers.objects.filter(id=id)
        serializer = WomenJoggersSerializer(Joggerss,many=True)
        return Response(serializer.data)
    
    def put(self,request,id=None):
        Joggerss = Women_Joggers.objects.get(id=id)
        serializer = WomenJoggersSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Women_Joggers.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CartAPIView(APIView):
    def get(self,request,format=None):
        Joggerss = Cart.objects.all()
        serializer = CartSerializer(Joggerss,many=True)
        return Response(serializer.data)

    
    def post(self,request,format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    def put(self,request,id=None):
        Joggerss = Cart.objects.get(id=id)
        serializer = CartSerializer(Joggerss,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id=None):
        shirts = Cart.objects.filter(id=id)
        shirts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
