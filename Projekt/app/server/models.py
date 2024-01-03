from django.db import models
from app import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in, user_logged_out


class OnlineUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_online_user(sender, instance, created, **kwargs):
    if created:
        OnlineUser.objects.create(user=instance)


@receiver(user_logged_in)
def update_online_user_on_login(sender, request, user, **kwargs):
    online_user = OnlineUser.objects.get(user=user)
    online_user.last_activity = online_user.user.last_login
    online_user.save()


@receiver(user_logged_out)
def update_online_user_on_logout(sender, request, user, **kwargs):
    online_user = OnlineUser.objects.get(user=user)
    online_user.last_activity = None
    online_user.save()


class Server(models.Model):
    server_name = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField(null=True)
    map = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.server_name}'


class Stats(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    player_count = models.IntegerField()
    rank = models.IntegerField()

    def __str__(self):
        return f'{self.server}'


class Vote(models.Model):
    VOTE = {
        "YES": "YES",
        "NO": "NO"
    }
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    user_who_voted = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vote = models.CharField(max_length=255, choices=VOTE)

    def __str__(self):
        return f'{self.user_who_voted} - {self.vote} '


class Section(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    server_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.server} - {self.server_owner} '


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.section} - {self.user} - {self.title}'
