from django.shortcuts import render,redirect
from attend.serializer import UserSerializer
from django.http import JsonResponse,HttpResponse

from rest_framework.decorators import api_view
from django.http import JsonResponse
from attend.models import User,Work,Exit
from datetime import date
from datetime import datetime

@api_view(['POST'])
def Add_user(request):
    
    msg = ""
    try:
        if request.method =='POST':
         
            new_user = User(
                user_name=request.POST['user_name'],
                user_pword="pword",
                shift_start=request.POST['start_time'],
                shift_end= request.POST['end_time']
            )

            
            new_user.save()
            msg="New user added"
            print(msg)
            return JsonResponse({"success":"successfully added"})
            # return render(request,'add_user.html')
        
    except Exception as e:
        # return JsonResponse({"error": str(e) })
        print(e)
        # return render(request,'add_user.html')
        return JsonResponse({"error": str(e) })
    

@api_view(['POST'])
def Checkin(request):
    msg = ""
    try:
        if request.method =='POST':
            
            print(request.POST['user_name'])
            userdata=  User.objects.get(user_name=request.POST['user_name'])
            currentday = date.today()
            print(currentday)
            # entry_time=request.POST['entry_time']
            
            print(request.POST['entry_time'])
            print(userdata.shift_start)
            print(userdata.shift_start.hour)
            entri=datetime.strptime(request.POST['entry_time'], "%H:%M")
            print(entri)
            # print(datetime.strptime((request.POST['entry_time'])))
            delay=((entri.hour*60)+entri.minute)-((userdata.shift_start.hour*60)+(userdata.shift_start.minute))
            if delay>30:
                status="absend"
            else:
                status="present"
            print(status)
            new_work = Work(
                user_name=request.POST['user_name'],
                work_date=currentday,
                start_time=request.POST['entry_time'],
                latetime1=delay,
                status=status,
                user_id=userdata.id
            )

            if Work.objects.filter(user_name=request.POST['user_name'],work_date=currentday):
                msg="Double entry"
                print(msg)
                # return httpResponce({"success":"successfully added"})
                # return HttpResponse("double entry")
                return JsonResponse({"error": str(msg) })
            else:
                new_work.save()
                
                msg="entry time added"
                print(msg)
                return JsonResponse({"success":"successfully added"})
                # return render(request,'entry.html')
        
    except Exception as e:
        print(e)
        # return render(request,'entry.html')
        return JsonResponse({"error": str(e) })


@api_view(['POST'])
def Checkout(request):
    msg = ""
    try:
        if request.method =='POST':
            
            print(request.POST['user_name'])
            userdata=  User.objects.get(user_name=request.POST['user_name'])
            currentday = date.today()
            
           
            
           
           
            exit=datetime.strptime(request.POST['exit_time'], "%H:%M")
            
            
            delay=((exit.hour*60)+exit.minute)-((userdata.shift_end.hour*60)+(userdata.shift_end.minute))
            if delay<0:
                status="absend"
            else:
                status="present"
           
            new_exit = Exit(
                user_name=request.POST['user_name'],
                work_date=currentday,
                exit_time=request.POST['exit_time'],
                extratime=delay,
                status=status,
                user_id=userdata.id
            )

            if Exit.objects.filter(user_name=request.POST['user_name'],work_date=currentday):
                msg="Double entry"
                print(msg)
                # return httpResponce({"success":"successfully added"})
                return JsonResponse({"success":str(msg)})
                # return HttpResponse("double entry")
            else:
                new_exit.save()
                
                msg="exit time added"
                print(msg)
                return JsonResponse({"success":str(msg)})
                # return render(request,'exit.html')
        
    except Exception as e:
        print(e)
        # return render(request,'exit.html')
        return JsonResponse({"error": str(e) })


    
@api_view(['POST'])
def Report(request):
   
    try:
        if request.method =='POST':
            
            username=request.POST['username']
            startdate=request.POST['startdate']
            enddate=request.POST['enddate']
            entrydata= Work.objects.filter(user_name=username,work_date__range=(startdate, enddate)) 
            # entrydata= Work.objects.all()
            exitdata=  Exit.objects.filter(user_name=username,work_date__range=(startdate, enddate)) 

            for i  in entrydata:
                x=[]
                x.append(i.work_date)
                x.append(i.start_time)
                x.append(i.latetime1)
                x.append(i.status)
                print(x)

            for j in exitdata:
                Y=[]
                Y.append(j.work_date)
                Y.append(j.exit_time)
                Y.append(j.extratime)
                Y.append(j.status)
                print(Y)
            return HttpResponse(x)
            return HttpResponse(Y)
            
            
        
            
            
            
        
    except Exception as e:
        # return JsonResponse({"error": str(e) })
        print(e)
        return render(request,'report.html')
