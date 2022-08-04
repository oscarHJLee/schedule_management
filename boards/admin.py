from django.contrib import admin

from boards.models import Content, Board

admin.site.register([Board, Content])
