from json.encoder import JSONEncoder
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
# from models import NE_Record, Foods_opt, Poop_opt, Pee_opt
from api.models import NE_Record, Foods_opt, Poop_opt, Pee_opt
from datetime import date, datetime, timedelta

def home( request ):
  return JsonResponse({'message':"hello"})

def NE_Record_search( request, year, month, day ):
  print( year, month, day )
  today = datetime.strptime( "%s-%s-%s" % (year, month, day), '%Y-%m-%d' )
  print( today )
  res = NE_Record.objects.filter(update_date__range=[today, today + timedelta(days=1)])
  return HttpResponse( serializers.serialize("json", res), content_type="application/json" )

def NE_Record_REQ( request ):
  method = request.POST.get("method") or request.method
  if   method == 'GET':
    return NE_Record_GET( request )
  elif method == 'POST':
    return NE_Record_POST( request )
  else:
    return JsonResponse({'error':'method not found'})

def NE_Record_GET( request ):
  today = date.today( )

  res = NE_Record.objects.filter(update_date__range=[today, today + timedelta(days=1)])
  # print( res )
  # return JsonResponse({'message':'GET'})
  return HttpResponse( serializers.serialize("json", res), content_type="application/json" )

def NE_Record_POST( request ):

  food_opt    = request.POST.get('food_opt')      or -1
  food_cap    = request.POST.get('food_cap')      or -1
  food_state  = request.POST.get('food_state')    or ''

  water_cap   = request.POST.get('water_cap')     or -1

  pee_opt     = request.POST.get('pee_opt')       or -1
  pee_cap     = request.POST.get('pee_cap')       or -1
  pee_state   = request.POST.get('pee_state')     or ''

  poop_opt    = request.POST.get('poop_opt')      or -1
  poop_state  = request.POST.get('poop_state')    or ''

  print("-"*10)
  print( food_opt, food_cap, food_state )
  print( water_cap )
  print( pee_opt, pee_cap, pee_state )
  print( poop_opt, poop_state )
  print("-"*10)

  update_date = request.POST.get('update_date', datetime.now().strftime("%Y-%m-%d %h:%M"))

  NE_Record.objects.create( 
    food_opt=food_opt, food_cap=food_cap, food_state=food_state, 
    water_cap=water_cap, 
    pee_opt=pee_opt, pee_cap=pee_cap, pee_state=pee_state, 
    poop_opt=poop_opt, poop_state=poop_state,
    update_date=update_date,
  )
  print( update_date )
  return JsonResponse({'message':'POST'})