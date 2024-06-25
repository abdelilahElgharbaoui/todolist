from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from core.models import Todo
from core.forms import TodoForm


@login_required
def index(request):
    context = {
        'todos': Todo.objects.filter(user=request.user),
        'form': TodoForm()
    }
    return render(request, 'index.html', context)


@login_required
@require_POST
def submit_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        todo = form.save(commit=False)
        todo.user = request.user
        todo.save()

        # return an HTML partial
        context = {'todo': todo}
        return render(request, 'index.html#todoitem-partial', context)

@login_required
@require_POST
def complete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = True 
    todo.save()
    context = {'todo': todo}
    return render(request, 'index.html#todoitem-partial', context)    

@login_required
@require_POST
def uncomplete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.is_completed = False 
    todo.save()
    context = {'todo': todo}
    return render(request, 'index.html#todoitem-partial', context)  

@login_required
@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    response = HttpResponse(status=204)
    response['HX-Trigger'] = 'delete-todo'
    return response

@login_required
def disconnect_view(request):
    if request.method == 'POST':
        request.session.flush()  # Clear all session data
        return redirect('index')  # Redirect to the home page or login page
    return redirect('index') 