from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication


from .models import Server, Stats, Vote, Section, Post, OnlineUser
from rest_framework import viewsets, generics
from .serializers import ServerSerializer, StatsSerializer, VoteSerializer, SectionSerializer, PostSerializer, OnlineUserSerializer

# Create your views here.


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class ActiveUserList(generics.ListAPIView):
    serializer_class = OnlineUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        return OnlineUser.objects.filter(last_activity__isnull=False)


class ServerViewSet(viewsets.ModelViewSet):
    serializer_class = ServerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Server.objects.all()


class StatsViewSet(viewsets.ModelViewSet):
    serializer_class = StatsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly, )
    queryset = Stats.objects.all()


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Vote.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Section.objects.all()
