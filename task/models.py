from django.db import models
#
#
# class Category(models.Model):
#     parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE,
#                                verbose_name=_('Üst Kategori'))
#     name = models.CharField(max_length=250, verbose_name=_('Başlık'))
#     description_plaintext = TextField(blank=True, default="", verbose_name=_('Tanım'))
#
#     class_tag = models.CharField(max_length=128, blank=True, null=True, verbose_name=_('İcon Tag'))
#     objects = models.Manager()
#
#     def __str__(self) -> str:
#         return self.name
#
#
#     class Meta:
#         verbose_name = _('Kategoriler')
#         verbose_name_plural = _('Kategoriler Liste')
#         default_permissions = ()
#         permissions = ((_('liste'), _('Listeleme Yetkisi')),
#                        (_('sil'), _('Silme Yetkisi')),
#                        (_('ekle'), _('Ekleme Yetkisi')),
#                        (_('guncelle'), _('Güncelleme Yetkisi')))
# class Task(models.Model):
#     category =
class Task(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   completed = models.BooleanField(default=False)

   def _str_(self):
     return self.title