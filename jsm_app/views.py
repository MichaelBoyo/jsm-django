from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from jsm_app.models import User, Income, Expense, Todo, Notes
from django.urls import reverse


def home(request):
    return render(request, 'login.html')


def addExpense(request):
    return None


def login(request):
    user = request.POST.get('username')
    password = request.POST.get('password')
    found_user = get_object_or_404(User, username=user)
    if found_user.password == password:
        return render(request, 'userpage.html')
    return None


def register(request):
    return None


def addTodo(request):
    return None


def addNote(request):
    return None


def get_income():
    incomes = Income.objects.filter(
        date_created__lte=timezone.now()
    ).order_by('-date_created')
    return incomes


def get_expense():
    expenses = Expense.objects.filter(
        date_created__lte=timezone.now()
    ).order_by('-date_created')
    return expenses


def get_total():
    balance = 0
    for i in get_income():
        balance += i.amount
    for e in get_expense():
        balance -= e.amount
    return balance


def userpage(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    users = User.objects.all()
    for u in users:
        if u.username == username and u.password == password:
            return render(request, 'userpage.html',
                          {'user': u, 'incomes': get_income()[:10], 'expenses': get_expense()[:10],
                           'total': get_total()})
        else:
            print("user not found")
            return render(request, 'login.html', {
                'error_message': "invalid credentials.",
            })


def income(request):
    return render(request, 'income.html', {"incomes": get_income(), 'total': get_total()})


def expense(request):
    return render(request, 'expense.html', {"expenses": get_income(), 'total': get_total()})


def get_todos():
    return Todo.objects.filter(
        date_created__lte=timezone.now()
    ).order_by('-date_created')


def todo(request):
    return render(request, 'todos.html', {"todos": get_todos()})


def get_notes():
    return Notes.objects.all()


def note(request):
    return render(request, 'notes.html', {"notes": get_notes()})