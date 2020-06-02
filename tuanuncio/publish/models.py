from django.db import models



import uuid

# Create your models here.

class region(models.Model):
    Codregion = models.CharField(max_length=2, default=None, primary_key=True)
    RegionName = models.CharField(max_length=50, default=None)
    
    def __str__(self):
        return self.RegionName
    
class comuna(models.Model):
    CodComuna = models.IntegerField(primary_key=True, default=None)
    Reg = models.ForeignKey(region, on_delete=models.CASCADE)
    ComunaName = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.ComunaName
class NameSocialNetworks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    NameDescriptions = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.NameDescriptions

class social_networks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_socialNetwork = models.CharField(max_length=50)
    red = models.ManyToManyField(NameSocialNetworks, default=None)
    
    def __str__(self):
        return self.user_socialNetwork

class credits(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_recharge = models.TimeField
    amount = models.IntegerField()
    time_recharge = models.TimeField(auto_now=False, auto_now_add=False, default=None)
    #advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.amount)

class phones(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    typePhone = models.CharField(max_length=50)
    Number = models.CharField(max_length=12)
    wsp = models.BooleanField
    #advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.Number


class typeA(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50)
    #advertisement_id = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.description

class subscription_plan(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=50)
    amount = models.IntegerField
    valid_from = models.DateField(auto_now=True, auto_now_add=False)
    valid_to = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.description

class advertisement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default = None, max_length=50)
    Type_advertisement = models.ForeignKey(typeA, on_delete=models.CASCADE, default=None)
    description  = models.CharField(max_length=200, default=None)    
    Social_network = models.ManyToManyField(social_networks, default=None)
    comuna = models.ForeignKey(comuna, on_delete=models.CASCADE, default = None)
    #phones = models.ManyToManyField(phones, default=None)
    whatsapp = models.CharField(max_length=11, default=None)
    show_phones = models.BooleanField(default=False)
    email = models.EmailField(max_length=254, default=None)                
    url_website = models.URLField(max_length=200, default=None)
    address = models.CharField(max_length=200, default=None)
    #latitude_longitude = models.CharField(max_length=200, default=None)
    show_adress = models.BooleanField(default=False)
    #image = models.ImageField(upload_to='static/img', default=None)
    #logo  = models.ImageField(upload_to='static/img/logo', default=None)
    incorporation_date = models.DateField(auto_now=True)
    #subscription_type = models.ForeignKey(subscription_plan, on_delete=models.CASCADE, default=None)
    state = models.BooleanField(default=True)
    #includes_maps  = models.BooleanField(default=False)
    #credits_id     = models.ForeignKey(credits, on_delete=models.CASCADE, default=None)
    #price_from = models.IntegerField(default=0)
    #price_to = models.IntegerField(default=0) 

    def __str__(self):
        return self.name

    def get_socialNetwork(self):
        return self.Social_network.name
        # return ', '.join([s.name for s in self.Social_network_set.all()])
    
    get_socialNetwork.shot_description = 'Redes Sociales'

HOUR_OF_DAY_24 = [(i,i) for i in range(1,25)]

WEEKDAYS = [
    (1, ("Lunes")),
    (2, ("Martes")),
    (3, ("Miercoles")),
    (4, ("Jueves")),
    (5, ("Viernes")),
    (6, ("Sabado")),
    (7, ("Domingo")),
]

class OpeningHours(models.Model):
    store = models.ForeignKey(advertisement, on_delete=models.CASCADE, default=None)
    weekday_from = models.PositiveSmallIntegerField(choices=WEEKDAYS, unique=True)
    weekday_to = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    from_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)
    to_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24)

    def get_weekday_from_display(self):
        return WEEKDAYS[self.weekday_from]

    def get_weekday_to_display(self):
        return WEEKDAYS[self.weekday_to]

class SpecialDays(models.Model):
    holiday_date = models.DateField()
    closed = models.BooleanField(default=True)
    from_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24, null=True, blank=True)
    to_hour = models.PositiveSmallIntegerField(choices=HOUR_OF_DAY_24, null=True, blank=True)