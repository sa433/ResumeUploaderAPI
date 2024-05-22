from rest_framework.response import Response
from myapp.models import Profile
from myapp.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class ProfileView(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mgs':'Resume Upload successfully', 'status':'success', 'candidate':serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def get(self, request):
        candidate = Profile.objects.all()
        ser_data = ProfileSerializer(candidate, many=True)
        return Response({'status':'success', 'candidates':ser_data.data},status=status.HTTP_200_OK)

    def delete(self, request,id=None):
        print("In Delete request")
        try:
            st = Profile.objects.get(id=id)
            st.delete()
            return Response({'status':'Deleted sucessfully'}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'status':'Not exists'}, status=status.HTTP_404_NOT_FOUND)

    def put(self,request, id=None):
        print("In PUT Request")
        try:
            st = Profile.objects.get(id=id)
            ser_data = ProfileSerializer(st, data=request.data, partial=True)
            if ser_data.is_valid():
                ser_data.save()
                return Response({'status':'Data Updated'}, status=status.HTTP_200_OK)
            return Response(ser_data.errors)
        except Profile.DoesNotExist:
            return Response({'status':'Not exists'}, status=status.HTTP_404_NOT_FOUND)
