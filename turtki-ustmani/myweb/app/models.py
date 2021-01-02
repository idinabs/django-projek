from django.db import models

class Modelskontak(models.Model):
      name = models.CharField(max_length=255)
      coment = models.TextField()

      def __str__(self):
            return self.name
print(Modelskontak.name)
