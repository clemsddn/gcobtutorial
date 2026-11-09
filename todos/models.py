from django.db import models
from django.urls import reverse


class Tache(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    terminee = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_creation']

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('tache-detail', kwargs={'pk': self.pk})