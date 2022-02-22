from django.db import models
from django.db.models import TextField


class Category(models.Model):
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE,
                               verbose_name='Üst Kategori')
    name = models.CharField(max_length=250, verbose_name='Başlık')
    description_plaintext = TextField(blank=True, default="", verbose_name='Tanım')

    class_tag = models.CharField(max_length=128, blank=True, null=True, verbose_name='İcon Tag')
    objects = models.Manager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ('Kategoriler')
        verbose_name_plural = ('Kategoriler Liste')
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi'))

class Task(models.Model):
   title = models.CharField(max_length=100,verbose_name='Başlık')
   description = TextField(blank=True, default="", verbose_name='Açıklama')
   category = models.ForeignKey(Category, related_name="gorev_kategori", null=True, on_delete=models.SET_NULL,verbose_name='Kategori')
   completed = models.BooleanField(default=False)

   def _str_(self):
     return self.title

   class Meta:
       verbose_name = ('Görevler')
       verbose_name_plural = ('Görev Liste')
       default_permissions = ()
       permissions = (('liste', 'Listeleme Yetkisi'),
                      ('sil', 'Silme Yetkisi'),
                      ('ekle', 'Ekleme Yetkisi'),
                      ('guncelle', 'Güncelleme Yetkisi'))