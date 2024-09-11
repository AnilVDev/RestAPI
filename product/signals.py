from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail 
from .models import Product

@receiver(post_save, sender=Product)
def send_product_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = 'New Product created'
        message = f'A new product has been created:\n\nName:{instance.name}\nPrice:{instance.price}\nColor: {instance.color}'
        from_email = 'our_email@gmail.com'
        recipient_list = ['recipient@gmail.com']
        
        send_mail(subject, message, from_email, recipient_list)