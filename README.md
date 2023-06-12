# EXP1RMS | LOGGER

Проект предоставляет удобный и эффективный инструмент для создания нескольких логгеров в вашем проекте без необходимости написания длинных конфигурационных файлов для каждого из них. Создание нескольких логгеров позволяет значительно улучшить процесс отладки проекта и повысить его эффективность.

## Преимущества

 - **Улучшенная отладка:** Создание нескольких логгеров позволяет точно указывать на источник логов, не ограничиваясь только уровнем логирования. Это значительно повышает читаемость и понятность логов, а также облегчает процесс отладки и анализа возникающих проблем.
 - **Модульность и гибкость**: Обеспечивает модульность вашего проекта, позволяя создавать и настраивать логгеры для различных компонентов или модулей приложения. Это делает логирование более гибким и адаптируемым к различным потребностям вашего проекта.
 - **Удобство и эффективность**: Благодаря простоте и эффективности использования, помогает сократить время настройки и управления логированием. Вы можете создавать новые логгеры или уровни для них с минимальными усилиями, что сокращает время, затрачиваемое на настройку и начало работы с логами.

## Инициализация нового логгера
1. Добавить в переменную `LOGGERS_CONFIG` в *logs/config.py* необходимые логгеры, как в примере ниже:

```python
import logging

LOGGERS_CONFIG = [  
{'name': 'ServerLogger', 'log_level': logging.DEBUG},  
{'name': 'BotLogger', 'log_level': logging.DEBUG},  
{'name': 'AnotherLogger', 'log_level': logging.DEBUG},  
]
```

2. Добавить в *logs/\_\_init\_\_.py* переменные под объекты логгеров:

```python
from logs.setup import loggers  

server_logger = loggers['ServerLogger']  
bot_logger = loggers['BotLogger']  
another_logger = loggers['AnotherLogger'] 
```

3. Логгеры готовы к использованию
```python
from logs import bot_logger, server_logger, another_logger

server_logger.info("Example info message")
server_logger.warning("Example warning message")
server_logger.debug("Example debug message")

bot_logger.info("Example info message")
bot_logger.warning("Example warning message")
bot_logger.debug("Example debug message")

another_logger.info("Example info message")
another_logger.warning("Example warning message")
another_logger.debug("Example debug message")
```

##### Отображение в консоли:
![Просмотр логов в консоли](https://i.ibb.co/vPQzSp0/image.png)

## Создание новых уровней логирования
>💡 Применяются ко всем созданным логгерам автоматически
1. Добавьте новый уровень логирования в _logs/config.py:_
```python
from colorama import Fore
# Настройка приоритетов для уровней логирования
level_log = {
    'debug': 10,
    'daemon': 15,
    'info': 20,
    'user': 20, # Добавили уровень user
    'event': 21,
    'warning': 30,
    'error': 40,
    'exception': 50,
}

# Настройка цветов для уровней логирования
level_color = {
    'debug': Fore.WHITE,
    'daemon': 15,
    'event': Fore.CYAN,
    'info': Fore.GREEN,
    'user': Fore.LIGHTGREEN_EX, # Цвет для нового уровня
    'warning': Fore.YELLOW,
    'error': Fore.MAGENTA,
    'exception': Fore.RED,
}
```
##### Пример вызова и отображения в консоли:
```python
from logs import server_logger

server_logger.user('Custom user level')
```
![Отображение в консоли](https://i.ibb.co/NtWhcks/image.png)

## Декораторы для обработки исключений
#### Обработка с логгированием:
```python
from logs import catch_exception, server_logger

# Обязательно передаём объект логгера, от которого будет вызвано сообщение.
# Необязательно передаём кастомное сообщение в выводе логов.
@catch_exception(server_logger, 'Custom error message')
def foo(a, b):
    c = a / b
    print(c)
```
![Отображение в консоли](https://i.ibb.co/pj8FnVM/image.png)

#### Тихая обработка исключений:
```python
from logs import silent_exception


@silent_exception()
def bar(a, b):
    c = a / b
    print(c)
```
В этом случае вывода в консоль по возникшим исключениям не будет.
Не рекомендую злоупотреблять этой функцией, но иногда она может оказаться полезной.

## Хранение
Каждый созданный логгер будет хранить информацию в своей директории.
Каждый уровень логгирования будет хранить информацию в своём файле.

![Структура файлов](https://i.ibb.co/0DwcdfV/image.png)