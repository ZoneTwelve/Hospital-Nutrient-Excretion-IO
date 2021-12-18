from django.db import models

# Create your models here.

class Foods( models.Model ):
  name       = models.TextField( blank=False, default="" )
  fullname   = models.TextField( blank=False, default="" )
  source     = models.TextField( default="" )
  user       = models.IntegerField( default=-1 )

class Poop_opt( models.Model ):
  name       = models.TextField( blank=False )

class NE_Record( models.Model ): # Nutrient & Excretion Record
  user_id    = models.IntegerField( default=-1 )

  food_name  = models.IntegerField( ) # Ref Foods.id
  food_cap   = models.IntegerField( )
  food_state = models.TextField( default='' )
  
  water_cap  = models.IntegerField( )
  
  pee        = models.IntegerField( ) # choose
  pee_cap    = models.IntegerField( default=0 )
  pee_state  = models.TextField( default='' )

  poop       = models.IntegerField( ) # choose
  poop_state = models.TextField( default='' )
  
  edit_date   = models.DateField( auto_now=True )
  update_date = models.DateField( auto_now_add=True )