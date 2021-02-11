import uuid
from django.db import models

from stdimage.models import StdImageField


def get_file_path(_instance, filename):
  ext = filename.split('.')[-1]
  filename = f'{uuid.uuid4()}.{ext}'
  return filename

class Base(models.Model):
  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)
  active = models.BooleanField(default=True)

  class Meta:
    abstract = True

class Services(Base):
  ICON_CHOICES = (
    ('lni-cog', 'Engrenagem'),
    ('lni-stats-up', 'Gráfico'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
  )

  service = models.CharField(max_length=100)
  description = models.TextField(max_length=200)
  icon = models.CharField(max_length=12, choices=ICON_CHOICES)

  class Meta:
    verbose_name = 'Serviço'
    verbose_name_plural = 'Serviços'

  def __str__(self):
    return self.service

  
class Role(Base):
  role = models.CharField(max_length=100)

  class Meta:
    verbose_name = 'Cargo'
    verbose_name_plural = 'Cargos'

  def __str__(self):
    return self.role  

class Team(Base):
  name = models.CharField(max_length=100)
  role = models.ForeignKey('core.Role', verbose_name='Role', on_delete=models.CASCADE)
  bio = models.TextField(max_length=200)
  image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height':480, 'crop': True}})
  facebook = models.CharField(max_length=100, default='#')
  twitter = models.CharField(max_length=100, default='#')
  instagram = models.CharField(max_length=100, default='#')