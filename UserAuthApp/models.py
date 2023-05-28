from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class UserModel(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('active','Active'),
        ('pending_verification','Pending Verification'),
        ('terminated','Terminated'),
        ('blocked','Blocked')   #use this when you want to restrict COD orders
        ('closed','Closed'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,blank=True,null=True)
    password = models.CharField(max_length=128)

    def set_password(self,raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self,raw_password):
        return check_password(raw_password,self.password)

    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    rating = models.IntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True)
    account_status = models.CharField(max_length=25,choices=ACCOUNT_STATUS_CHOICES)

class DeliveryPerson(models.Model):
    VEHICLE_CHOICES = [
        ('bike', 'MotorBike'),
        ('cycle', 'BiCycle'),
    ]
    AVAILABILITY_CHOICES = [
        ('offline','Offline'),
        ('on_order','On Order'),
        ('available','Available'),
    ]
    # id = 
    delivery_user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    # active_order_id = FK
    adhar_card = models.IntegerField(max_length=20)
    pan_card = models.CharField(max_length=10)
    vehicle_type = models.CharField(max_length=20,choices=VEHICLE_CHOICES)
    availability = models.CharField(max_length=20,choices=AVAILABILITY_CHOICES)
    total_delivery = models.IntegerField(default=0)

class Customer(models.Model):
    customer_user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # default address
    # order_history = 
    # active_order = 
    default_payment = models.CharField(max_length=100)
    # discounts = models.C/

class AddressUser(models.Model):
    user_id = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.IntegerField(max_length=10)
    appartment = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9,decimal_places=6)
    longitude = models.DecimalField(max_digits=9,decimal_places=6)


# def create_user(self, username, password):
#     self.username = username
#     self.set_password(password)
#     self.save()

# def authenticate_user(self, username, password):
#     user = UserModel.objects.get(username=username)
#     if user.check_password(password):
#         # Password is correct, perform authentication
#         # ...
#         return user
#     else:
#         # Password is incorrect, authentication failed
#         return None
