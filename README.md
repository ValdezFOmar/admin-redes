# admin-redes

Create database tables:

```sh
cd admin_redes
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Create users:

```sh
python manage.py shell
```

```python
>>> from clients.models import User
>>> User.objects.create_user(username='user', email='user@example.com', password='1234')
```
