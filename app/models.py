from django.db import models

# ✅ ENROL FORM
class Enquiry(models.Model):
    child_name = models.CharField(max_length=100)
    child_dob = models.DateField()
    program = models.CharField(max_length=50)
    start_date = models.DateField()

    parent_name = models.CharField(max_length=100)
    parent_phone = models.CharField(max_length=20)
    parent_email = models.EmailField()

    message = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.parent_name


# ✅ CONTACT FORM (ADD THIS)
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='gallery/')
    is_featured = models.BooleanField(default=False)  # ⭐ ADD THIS
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title if self.title else "Gallery Image"