from django.db import models

# Create your models here
class fileupload(models.Model):
    inputfile=models.FileField(upload_to='documnents/')
    inputfile_name=models.CharField(max_length=20,blank=False)
    inputfile_content=models.TextField(blank=False)
    inputfile_author=models.CharField(max_length=20,blank=False)
    inputfile_uploadedat=models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.inputfile_name
