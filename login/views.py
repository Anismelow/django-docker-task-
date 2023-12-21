from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')



# def registro(request):
#     if request.method == 'GET':
#         return render(request, 'registro.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 return redirect('login')
#             except:
#                 return render(request, 'registro.html', {
#                     'form': UserCreationForm,
#                     'error': 'El usuario ya existe'
#                 })
#         else:
#             return render(request, 'registro.html', {
#                 'form': UserCreationForm,
#                 'error': 'Las contraseñas no coinciden'
#             })
    
def registro(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                print(f'Se ha creado el usuario {user}')
                return redirect('task')
            except:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        else:
            return render(request, 'registro.html', {
                'form': UserCreationForm,
                'error': 'Las contraseñas no coinciden'
            })
    else:
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    

def inicioSesion(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        try:
            user = authenticate(request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                print(f'Se ha iniciado sesion el usuario {user}')
                return redirect('task')
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Usuario o contraseña incorrectos'
                })
        except ValueError:
            return render(request, 'login.html', {
                'form': form,
                'error': 'Usuario o contraseña incorrectos'
            })
    return render(request, 'login.html', {'form': form})


def task(request):
    return render(request, 'task.html')