from django.urls import path
from .views import BankListView, BranchByIFSCView, BranchesByBankCity

urlpatterns = [
    path("banks/", BankListView.as_view(), name="bank-list"),
    path("branches/", BranchesByBankCity.as_view(), name="branch-by-bank-city"),
    path("branches/<str:ifsc>/", BranchByIFSCView.as_view(), name="branch-by-ifsc"),
]
