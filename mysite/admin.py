from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import MainContent, Comment #현재 디렉토리의 models에서 모델을 가져온다

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_date']
    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
        list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
        search_fields = ['author']

admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin) #모델Comment를 관리자페이지에 등록하여 조작