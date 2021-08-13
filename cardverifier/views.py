from django.shortcuts import render
from .serializers import VerifyCardSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import  generics, filters, status
from .services import validate_card_number


class VerifyCardViewset(generics.GenericAPIView):
    serializer_class = VerifyCardSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            data = validate_card_number(request.data['card_number'])

        return Response(data)


def home(request):

    data = {}
    if request.method == "POST":
        number = request.POST.get("number")
        number = number.replace("-", "")
        result = validate_card_number(number)
        data["number"] = number
        data["result"] = result

    return render(
        request,
        'home.html',
        data
    )

