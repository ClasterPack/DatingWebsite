from django.db.models import TextChoices


class Sex(TextChoices):
    not_selected = '-', "Не выбран"
    women = 'w', "Женский"
    man = 'm', "Мужской"

