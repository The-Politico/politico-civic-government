"""
Use this file to configure pluggable app settings and resolve defaults
with any overrides set in project settings.
"""

from django.conf import settings as project_settings


class Settings:
    pass


Settings.API_AUTHENTICATION_CLASS = getattr(
    project_settings,
    'GOVERNMENT_API_AUTHENTICATION_CLASS',
    'rest_framework.authentication.BasicAuthentication'
)

Settings.API_PERMISSION_CLASS = getattr(
    project_settings,
    'GOVERNMENT_API_PERMISSION_CLASS',
    'rest_framework.permissions.IsAdminUser'
)

Settings.API_PAGINATION_CLASS = getattr(
    project_settings,
    'GOVERNMENT_API_PAGINATION_CLASS',
    'government.pagination.ResultsPagination'
)

settings = Settings
