from django.db import models

# Create your models here.

class Foods_opt( models.Model ):
  name        = models.TextField( blank=False, default="" )
  fullname    = models.TextField( blank=True,  default="" )
  source      = models.TextField( blank=True,  default="" )
  user        = models.IntegerField( default=-1 )

class Poop_opt( models.Model ):
  name        = models.TextField( blank=False )

class Pee_opt( models.Model ):
  name        = models.TextField( blank=False )

class NE_Record( models.Model ): # Nutrient & Excretion Record
  user_id     = models.IntegerField( default=-1 )

  food_opt    = models.IntegerField( default=-1 ) # Ref Foods.id
  food_cap    = models.IntegerField( default=-1 )
  food_state  = models.TextField( default='', blank=True )
  
  water_cap   = models.IntegerField( default=-1 )
   
  pee_opt     = models.IntegerField( default=-1 ) # choose
  pee_cap     = models.IntegerField( default=-1 )
  pee_state   = models.TextField( default='', blank=True )

  poop_opt    = models.IntegerField( default=-1 ) # choose
  poop_state  = models.TextField( default='', blank=True )
  
  insert_date = models.DateTimeField( auto_now_add=True )
  update_date = models.DateTimeField( default=None )
  # edit_date   = models.DateField( auto_now=True )
  # update_date = models.DateField( auto_now_add=True )