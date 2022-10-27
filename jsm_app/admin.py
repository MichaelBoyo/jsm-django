from django.contrib import admin

from jsm_app.models import User, Todo, Notes, Expense, Income, Category

admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Notes)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Category)

