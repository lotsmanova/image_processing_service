# Image Processing Service

---

Упрощенная версия одного из сервисов платформы видеоаналитики- сервис обработки изображений. Сервис принимает на вход изображения и прогоняет их по различным пайплайнам обработки изображений.

## Технологии

---

- Python 3+
- FastAPI
- PostgreSQL
- Pydantic
- SQLAlchemy
- Docker
- pytest

## Установка зависимостей

---

- Для работы программы необходимо установить зависимости из файла `requirements.txt`;
- Файл `.env.sample` содержит необходимые переменные окружения;

## Структура проекта

---

### Основное приложение

**Endpoints**:

- [ ]  `/process_image.` На вход принимает JPEG-изображение и id пайплайна, по шагам которого необходимо провести обработку изображения.
- [ ]  `/pipelines`.  CRUD для пайплайна и его шагов.

**Модели SQLAlchemy:**

- [ ]  `Pipelines`. Структура сущности для хранения информации о пайплайнах в базе данных.
- [ ]  `Steps`. Структура сущности для хранения информации о шагах в базе данных.

Связь между таблицами один ко многим. Фикстура для создания пайплайна обработки изображения находится в ./app/pipeline_fixture.json

**Схемы Pydantic:**

- [ ]  `PipelineAdd` и `PipelineRead`. Создание и просмотр пайплайнов соответственно.
- [ ]  `StepBase` и `StepRead`. Создание и просмотр шагов соответственно.

### Микросервис “Модель машинного обучения”

Микросервис имитирует работу модели машинного обучения. На вход получает обработанное изображение, после чего с вероятностью 50 % возвращает пустой ответ или заготовленные координаты бокса автомобиля - прямоугольника, внутри которого найден автомобиль.
**Endpoints**:

- [ ]  `/detect_car.` На вход принимает обработанное изображение (base64-строка), возвращает пустой ответ либо координаты задектированного автомобиля. Координаты автомобиля сохраняются в базу данных.
- [ ]  `/image_detection`.  Просмотр всех результатов обработки изображений и детальный просмотр результата для конкретного  изображения.

**Модели SQLAlchemy:**

- [ ]  `Result`. Структура сущности для хранения информации о результате проверки изображения  в базе данных.

**Схемы Pydantic:**

- [ ]  `ResultAdd` и `ResultRead`. Создание и просмотр пайплайнов соответственно.

## Документация

---

Документация к API доступна по ссылке [`http://127.0.0.1:8000/](http://127.0.0.1:8000/)docs/`

## Тестирование

---

Тесты написаны с помощью библиотеки `pytest`. Общее покрытие тестами 72 %.

## Docker

---

Сбор контейнера: `docker compose build`

Запуск контейнера: `docker compose up`