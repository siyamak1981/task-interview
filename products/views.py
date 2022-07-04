from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer,RateSerializer
from .models import Product, Rate
from rest_framework.permissions import IsAuthenticated
from django.db.models import Avg, Count


class ProductsView(APIView):

    permission_classes = [IsAuthenticated,]
    def get(self,request):

        products=Product.objects.all()

        ser_data=ProductSerializer(instance=products, many=True).data
        ser_list=[]
        for i in ser_data:
            ser_list.append(dict(i))

        for i in ser_list:
            id=i['id']
            rate=Rate.objects.filter(product=Product.objects.get(id=id) , user=request.user)
            if rate.exists():
                rate=rate.values('ratenum')[0]['ratenum']
                i.update({'you_rate':rate})

        for i in ser_list:
            agrrate = Product.objects.filter(id=i['id']).aggregate(average_rate=Avg('rate__ratenum'),count_rate=Count('rate__ratenum'))

            i.update(agrrate)

        return Response(ser_list)


class ProductDetailView(APIView):

    permission_classes = [IsAuthenticated,]
    def get(self,request,id):
        product=Product.objects.get(id=id)
        ser_data=ProductSerializer(instance=product).data
        agrrate=Product.objects.filter(id=id).aggregate(average_rate=Avg('rate__ratenum'),count_rate=Count('rate__ratenum'))
        rate = Rate.objects.filter(product_id=id, user=request.user)
        ser_data.update(agrrate)
        if rate.exists():
            rate = rate.values('ratenum')[0]['ratenum']
            ser_data.update({'you_rate': rate})
        return Response(ser_data)


class RateView(APIView):

    def post(self,request,id):
        rate = Rate.objects.filter(product_id=id, user=request.user)
        if rate.exists():
            ser_data=RateSerializer(instance=rate,data=request.data, partial=True)
            if ser_data.is_valid():
                rate.ratenum=ser_data.validated_data['ratenum']
                rate.save()
                return Response('your rate to this product updated!')
        else:
            print("this is a test:{ser_data}")

            ser_data=RateSerializer(data=request.data)
            if ser_data.is_valid():
                Rate.objects.create(product=Product.objects.get(id=id) , user=request.user, ratenum=ser_data.validated_data['ratenum'])
                return Response('your rate has been saved!')