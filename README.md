PetShop API Autotests

Проект автоматизированного тестирования API для PetShop на Python с использованием Docker и Allure отчетов.

### Предварительные требования:
- Установленный Docker и Docker Compose

### Запуск тестов

1. Клонируйте репозиторий:
git clone 
cd AutoTestingAPIvr1

Создайте файл .env в корне проекта и добавьте ваш API-ключ:
PETSHOP_KEY=your_api_key_here

2. Запустите тесты:

docker-compose up --build
После выполнения вы увидите результаты тестов в консоли.

### Просмотр отчетов Allure
1. Для генерации и просмотра отчетов установите Allure на вашей машине:

# Для Windows через scoop
scoop install allure

# Или через npm
npm install -g allure-commandline

2. Сгенерируйте и откройте отчет:

allure serve allure-results
