
>***жирным курсивом*** - команды в консоли
### Установка проекта     
1. Создали директорию. Например - *test_dir*<br>
2. Качаем архив **[Отсюда](https://github.com/anton-3003/sf-shelter/archive/main.zip)**          
3. Распаковываем в папке *test_dir*         
4. Открываем консоль и выбираем эту директорию      
5. Создаем виртуальное окружение. Называем, например, *v_test*          DISC:\\..\\test_dir>***python -m venv v_test***         
6. Активируем виртуальное окружение:    DISC:\\..\\test_dir>***v_test\scripts\activate.bat***        
Строка примет вид *(v_test) DISC:\\..\\test_dir>*           
7. Переходим в распакованную папку с проектом и устанавливаем зависимости: ***pip install -r requirements.txt***           
8. Запускаем локальный сервер:  ***python manage.py runserver***            
        
### Администрирование
- После пункта №7 выполнить команду ***python manage.py createsuperuser*** и ввести данные          
- После запуска сервера и открытия в браузере страницы, перейти по ссылке "Администрирование" в навигационной панели<br>
- Ввести данные, которые указали при создании суперпользователя<br>
- Можно добавлять, удалять, редактировать питомцев   

![alt text](https://icon-icons.com/icons2/1465/PNG/48/756exclamationmark_100528.png) Добавлять изображения питомцев возможно только из админ.панели!           


### Разворачиваем на heroku   
*Должен быть установлен git и heroku                 
В корневой папке проекта в консоли:     
1. Инициализируем репозиторий ***git init***  
2. Добавляем в него файлы ***git add .***  
3. Коммитим файлы ***git commit -m "initial commit"***  
4. Создаем проект на платформе хероку ***heroku create***
5. Фиксируем все изменения 
    - ***git add .***  
    - ***git commit -m "about to deploy"***    
6. Заливаем на хероку ***git push heroku master***

### Клонируем объект
- В консоли выбираем папку, в которую хотим скопировать(клонировать) объект
- Логинимся на платформе хероку (перенаправит на сайт): ***heroku login***
- Подтверждаем log in, возвращаемся в консоль и клонируем объект: ***heroku git:clone -a {название объекта}***
- Редактируем файлы уже непосредственно в клонированной папке
- Переходим в клонированную папку: ***cd {название проекта}***
- Фиксируем изменения:
    - ***git add .***
    - ***git commit -am "make it better"***
- Заливаем обратно на хероку: ***git push heroku master***
    
    





 