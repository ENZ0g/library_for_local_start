# Проект личной библиотеки

Содержание:  
Функционал  
[Как развернуть локально](#как-развернуть-локально)

### Функционал

В верхней части всех страниц имеются кнопки для перехода
в соответствующий раздел: 

##### Список книг
Главная страница приложения.
- отображает все книги библиотеки
и большую часть информации по книгам
- подсчитывает количество наименований книг и общее их количество
- позволяет быстро изменить количество копий книг
- Наименование книги - ссылка на детальную информацию по книге.
Здесь дополнительно имеется поле для изображения книги,
 картинку можно изменить.
 
##### Добавить книгу
Форма добавления новой книги в библиотеку.
Позволяет заполнить все доступные поля.

##### Авторы, Издательства, Читатели
Эти страницы содержат таблицы с детальной информацией по
соответствующему разделу и содержат форму для добавления
новых записей.

Все формы при возникновении ошибок валидации стараются
деликатно и понятно сообщить пользователю, что от него
ожидается.

### Как развернуть локально

Рекомендую создать отдельное виртуальное окружение,
после активации которого выполнить следующие команды:  

`git clone https://github.com/ENZ0g/library_for_local_start.git`  
  
После того, как скопируется репозиторий, 
перейдите в папку `library_for_local_start` и выполните установку
необходимых модулей:  

`pip install -r requirements.txt`

Затем выполните миграции и заполните базу данных:  

`python manage.py migrate`  

`python manage.py loaddata db_data.xml`

Теперь можно запустить сервер:  

`python manage.py runserver`

Переходите по ссылке (`http://127.0.0.1:8000/
`) и пробуйте приложение!

Чтобы воспользоваться панелью администратора
(`http://127.0.0.1:8000/admin`), создайте
пользователя, следуя
указаниям команды:  

`python manage.py createsuperuser`  
