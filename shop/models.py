from django.db import models

# Create your models here.

class Category(models.Model):
    """Creates instance of category"""
    class Meta:
        """Gives verbose name for category"""
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
   
    def get_friendly_name(self):
        return self.friendly_name

# Options for plant care / filters

WATER_CHOICE = {
    ('water only when dry', 'WATER ONLY WHEN DRY'),
    ('light watering', 'LIGHT WATERING'),
    ('always thirsty', 'ALWAYS THIRSTY'),
}

HUMIDITY_CHOICE = {
    ('prefers dry air', 'PREFERS DRY AIR'),
    ('likes a little moisture', 'LIKES A LITTLE MOISTURE'),
    ('prefers humidity', 'PREFERS HUMIDITY'),
}

GROWTH_CHOICE = {
    ('fast grower', 'FAST GROWER'),
    ('takes its time', 'TAKES ITS TIME'),
    ('lifelong friend', 'LIFELONG FRIEND'),
}

TEMP_CHOICE = {
    ('keep cool', 'KEEP COOL'),
    ('keep at room temperature', 'KEEP AT ROOM TEMPERATURE'),
    ('keep warm', 'KEEP WARM'),
}

LIGHT_CHOICE = {
    ('loves the shade', 'LOVES THE SHADE'),
    ('loves a bit of both', 'LOVES A BIT OF BOTH'),
    ('loves bright light', 'LOVES BRIGHT LIGHT'),
}

EASE_OF_CARE_CHOICE = {
    ('practically unkillable', 'PRACTICALLY UNKILLABLE'),
    ('easy to care for', 'EASY TO CARE FOR'),
    ('needs a bit of love', 'NEEDS A BIT OF LOVE'),
    ('can be a diva', 'CAN BE A DIVA'),
}

# Seasonal collection options

SEASONAL_COLLECTION = {
    ('winter', 'WINTER'),
    ('valentines', 'VALENTINES'),
    ('spring', 'SPRING'),
    ('summer', 'SUMMER'),
}

SIZE_CHOICE = {
    ('one size', 'ONE SIZE'),
    ('10kg', '10kg'),
}


class Product(models.Model):
    """Creates instance of a product"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    is_plant = models.BooleanField(default=False, null=True, blank=False)
    is_accessory = models.BooleanField(default=False, null=True, blank=False)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=False, blank=False, default=name)
    height = models.CharField(max_length=254, null=True, blank=True)
    has_size_choice = models.BooleanField(
        default=False, null=True, blank=False)
    size = models.CharField(max_length=254, choices=SIZE_CHOICE, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    water_need = models.CharField(
        max_length=254, choices=WATER_CHOICE, blank=True)
    humidity_need = models.CharField(
        max_length=254, choices=HUMIDITY_CHOICE, blank=True)
    growth_need = models.CharField(
        max_length=254, choices=GROWTH_CHOICE, blank=True)
    temp_need = models.CharField(
        max_length=254, choices=TEMP_CHOICE, blank=True)
    light_need = models.CharField(
        max_length=254, choices=LIGHT_CHOICE, blank=True)
    ease_of_care = models.CharField(
        max_length=254, choices=EASE_OF_CARE_CHOICE, blank=True)
    is_in_seasonal_collection = models.BooleanField(
        default=False, null=True, blank=True)
    seasonal_collection = models.CharField(
        max_length=254, choices=SEASONAL_COLLECTION, blank=True)
    tip_water = models.TextField(null=True, blank=True)
    tip_humidity = models.TextField(null=True, blank=True)
    tip_growth = models.TextField(null=True, blank=True)
    tip_temperature = models.TextField(null=True, blank=True)
    tip_light = models.TextField(null=True, blank=True)
    tip_ease = models.TextField(null=True, blank=True)
    is_on_sale = models.BooleanField(default=False, null=True, blank=True)
    recommended_items = models.ManyToManyField("self", blank=True)
    sale_price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1054, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
