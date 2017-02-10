from django.contrib.auth.models import User

user = User.objects.create_user(
    'admin', email='admin@admin.com', password='demodemo')
user.is_superuser = True
user.is_staff = True
user.save()
