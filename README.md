# 1 Написать api калькулятора и запустить его в Docker контейнере
![image](https://github.com/user-attachments/assets/b6e00195-eb00-4e9f-b6e6-8a455b882f9a)
docker build -t calc . n\
docker run -d -p 80:80 calc
![image](https://github.com/user-attachments/assets/4a36a5ef-4f29-49f7-9ca2-e7ada8202c07)
![image](https://github.com/user-attachments/assets/eafdd9e8-5c5c-4dcb-85fb-ce94dc6584d7)
![image](https://github.com/user-attachments/assets/e137bda4-cf27-4c9e-9688-888d0de3adcd)
![image](https://github.com/user-attachments/assets/0c0f3212-3599-4bed-bc2d-9bf5992dbeb7)

# 2 Создание пайплайна для обновления версии
![image](https://github.com/user-attachments/assets/1013c87a-6b6a-480b-b2cd-5b0c4506583e)
Делали через jenkins
В пайплайне не реализован процесс удаления старых контейнеров и запуск нового, так как на машине, на которой выполнялось задание запущены другие контейнеры, которые удалять не хотелось бы.
Работает скрипт по времени, активируется каждую минуту.
![image](https://github.com/user-attachments/assets/2a9aa748-7c54-4716-80ad-643e10b64419)

# 3 Внедрение инструментов безопасности
![image](https://github.com/user-attachments/assets/15a11670-b670-452a-9e69-bba7f632f5db)
Был внедрен только semgrep.
Выполнятеся он при каждом обновлении версии.

# 4 Анализ результата работы инструментов безопасности
![image](https://github.com/user-attachments/assets/bc574a37-f032-4c84-b483-793da7091b39)
Первая проблема: приложение запускается от root, это связано с тем, как у нас был собран контейнер:
![image](https://github.com/user-attachments/assets/a73819d4-571d-402c-93a2-21364afd4992)
Устранить это можно тем, что изменить пользователя, от которого выполняется програма.
![image](https://github.com/user-attachments/assets/cf25e994-7001-4c48-ac92-9cd603313279)
Вторая проблема: приложение запускается на хосте 0.0.0.0, из-за этого оно может быть доступно публично.
