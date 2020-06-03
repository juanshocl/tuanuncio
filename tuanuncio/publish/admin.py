from django.contrib import admin
from django.contrib.auth.models import User
from publish.models import advertisement, region, comuna, NameSocialNetworks, social_networks, typeA


# Register your models here.

@admin.register(advertisement)
class advertisementAdmin(admin.ModelAdmin):
    #list_display = ()
    list_display = ('User', 
               'name',
               'id',
               'Type_advertisement',
               'description',
               'comuna',
               'whatsapp',
               'show_phones',
               'email',
               'url_website',
               'address',
               'show_adress', 
               'Userfacebook',
               'UserInstagram',
               'UserTwitter',
               'state')

@admin.register(region)
class regionAdmin(admin.ModelAdmin):
    list_display = ()
@admin.register(comuna)
class comunaAdmin(admin.ModelAdmin):
    list_display = ()
@admin.register(NameSocialNetworks)
class NameSocialNetworksAdmin(admin.ModelAdmin):
    list_display = ()
@admin.register(social_networks)
class social_networksAdmin(admin.ModelAdmin):
    list_display = ()
@admin.register(typeA)
class typeAAdmin(admin.ModelAdmin):
    list_display = ()

