from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .forms import SignupForm
from .models import User, FriendlyRequest
from.serializers import UserSerializer,FriendlyRequestSerializer

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
    })

#The below authentication allow us to accesss
# the signup view even if you are not authenticated since they are empty
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'
    form = SignupForm({
        
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    if form.is_valid():
        form.save()
        # send verification email later!
    else:
        message = 'error'    
    
    return JsonResponse({'message': message})



#deals with acceptance of the freindly request 
@api_view(['GET'])
def friends(request, pk):
    user = User.objects.get(pk=pk) #i think this is the id of the user whom the request is from 
    
    requests = []
    
    if user == request.user:
        requests = FriendlyRequest.objects.filter(created_for=request.user, status=FriendlyRequest.SENT)
        # by adding this line of code  {status=FriendlyRequest.SENT} after the user has accepted the request that request will 
        # will be removed completely 
        requests = FriendlyRequestSerializer(requests, many=True)
        requests = requests.data
    friends = user.friends.all()
    
    return JsonResponse({
        
        'user': UserSerializer(user).data,
        'friends': UserSerializer(friends, many=True).data,
        'requests': requests
        
    }, safe=False)


#api view for sending the friendly request
#here we are using the user id to send him the request for him to accept 
@api_view(['POST'])
def friendly_request(request, pk):
    user = User.objects.get(pk=pk)
    # getting the user id which the request is sent to him for him to accept it 
    
    check1 = FriendlyRequest.objects.filter(created_for=request.user).filter(created_by=user)
    check2 = FriendlyRequest.objects.filter(created_for=user).filter(created_by=request.user)
    
    if not check1 or not check2:
        FriendlyRequest.objects.create(created_for=user,created_by=request.user)
        return JsonResponse({'message': 'Request sent'}) 
    else:
        return JsonResponse({'message': 'request already sent '})



@api_view(['POST']) # here we are handling the the acceptance or the rejection of the friendly ruquest 
def handle_request(request, pk, status):
    #here we are using the user id to who the request is from 
    user = User.objects.get(pk=pk)
    friendlyrequest = FriendlyRequest.objects.filter(created_for=request.user).get(created_by=user)
    friendlyrequest.status = status
    friendlyrequest.save()
    
    user.friends.add(request.user)
    user.friends_count = user.friends_count + 1
    user.save()
    
    request_user = request.user
    request_user.friends_count = request_user.friends_count + 1
    request_user.save()
    
    return JsonResponse({'message':'Friendly request updated'})
    
    
        