from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from mine.models import User, MyUser, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.



def welcome(request):
	return render(request,'welcome.html')





def register_data(request):
	frm = RegisterForm()
	ctx = {'form': frm}
	return render(request, 'signinpage.html', ctx)


def login_data(request):
	fm = LoginForm()
	ptx = {'fm': fm}

	return render(request, 'loginpage.html', ptx)








def loggin(request):

    if not request.method == 'POST':
        return HttpResponse('get request')

    frm = LoginForm(request.POST)

    if frm.is_valid():
        print ('yes'), frm.cleaned_data
        uname = frm.cleaned_data['username']
        ps = frm.cleaned_data['password']
        print (uname)
    u = authenticate(username=uname, password=ps)
    print (ps)
    print (u)
    if u:

        # if u.is_active:
        # ....login(request, u)
        # ctx = {'user': u}

        name = uname
        name = str(name)
        m = User.objects.get(username=name)
        n = MyUser.objects.get(user=m)
        if n.t == 0:
            n.t = 1
            n.save()
            return render(request, 'profile.html', {'users': uname})
        else:

            return render(request, 'home.html',{'users': uname})
    else:

    # else:
    # ............return HttpResponse("User account deactivated")

        return HttpResponse('Invalid User!')
	

















def register(request):
	if request.method == 'POST':
		frm = RegisterForm(request.POST)
		# frm.cleaned_data
	#	print (frm)
		# return HttpResponse("efgsb")
		if frm.is_valid():
			fdata = frm.cleaned_data
			uname = fdata['username']
			name = fdata['name']
			passwd = fdata['password']
			try:
				print (uname, passwd)
				usr = User(username=uname)
				usr.set_password(passwd)
				usr.save()
			except:
				return HttpResponse("User already exists!")
			myusr = MyUser(user=usr, name=name,t=0)
			myusr.save()

			return render(request,"welcome.html")
		else:
			return HttpResponse("fill all the boxes")
	else:
		return HttpResponse('Nice Try!')




def profile(request):
    a = request.GET.get('username')
    b = request.GET.get('address')
    a=str(a)
    b=str(b)
    u = User.objects.get(username=a)
    p = MyUser.objects.get(user=u)
    p.address=b
    p.save()
    

    return render(request,'home.html',{'users' :a})
'''	b=requests.GET.get('address')

	return render(request,'profile.html')
'''












