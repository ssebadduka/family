from django.db import models

# Create your models here.
class Kika (models.Model):
    Kika = models.CharField(max_length=50)
    Owakasolya = models.CharField(max_length=50)
    Asangibwa = models.CharField(max_length=50)


    class Meta:
        verbose_name = ("kika")
        verbose_name_plural = ("kika")

    def __str__(self):
        return f'{self.Kika} - {self.Owakasolya}-{self.Asangibwa}'

    def get_absolute_url(self):
        return reverse("kika_detail", kwargs={"pk": self.pk})
class Akabiro (models.Model):
    Akabiro = models.CharField(max_length=50)
    Omubala = models.CharField(max_length=50)
    


    class Meta:
        verbose_name = ("Akabiro")
        verbose_name_plural = ("Akabiro")

    def __str__(self):
        return f'{self.Akabiro} - {self.Omubala}'

    def get_absolute_url(self):
        return reverse("Akabiro_detail", kwargs={"pk": self.pk})

class Siga(models.Model):
    Siga = models.CharField(max_length=50)
    Owesiga = models.CharField(max_length=50)
    Asangibwa = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Siga")
        verbose_name_plural = ("Siga")

    def __str__(self):
        return f'{self.Siga} - {self.Owesiga}-{self.Asangibwa}'

    def get_absolute_url(self):
        return reverse("Siga_detail", kwargs={"pk": self.pk})
class Mutuba(models.Model):
    Mutuba=models.CharField(max_length=50)
    Owomutuba=models.CharField(max_length=50)
    Asangibwa = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Mutuba")
        verbose_name_plural = ("Mutuba")

    def __str__(self):
        return f'{self.Mutuba} - {self.Owomutuba}-{self.Asangibwa}'

    def get_absolute_url(self):
        return reverse("Mutuba_detail", kwargs={"pk": self.pk})

class Lunyiriri(models.Model):
    Lunyiriri=models.CharField(max_length=50)
    Owolunyiriri=models.CharField(max_length=50)
    Asangibwa = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Lunyiriri")
        verbose_name_plural = ("Lunyiriri")

    def __str__(self):
        return f'{self.Lunyiriri} - {self.Owolunyiriri}-{self.Asangibwa}'

    def get_absolute_url(self):
        return reverse("Lunyiriri_detail", kwargs={"pk": self.pk})

class Lugya(models.Model):
    Lugya=models.CharField(max_length=50)
    
    Lusangibwa = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Lugya")
        verbose_name_plural = ("Lugya")

    def __str__(self):
        return f'{self.Lugya} - {self.Lusangibwa}'

    def get_absolute_url(self):
        return reverse("Lugya_detail", kwargs={"pk": self.pk})

class Nju(models.Model):
    Nju=models.CharField(max_length=50)
    
    Esangibwa = models.CharField(max_length=50)
    name = models.IntegerField(verbose_name='Generation')
    
    desc_gen = models.CharField(max_length=200,verbose_name='Generation Description')
    Lugya = models.ForeignKey(Lugya,on_delete=models.CASCADE,
    null=True,blank=True,related_name='Lugya_name')

    class Meta:
        verbose_name = ("Nju")
        verbose_name_plural = ("Nju")

    def __str__(self):
        return f'{self.Nju} - {self.Esangibwa}-{self.name}'

    def get_absolute_url(self):
        return reverse("Lugya_detail", kwargs={"pk": self.pk})



class Muganda(models.Model):
    Kika = models.ForeignKey(Kika,on_delete=models.CASCADE,
    null=True,blank=True,related_name='kika_name')
    Akabiro = models.ForeignKey(Akabiro,on_delete=models.CASCADE,
    null=True,blank=True,related_name='kika_name')
    Siga = models.ForeignKey(Siga,on_delete=models.CASCADE,
    null=True,blank=True,related_name='siga_name')
    Mutuba = models.ForeignKey(Mutuba,on_delete=models.CASCADE,
    null=True,blank=True,related_name='mutuba_name')
    Lunyiriri = models.ForeignKey(Lunyiriri,on_delete=models.CASCADE,
    null=True,blank=True,related_name='lunyiriri_name')
    Lugya = models.ForeignKey(Lugya,on_delete=models.CASCADE,
    null=True,blank=True,related_name='lugya_name')
    Nju = models.ForeignKey(Nju,on_delete=models.CASCADE,
    null=True,blank=True,related_name='Nju_name')
    name = models.CharField(max_length=100,verbose_name='Erinya(Full Names)')
    Life_TYPE_CHOICES=[
        ('Died','Died'),
        ('Living','Living')
    ]
    your_Life_Status =models.CharField(max_length=100,choices=Life_TYPE_CHOICES)
    father = models.CharField(max_length=100,verbose_name='Taata(Father Full Name)')
    father_TYPE_CHOICES=[
        ('Died','Died'),
        ('Living','Living')
    ]
    father_Life_Status = models.CharField(max_length=100,choices=father_TYPE_CHOICES,default='Living')
    Address = models.CharField(max_length=50)
    Contact = models.CharField(max_length=50)
    Gender_TYPE_CHOICES=[
        ('Male','Male'),
        ('Female','Female')
    ]
    Gender = models.CharField(max_length=50,choices=Gender_TYPE_CHOICES)
    Age_TYPE_CHOICES=[
        ('Below 18','Below 18'),
        ('Above 18','Above 18')
    ]
    Age=models.CharField(max_length=50,choices=Age_TYPE_CHOICES)
    photo=models.ImageField(upload_to='pic')







    class Meta:
        verbose_name = ("name")
        verbose_name_plural = ("name")

    def __str__(self):
        return f'{self.Nju} - {self.name} - {self.father}-{self.your_Life_Status}'

    def get_absolute_url(self):
        return reverse("Lugya_detail", kwargs={"pk": self.pk})

