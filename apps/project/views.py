from django.shortcuts import render, redirect
from models import Appoint
from django.contrib import messages
from ..login.models import User
from datetime import datetime



def appoints(request):

    if not "user_id" in request.session: #8000/travel  -> redirect
        return redirect('logins:index')
    user = User.objects.get(id = request.session['user_id'])

    appoint = Appoint.objects.filter(planned_by = user)
    other_appoint = Appoint.objects.exclude(planned_by = user)

    context = {
        'date':datetime.now().date(),
        'timeanddate' :datetime.now(),
        'appoint': appoint,
        'other_appoint': other_appoint
    }
    return render(request, 'project/appoint.html', context)
def process(request):
    print "process"
    if request.method == 'POST':
        data = Appoint.objects.addAppoint(request.POST)
        if data['valid']:
            print request.POST
            print "$"*50
            print data
            return redirect('projects:appoints')
        else:
            print 'invalid'
            for error in data['errors']:
                messages.error(request, error)
            return redirect ('projects:appoints')

def edit(request, id):
    update_id = Appoint.objects.get(id = id)
    context = {
        'update_id':update_id
    }
    return render(request, 'project/edit.html', context)

def delete(request,id):
	Appoint.objects.get(id=id).delete()
	return redirect('projects:appoints')


def update(request,id):
	if request.method == 'POST':

		appoitments=Appoint.objects.filter(id=id).update(tasks=request.POST['tasks'],status=request.POST['status'], date=request.POST['date'], time=request.POST['time'])
	return redirect('projects:appoints')
