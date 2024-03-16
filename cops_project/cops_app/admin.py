from django.contrib import admin
from django import forms
from .models import Case, CustomUser,Notification
from django.contrib.auth.models import Group

class UserDetails(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["username", "user_type", "entry"]}),
        ("More information", {"fields": ["phone", "email","rank"]}),
    ]

    list_display = ["username", "user_type", "entry"]    
    list_filter = ["user_type", "entry"]                           #filtering
    search_fields = ["username"]                                    #search
    list_per_page = 10 




class CaseAdminForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the police field queryset to only show users with user_type 'police'
        self.fields['police'].queryset = self.fields['police'].queryset.filter(user_type='police')


class CaseAdmin(admin.ModelAdmin):
    form = CaseAdminForm
    list_display = ('type', 'date', 'place', 'user', 'police', 'status')
    list_filter = ('status', 'type', 'user', 'police')
    search_fields = ('type', 'place', 'culprit', 'victim', 'user__username', 'police__username')

    # other configurations for CaseAdmin if needed


admin.site.unregister(Group)
admin.site.register(Case, CaseAdmin)
admin.site.register(CustomUser, UserDetails)
# admin.site.register(Notification)

admin.site.site_header= 'Cops On Stream'