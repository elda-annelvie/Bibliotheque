from django.contrib import admin
from . models import Departement, Filiere, Document



class FiliereInline(admin.StackedInline):
	model =Filiere
	extra=3




class DocumentInline(admin.StackedInline):
	model =Document
	extra=3




class DepartementAdmin(admin.ModelAdmin):
	list_display  =('libelle','description',)
	list_filter   =('libelle',)
	search_fields =('libelle',)
	inlines=[
		FiliereInline,
	]





class FiliereAdmin(admin.ModelAdmin):
	list_display  =('libelle','image','departement',)
	list_filter   =('libelle',)
	search_fields =('libelle',)
	inlines=[
		DocumentInline,
	]
	





class  DocumentAdmin(admin.ModelAdmin):
	list_display  =('titre','image','filiere')
	list_filter   =('titre',)
	search_fields =('titre','fichier',)	

		

admin.site.register(Departement, DepartementAdmin )
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Document, DocumentAdmin)
# Register your models here
