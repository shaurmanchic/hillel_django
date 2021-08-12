# hillel_django

### Startup

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Running celery

celery -A hillel_django_project worker -l info --concurrency 1 -P solo
celery -A hillel_django_project beat -l info --concurrency 1 -P solo


## Homework:

(2) 1. Настроить rabbitmq + celery + celerybeat

https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html
https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html

(2) 2. Создать Middleware которая будет логировать все действия в рамках админки (`if request.path.startswith('/admin/'):`) и сохранять в базу.Модель:

class Logger(models.Model):
    path = models.CharField (request.path) 
    method = models.CharField (request.method)
    time_delta = models.CharField Время работы вью функции
    created = models.DateTimeField (auto_now_add=True)  # https://docs.djangoproject.com/en/2.2/ref/models/fields/#django.db.models.DateField.auto_now_add

(3) 3. Удалять все логи (модель Logger) "старше" 7 дней, с периодикой раз в день. (created)

(3) 4. Создать форму ContactUS(forms.Form) (title, message, email_from).
На save формы необходимо отправить письмо на vitalik1996@gmail.com. Письмо должно уходить через celery task. Только пожалуйста, тестируйте на своей почте сначала)

https://docs.djangoproject.com/en/3.2/topics/email/