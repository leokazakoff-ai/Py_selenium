
# Python_autotest

Автоматизация браузера с помощью Python и Selenium.  
Проект включает набор скриптов и тестов, демонстрирующих различные приёмы взаимодействия с веб-страницами и элементов управления браузером.

## 📦 Установка

1. Убедитесь, что у вас установлен Python версии 3.7 или выше.
2. Установите необходимые зависимости:

```bash
pip install selenium
```

3. Также потребуется установить соответствующий драйвер для вашего браузера, например, [ChromeDriver](https://sites.google.com/chromium.org/driver/).

## 🚀 Использование

Пример базового скрипта для автоматизации браузера:

```python
from selenium import webdriver

# Укажите путь к вашему драйверу
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Откройте веб-страницу
driver.get('https://example.com')

# Выполните необходимые действия
element = driver.find_element_by_id('some-id')
element.click()

# Закройте браузер
driver.quit()
```

## 🧪 Тестирование

Для тестирования с использованием `pytest`:

1. Установите `pytest`:

```bash
pip install pytest
```

2. Создайте файл теста, например, `test_example.py`:

```python
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
    yield driver
    driver.quit()

def test_example(driver):
    driver.get('https://example.com')
    assert 'Example Domain' in driver.title
```

3. Запустите тесты:

```bash
pytest
```

## 📄 Лицензия

Этот проект лицензируется на условиях MIT License.
