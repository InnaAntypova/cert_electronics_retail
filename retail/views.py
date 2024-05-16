from retail.models import Dealer, Contacts, Products
from rest_framework import generics

from retail.serializers import DealerSerializer, DealerCreateSerializer


class DealerCreateListAPIView(generics.ListCreateAPIView):
    queryset = Dealer.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DealerCreateSerializer
        else:
            return DealerSerializer
