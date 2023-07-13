from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.http.response import JsonResponse
from .models import User


class UserView(APIView):

    def get_user(self, pk):
        try:
            user = User.objects.get(userId=pk)
            return user
        except:
            return JsonResponse('User does not Exist', safe=False)

    def get(self, response, pk=None):
        if pk:
            data = self.get_user(pk)
            serializer = UserSerializer(data)
        else:
            data = User.objects.all()
            serializer = UserSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse('User created successfully', safe=False)
        return JsonResponse('Failed to add user', safe=False)

    def put(self, request, pk=None):
        user_to_update = User.objects.get(userId=pk)
        serializer = UserSerializer(instance=user_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse('User updated successfully', safe=False)
        return JsonResponse('Failed to update the User')

    def delete(self, request, pk=None):
        user_to_delete = User.objects.get(userId=pk)
        user_to_delete.delete()
        return JsonResponse('User deleted successfully', safe=False)
