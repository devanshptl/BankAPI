from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer


class BankListView(generics.ListAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BranchByIFSCView(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = "ifsc"


# Parameters: bank_name and city in Postman
class BranchesByBankCity(APIView):
    def get(self, request):
        bank_name = request.GET.get("bank_name")
        city = request.GET.get("city")

        if not bank_name or not city:
            return Response({"error": "bank_name and city are required"}, status=400)

        branches = Branch.objects.filter(
            bank__name__icontains=bank_name, city__iexact=city
        )
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data)
