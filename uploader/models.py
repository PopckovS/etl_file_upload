from django.db import models

# ======================================
#   Models for testing document uploader
# ======================================


class TestA(models.Model):
    name = models.CharField(verbose_name='Название', blank=True, null=True, max_length=255)
    count = models.IntegerField(verbose_name='Количество', blank=True, null=True, default=0)
    content = models.TextField(verbose_name='Содержимое', blank=True)

    guid = models.CharField(verbose_name='Номер', max_length=255)

    class Meta:
        db_table = '"public"."test_a"'
        verbose_name = 'Объект A'
        verbose_name_plural = 'Объекты A'


class TestB(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255)
    count = models.IntegerField(blank=True, null=True, default=0)
    content = models.TextField(blank=True)

    time_create = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    time_update = models.DateTimeField(blank=True, null=True, auto_now=True)
    is_published = models.BooleanField(blank=True, null=True, default=True)

    guid = models.CharField(max_length=255)

    class Meta:
        db_table = '"public"."test_b"'
        verbose_name = 'Объект B'
        verbose_name_plural = 'Объекты B'
