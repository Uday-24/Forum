from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import Author

@receiver(post_save, sender=User)
def create_author_on_signup(sender, instance, created, **kwargs):
    if created:  # Ensures it runs only on new User creation
        base_slug = slugify(instance.get_full_name()) or f"user-{instance.id}"
        slug = base_slug
        counter = 1
        while Author.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        Author.objects.create(user=instance, fullname=instance.get_full_name(), slug=slug)

@receiver(post_save, sender=User)
def save_author_profile(sender, instance, **kwargs):
    if hasattr(instance, "author"):  # Check if an Author profile exists
        instance.author.save()
