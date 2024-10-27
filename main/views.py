from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_exempt



@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'main/home.html', {"posts": posts})


@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class SecureDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"data": "This is secure data."})


from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer  # Create a serializer for the User model

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'username': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework import viewsets
from rest_framework.response import Response
from .models import Picture
from .serializers import PictureSerializer
import random
from rest_framework.decorators import action

class RandomPictureView(APIView):
    def get(self, request):
        # Get all pictures
        pictures = list(Picture.objects.all())
        # Select 5 random pictures
        random_pictures = random.sample(pictures, min(len(pictures), 5))

        # Build the response with absolute URLs
        response_data = []
        for picture in random_pictures:
            picture_data = {
                "id": picture.id,
                "description": picture.description,
                "image_url": request.build_absolute_uri(picture.image.url)  # Get the absolute URL
            }
            response_data.append(picture_data)

        return Response(response_data)
    

from django.http import JsonResponse
from rest_framework.views import APIView
from sentence_transformers import SentenceTransformer
import numpy as np

class SentenceSimilarityView(APIView):
    def post(self, request):
        # Get sentences from the request data
        s1 = request.data.get("sentence1")
        s2 = request.data.get("sentence2")

        # Check if both sentences are provided
        if not s1 or not s2:
            return JsonResponse({'error': 'Both sentence1 and sentence2 are required.'}, status=400)

        # Calculate similarity
        similarity_score = self.get_similarity(s1, s2)
        
        # Return the result as JSON
        return JsonResponse({'result': similarity_score})

    def get_similarity(self, s1, s2):
        sentences = [s1, s2]
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        embeddings = model.encode(sentences)

        # Calculate cosine similarity
        similarity = np.dot(embeddings[0], embeddings[1]) / (np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))
        return float(similarity) * 100  # Return percentage



from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserProfileSerializer

class UserProfileView(APIView):
    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        serializer = UserProfileSerializer(profile)
        return Response(serializer.data)
    

class UpdateUserScoreView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        score_type = request.data.get('score_type')  # Should be 'score1', 'score2', or 'score3'
        score_value = request.data.get('score_value')
        print(request.data)

        try:
            # Fetch the user
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)

            # Update the appropriate score
            if score_type == 'score1':
                profile.score1.append(score_value)  # Assuming score1 is a list
            elif score_type == 'score2':
                profile.score2.append(score_value)  # Assuming score2 is a list
            elif score_type == 'score3':
                profile.score3.append(score_value)  # Assuming score3 is a list
            else:
                return Response({'error': 'Invalid score type.'}, status=status.HTTP_400_BAD_REQUEST)

            profile.save()  # Save the updated profile

            return Response({'message': 'Score updated successfully.'}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)