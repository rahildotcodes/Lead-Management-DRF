from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import authentication,permissions,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter



# Create your views here.

class LeadCreateListView(CreateAPIView,ListAPIView):
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    search_fields=['name','email','status','source']
    ordering_fields=['name','added_date']
    filterset_fields=['status','source']

class LeadRetrieveUpdateDeleteView(UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=LeadSerializer
    queryset=Lead.objects.all()
    lookup_url_kwargs="pk"

# class StatusLevelLeadsView(ListAPIView):
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     serializer_class=LeadSerializer
#     def get(self,request,*args,**kwargs):
#         new_leads=Lead.object.filter(status="new")
#         contacted_leads=Lead.object.filter(status="contacted")
#         converted_leads=Lead.object.filter(status="converted")
#         lost_leads=Lead.object.filter(status="lost")

#         result={
#             "new_leads":new_leads,
#             "contacted_leads":contacted_leads,
#             "converted_leads":converted_leads,
#             "lost_leads":lost_leads
#         }
#         return Response(result)