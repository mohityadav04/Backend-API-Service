from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Banks, Branches
from .serializers import BanksSerializer, BranchesSerializer
from rest_framework import (response, status, permissions)
from rest_framework.settings import api_settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User
import json
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


class BranchDetailView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        # using try,except to fail gracefully
        try:
            ifsc_requested = request.GET.get('ifsc')
            q = Branches.objects.get(ifsc=ifsc_requested)
            s = BranchesSerializer(instance=q)
            return response.Response(s.data, status.HTTP_200_OK)
        except (KeyError, ObjectDoesNotExist):
            return response.Response(
                "No information for given bank in given city",
                status.HTTP_404_NOT_FOUND
            )


class BankBranchesInCityView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        try:
            bank_requested = request.GET.get('bank')
            city_requested = request.GET.get('city')
            # Below will take care of duplicate bank record in banks table, because bank name is not a primary key
            bank_record = Banks.objects.filter(name=bank_requested).first()
            # Get the branches from above bank in the given city
            branches_records = Branches.objects.filter(bank=bank_record, city=city_requested)

            # handle pagination
            pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
            paginator = pagination_class()
            paginated_records = paginator.paginate_queryset(branches_records, request)

            # Serialize records
            serialized_records = BranchesSerializer(instance=paginated_records, many=True)
            return response.Response(serialized_records.data, status.HTTP_200_OK)
        except KeyError:
            return response.Response(
                "No information for given bank in given city",
                status.HTTP_404_NOT_FOUND
            )


@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(View):

    def post(self, request):
        user_details = json.loads(request.body)
        u = User.objects.create_user(
            username=user_details['username'],
            password=user_details['password']
        )
        u.save()
        return HttpResponse("Welcome! Account Created.")
