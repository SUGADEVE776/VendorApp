from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.vendor.config import PurchaseOrderChoices
from apps.vendor.models import PurchaseOrder


@receiver(post_save, sender=PurchaseOrder)
def update_purchase_order_completion(sender, instance, created, **kwargs):
    if instance.status == PurchaseOrderChoices.completed:
        instance.calculate_ontime_delivery_rate()
        instance.calculate_fulfillment_rate()

    if instance.quality_rating:
        instance.calculate_quality_rating_average()
