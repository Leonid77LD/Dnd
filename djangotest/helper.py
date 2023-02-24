"""
django-admin startproject myproject   - создать новый проект (генерирует структуру)

python manage.py runserver            - запустить тестовый сервер (на http://127.0.0.1:8000)

python manage.py runserver 0.0.0.0:80 - запустить тестовый сервер доступный извне (не
                                        злоупотреблять)

django-admin startapp myapp           - создать приложение в текущем проекте

django-admin makemessages             - сгенерировать файлы с сообщениями подлежащими локализации

django-admin compilemessages          - скомпилировать файлы локализации

python manage.py makemigrations       - создать файлы миграций для БД

python manage.py sqlmigrate app 0001  - просмотр sql-кода, сгенерированного в миграции 0001
                                        приложения app

python manage.py shell                - запустить окно командной строки

python manage.py test                 - прогнать тесты (для прогона будет создана чистая БД)

python manage.py test --verbosity=2   - управление детализацией вывода при тестах (2-макс, 0 - мин)

python manage.py createsuperuser      - создать пользователя-администратора

"""

# part2

"""
В примерах ниже Board - класс, board - экземпляр класса.

Операция                                              Пример кода
Создать обьект без сохранения                         board = Board()
Сохранить обьект (создать или обновить)	              board.save()
Создать обьект и сохранить в базу	              Board.objects.create(name='...', desc='...')
Получить список всех обьектов	                      Board.objects.all()
Получить список обьектов, фильтр по полю	      Board.objects.get(id=1)

"""