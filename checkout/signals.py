from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

# This code is copied in its whole from the CI boutique ado project


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
