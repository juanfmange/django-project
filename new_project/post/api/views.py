from pip._vendor.requests.models import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from post.api.serializer import PostSerializer
from post.api.permissions import IsAdmindOrReadOnly



class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdmindOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()



# class PostViewSet(ViewSet):
#     def list(self,request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(serializer.data)
#
#     def retrieve(self,request,pk: int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)
#
#     def create(self,request):
#         serializer = PostSerializer(data=request.POST)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)





# class PostApiView(APIView):
#     def get(self, request):
#         #posts = Post.objects.all()
#         #posts = [post.title for post in Post.objects.all()]
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK,data=serializer.data)
#
#     def post(self, request):
#         Post.objects.create(title=request.data['title'], description=request.data['description'], age =request.data['age'], name =request.data['name'],email=request.data['email'])
#         return Response(status=status.HTTP_201_CREATED)
        # #return self.get(request)


        # serializer = PostSerializer(data = request.POST)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(status=status.HTTP_200_OK,data=serializer.data)