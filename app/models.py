from django.db import models

class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=50)
    detalhes = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    imagem = models.ImageField(upload_to='carros/')

    class Meta:
        ordering = ['modelo']

    def __str__(self):
        return f'{self.modelo} ({self.cor})'

    def get_absolute_url(self):
        return reverse('app:detalhe', args=[self.pk])
