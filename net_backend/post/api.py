from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import PostForm
from .serializers import PostSerializer
from .models import Post

from accounts.models import User
from accounts.serializers import UserSerializer

# Create your views here.
@api_view(['Get'])
# this view here is for getting all the post in the database 
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)# in this fields we use many=true since we have more than one objects
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])# ensuring that the information fetched back is for the user own profile
def post_list_profile(request, id):
    user = User.objects.get(pk=id)
    posts = Post.objects.filter(created_by_id=id)
    user_serializer = UserSerializer(user)
    posts_serializer = PostSerializer(posts, many=True)
    return JsonResponse({
        'posts':posts_serializer.data,
        'user':user_serializer.data 
    }, safe=False)
    



@api_view(['POST'])
# This view here is for creating apost in the frontend and passing it in 
# in the backend 
def post_create(request):
    form = PostForm(request.data)
    
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()
        
        serializer = PostSerializer(post)
        
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'add something here later!....'})
 
    
    
    
    