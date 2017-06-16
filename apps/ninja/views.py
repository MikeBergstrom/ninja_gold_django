# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime

def index(request):
    print "index!"
    if 'goldcount' in request.session:
        print "session active"
        print request.session['goldcount']
        print request.session['activities']
    else:     
        request.session['goldcount'] = 0
        request.session['activities'] = []
    return render(request, 'ninja/index.html')

def process(request):
    if request.POST['building'] == 'farm':
        goldresp = random.randint(10,20)
        print goldresp
        request.session['goldcount'] += goldresp
        request.session['activities'].append("Earned " +str(goldresp) + " golds from the farm!" + str(datetime.datetime.now()))
        return redirect('/')
    elif request.POST['building'] == 'cave':
        goldresp = random.randint(5,10)
        print goldresp
        request.session['goldcount'] = request.session['goldcount'] + goldresp
        request.session['activities'].append("Earned "+ str(goldresp) + " golds from the cave! " + str(datetime.datetime.now()))
        return redirect('/')
    elif request.POST['building'] == 'house':
        goldresp = random.randint(2,5)
        print goldresp
        request.session['goldcount'] = request.session['goldcount'] + goldresp
        request.session['activities'].append("Earned "+ str(goldresp) + " golds from the house! " + str(datetime.datetime.now()))
        return redirect('/')
    elif request.POST['building'] == 'casino':
        goldresp = random.randint(-50,50)
        print goldresp
        if goldresp >=0:
            request.session['goldcount'] = request.session['goldcount'] + goldresp
            request.session['activities'].append("Entered a casino and won "+ str(goldresp) + " golds! Yipee!! " + str(datetime.datetime.now()))
            return redirect('/')
        elif goldresp < 50:
            request.session['goldcount'] = request.session['goldcount'] + goldresp
            request.session['activities'].append("Entered a casino and lost "+ str(goldresp) + " golds...ouch! " + str(datetime.datetime.now()))
            return redirect('/')
    
# Create your views here.
