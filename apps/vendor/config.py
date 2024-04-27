from djchoices import ChoiceItem, DjangoChoices


class PurchaseOrderChoices(DjangoChoices):
    """Choices for Purchase Orders"""

    pending = ChoiceItem("pending", "Pending")
    completed = ChoiceItem("completed", "Completed")
    cancelled = ChoiceItem("cancelled", "Cancelled")
