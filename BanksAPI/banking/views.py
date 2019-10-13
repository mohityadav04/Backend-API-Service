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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        # using try,except to fail gracefully
        try:
            q = Branches.objects.get(ifsc=kwargs['icode'])
            s = BranchesSerializer(instance=q)
            return response.Response(s.data, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return response.Response(
                "No information for given bank in given city",
                status.HTTP_404_NOT_FOUND
            )


class BankBranchesInCityView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        # Below will take care of duplicate bank record in banks table
        bank_record = Banks.objects.filter(name=kwargs['bname']).first()
        # Get the branches from above bank in the given city
        branches_records = Branches.objects.filter(bank=bank_record, city=kwargs['cityname'])

        # handle pagination
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        paginated_records = paginator.paginate_queryset(branches_records, request)

        # Serialize records
        serialized_records = BranchesSerializer(instance=paginated_records, many=True)
        return response.Response(serialized_records.data, status.HTTP_200_OK)


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
