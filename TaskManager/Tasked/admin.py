from django.contrib import admin
from .models import Project, Task, Tag

# Регистрация модели Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для отображения в списке
    search_fields = ('name',)  # Поля для поиска

# Регистрация модели Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'created_at')  # Поля для отображения
    list_filter = ('created_at',)  # Фильтры справа
    search_fields = ('name', 'description')  # Поля для поиска
    filter_horizontal = ('members',)  # Горизонтальный виджет для many-to-many поля

# Регистрация модели Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'assignee', 'due_date', 'project')  # Поля для отображения
    list_filter = ('status', 'priority', 'due_date', 'project', 'tags')  # Фильтры
    search_fields = ('title', 'description')  # Поля для поиска
    filter_horizontal = ('tags',)  # Горизонтальный виджет для тегов
    date_hierarchy = 'due_date'  # Навигация по датам
    ordering = ('-created_at',)  # Сортировка по умолчанию

    # Опционально: можно добавить поля для отображения на странице редактирования
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project')
        }),
        ('Details', {
            'fields': ('status', 'priority', 'assignee', 'due_date', 'tags')
        }),
    )