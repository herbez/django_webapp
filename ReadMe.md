Create table
# py manage.py makemigrations
# py manage.py migrate

create super user or admin
# py manage.py createsuperuser
# Username: admin
# password: Hpass@123

Manage products in admin panel
# from .models import Product

# admin.site.register(Product)

Customise admin panel
# class ProductAdmin(admin.ModelAdmin):
    #list_display = ('name','price','stock')

Manage products in admin panel
# admin.site.register(Product, ProductAdmin)
