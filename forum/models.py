from django.db import models
from django.db.models.fields import related
from django.utils import timezone
from django.utils.text import slugify
from django.db.utils import IntegrityError

from django.contrib.auth.models import User
import uuid

#class User(models.Model):
#    name = models.CharField(max_length=64, unique=True)
#
#    def __str__(self):
#        return self.name

class BaseModel(models.Model):
    pass
#class Comment(BaseModel):
#    pass

class Post(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    #created_on = models.DateTimeField(default=timezone.now)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, related_name="posts")
    
    post = models.TextField()

    class Meta:
        permissions = [('can_eat_pizzas', 'Can eat pizzas')]
        
    def save(self, *args, **kwargs):
        try:
            if not self.slug:
                post = self.post.split(" ")[:5]
                self.slug = slugify(post)
                
            super().save(*args, **kwargs)
        except IntegrityError:
            self.slug = slugify(self.slug + str(timezone.now()))

            super().save(*args, **kwargs)
