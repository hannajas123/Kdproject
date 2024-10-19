from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
class K_dunit(models.Model):
    name=models.CharField(max_length=100)
    unit_no=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    panchayath=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
class K_dmembers(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    panchayath=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
class User(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    photo=models.CharField(max_length=500)
    place=models.CharField(max_length=100)
    panchayath=models.CharField(max_length=100)
    ward=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
class Feedback(models.Model):
    USER=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField()
    feedback=models.CharField(max_length=100)
class Notification(models.Model):
    date=models.DateField()
    notification=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
class KdMembersMeetig(models.Model):
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    purpose=models.CharField(max_length=200)

class Meetig(models.Model):
    date = models.DateField()
    time = models.TimeField()
    purpose = models.CharField(max_length=200)
class kmembers_Meetig(models.Model):
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    purpose=models.CharField(max_length=200)
class Events(models.Model):
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    theme=models.CharField(max_length=200)
    title=models.CharField(max_length=200)



class Product(models.Model):
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=200)
    datails=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    photo=models.CharField(max_length=500)
    name=models.CharField(max_length=100)
    quality=models.CharField(max_length=100)
class Order_main(models.Model):
    USER=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField()
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
    status=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
class Order_sub(models.Model):
    ORDERMAIN=models.ForeignKey(Order_main, on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.CharField(max_length=100)
class Complaint(models.Model):
    USER=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateField()
    complaint=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
class Return_order(models.Model):
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    USER=models.ForeignKey(User, on_delete=models.CASCADE)
    reason=models.CharField(max_length=100)

class Kuris(models.Model):
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    totalAmount=models.CharField(max_length=100)
    totalinstallments=models.CharField(max_length=100)
    installmentamount=models.CharField(max_length=100)
    startingDate=models.DateField()
    EndingDate=models.DateField()


class Payment(models.Model):
    KDUNIT=models.ForeignKey(K_dunit,on_delete=models.CASCADE)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    ORDERMAIN=models.ForeignKey(Order_main, on_delete=models.CASCADE)
    date=models.DateField()
    amount=models.CharField(max_length=200)
    status=models.CharField(max_length=200)

class Kuri_Payment(models.Model):
    KDUNIT = models.ForeignKey(K_dunit, on_delete=models.CASCADE)
    KDMEMBER = models.ForeignKey(K_dmembers, on_delete=models.CASCADE)
    KURIS = models.ForeignKey(Kuris, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    winner = models.CharField(max_length=200)

class Cart(models.Model):
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE,default="")
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    quantity=models.CharField(max_length=30)