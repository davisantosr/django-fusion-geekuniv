from django.contrib import admin

from .models import Role, Services, Team

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
  list_display = ('role', 'active', 'updated')

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
  list_display = ('service', 'icon', 'active', 'updated')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
  list_display = ('name', 'role')