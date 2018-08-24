from django.db import models
from django.urls import reverse

class Departement(models.Model):
  libelle=models.CharField(max_length=255, unique=True ,help_text='veuillez indiquer un departement')
  image=models.FileField(upload_to="Departement/images/", default="Departement/images/images39.png")
  description=models.TextField(help_text='Ce champ doit avoir au minimum 300 caractères')


  class Meta:
    ordering =('libelle',)
      


  def __str__(self):
     return self.libelle.lower()


  def get_absolute_url(self):
    return reverse('departement_detail', args=[str(self.id)])


class Filiere(models.Model):
  libelle=models.CharField(max_length=255, unique=True ,help_text='veuillez indiquer une filiere')
  image=models.FileField(upload_to="Departement/images/", default="Departement/images/images39.png")
  description=models.TextField()
  departement=models.ForeignKey(Departement, on_delete=models.CASCADE)

  class Meta:
    ordering =('libelle',)
      


  def __str__(self):
    return self.libelle.lower()


  def get_absolute_url(self):
    return reverse('filiere_detail', args=[str(self.id)])




class Document(models.Model):
  titre=models.CharField(max_length=100, unique=True, help_text='veuillez indiquer le titre du document')
  description=models.TextField()
  image=models.FileField(upload_to="Document/images/", default='Document/images/images34.jpeg')
  fichier=models.FileField(upload_to="Document/fichiers/", default='Document/fichiers/tutoriel2.pdf')
  filiere=models.ForeignKey(Filiere, on_delete=models.CASCADE)


  class Meta:
    ordering =('titre',)
      
   

  def __str__(self):
    return self.titre.lower()



  def get_absolute_url(self):
    return reverse('document_detail', args=[str(self.id)])




            







# Create your models here.