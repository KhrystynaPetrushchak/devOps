# Lab4

### 1. Ознайомилась шо таке Docker
### 2. Перевірила чи встановлений докер і виконала наступні команди
#### docker -v
#### docker -h
#### docker run docker/whalesay cowsay Docker is fun
#### Перенаправила вивід цих команд у файл my_work.log закомітила до репозиторію
### 3. Ознайомилась з документацією
### 4. Виконала команди 
#### sudo docker pull python:3.8-slim
#### sudo docker images
#### sudo docker inspect python:3.8-slim
#### Створила файл Dockerfile і скопіювала вміст такого ж файлу з репозиторію, але замінила посилання на свій Git і тд.
### 5. Створила власний репозиторій на Docker Hub.
### 6. Виконала білд імеджа та завантажила його до репозеторію за допомогою команд :
#### sudo docker build -t khrystyna2411/devops_lab4:khrustya .
#### sudo docker images 
#### sudo docker push khrystyna2411/devops_lab4:khrustya
#### Посилання на Docker: https://hub.docker.com/r/khrystyna2411/devops_lab4/tags?page=1&ordering=last_updated
#### Посилання на скачування імеджа: https://hub.docker.com/layers/khrystyna2411/devops_lab4/khrustya/images/sha256-4df44476e11419324f49991fa7fda6babba9e00e9dde5915b4bd856965fc0e0a?context=explore
### 7.Намагалась виконати запуск веб-сайту, і для цього застосувала ось таку команду:
#### sudo docker run -it --name=khrustya --rm -p 8000:8000 khrystyna2411/devops_lab4:khrustya
#### Сайт працює
### 8. Створила файл Dockerfile.monitor 
### 9. Виконала білд даного імеджа docker build -t khrystyna2411/devops_lab4:monitoring .
#### Посилання : https://hub.docker.com/layers/khrystyna2411/devops_lab4/monitoring/images/sha256-39f3fd8956e60585953d3dcbde035a4e2bddd15171d9f2b1b19cea48d058b3a8?context=explore
### 10.Переконалась шо програма виконується успішно. Виконала команду
#### sudo docker run -it --rm -p 8000:8000 --net=host khrystyna2411/devops_lab4:khrustya
### 11. Виконала наступні команди для перенесення файлу server.log
#### sudo docker ps
#### sudo docker export 10a04951628f > latest.tar
#### Зайшла в папку App та витягнула звідти server.log
 
 
