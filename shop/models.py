from django.db import models
# it was creating when we can run manage.py migrate
# Create your models here.for database
# here we can make a class for our products
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50,default="") # defining name ,description date in database
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    des = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/image',default='')   # for inserting image and the best way is first going on setiings.py and then see Static_Url and then see

    def __str__(self):
        return self.product_name

class Contact(models.Model):
        msg_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50, default="")  # defining name ,description date in database
        email= models.CharField(max_length=70, default="")
        phone = models.CharField(max_length=12, default=0)
        desc = models.CharField(max_length=500,default='')


        def __str__(self):
            return self.name

class Orders(models.Model):
        order_id = models.AutoField(primary_key=True)
        items_json = models.CharField(max_length=5000, default="")
        amount= models.IntegerField(default=0)
        name = models.CharField(max_length=50, default=" anonymus ")  # defining name ,description date in database
        email = models.CharField(max_length=70, default="")
        address= models.CharField(max_length=300, default="")
        city = models.CharField(max_length=200, default="")
        state = models.CharField(max_length=50,default="")
        zip_code = models.CharField(max_length=20,default="")
        phone = models.CharField(max_length=12,default=0)

        def __str__(self):
            return self.name

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."
