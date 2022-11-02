from django.shortcuts import render,redirect
from todo.models import task
# Create your views here.
def add(request):
    if (request.method=='POST'):
        heading_=request.POST['heading'] #here heading is value from html name attribute
        detail_=request.POST['detail']
        date_=request.POST['date']
        print(heading_)
        print(detail_)
        print(date_)

        #create sql query to insert data
        #variable=classname.objects.create(columnname=value)
        insert_data=task.objects.create(heading = heading_ ,deatils = detail_,date= date_ , is_deleted='n')

        #executing sql query
        insert_data.save()
        return redirect('/')
    return render (request,'todo/add.html')

def show(request):
    #show_all=task.objects.all()
    #show_all={'show_all':show_all}
    show_all=task.objects.filter(is_deleted='n')
    show_all={'show_all':show_all}
    return render(request,'todo/show.html',show_all)


def delete(request,tid):
    #record_to_be_deleted=task.objects.filter(id=tid)
    #record_to_be_deleted.delete()
    record_to_be_deleted=task.objects.filter(id=tid)
    record_to_be_deleted.update(is_deleted='y')
    return redirect('/')

def update(request,tid):
    if (request.method=='POST'):
        heading_=request.POST['heading'] #here heading is value from html name attribute
        detail_=request.POST['detail']
        date_=request.POST['date']
        record_to_be_deleted=task.objects.filter(id=tid)
        record_to_be_deleted.update(heading = heading_ ,deatils = detail_,date= date_ )
        return redirect('/')
    else :
        record_to_be_update=task.objects.get(id=tid)
        record_to_be_updated={'show_all':record_to_be_update}
        return render(request,'todo/update.html',record_to_be_updated)
