from django.contrib import admin
from .models import TestA, TestB
from utils.utils import owncloud_document_download, download_document
import tempfile
import os


@admin.register(TestA)
class TestAModel(admin.ModelAdmin):
    actions = ['synch_doc_a']

    @admin.action(description='Синхронизация owncloud с БД')
    def synch_doc_a(self, request, queryset):
        with tempfile.TemporaryDirectory() as tmp_dir:

            file = 'test.xlsx'
            src = os.path.join('/home/popkov_sn/Projects/etl_file_upload/src', file)
            dist = os.path.join(tmp_dir, file)

            # doc = owncloud_document_download(tmp_dir)
            doc = download_document(src, dist)
            doc = doc





