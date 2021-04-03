from django.contrib import admin
from .models import Candidate, Position


# Register your models here.
# @admin.register(Candidate)
class AdminCandidate(admin.ModelAdmin):
    readonly_fields = ['votes']

    class Meta:
        model = Candidate


admin.site.register(Candidate, AdminCandidate)
admin.site.register(Position)