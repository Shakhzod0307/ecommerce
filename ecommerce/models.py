from django.contrib.auth.models import User
from django.db import models

# Create your models here.

CATEGORY_CHOICE = (
    ('MK', 'Milk'),
    ('TM', 'Tomato'),
    ('MS', 'Milkshake'),
    ('EG', 'Egg'),
    ('BN', 'Banana'),
    ('IC', 'Ice-Cream'),
)


class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    selling_price = models.FloatField(null=True)
    discounting_price = models.FloatField(null=True)
    description = models.TextField()
    composition = models.CharField(max_length=200)
    prodapp = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to='app/product')

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounting_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)


class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_status = models.CharField(max_length=100,null=True,blank=True)
    razorpay_payment_id = models.CharField(max_length=100,null=True,blank=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default='')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounting_price












