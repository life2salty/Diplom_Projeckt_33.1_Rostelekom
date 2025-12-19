# Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии»
33.1. Итоговый проект по автоматизации тестирования (PJ-04):

Выполнил: Алимбеков Манcур QAP-193

Ссылка на чек-лист, тест-кейсы и баг репорты: https://disk.yandex.ru/i/FDiqY_aI9XK6Vg  

В процессе выполнения проекта использовалось ручное тестирование в проверках юзабилити интерфейса, работы системы и адаптивности сайта на мобильном устройстве. Некоторые тест-кейсы, которые можно автоматизировать, выполнялись вручную т.к. ручная проверка позволила понять логику работы системы, четко не отраженную в брифе от заказчика. Также применялось автоматизированное тестирование с использованием Selenium WebDriver и библиотеки pytest. С помощью него проверялись часть сценариев авторизации и регистрации, которые легко поддаются автоматизации. Кроме того, автоматизированное тестирование позволило сократить время и затраты на повторное выполнение одних и тех же тест-кейсов вручную, а также повысило гибкость проверок, при внесении изменений в систему. Что касается применения техник тест-дизайна были применены следующие техники:

1. Техника классов эквивалентности

Эта техника применялась для определения наборов тестовых входных данных, которые должны привести к одинаковому поведению системы. Например, TC-RT-001, TC-RT-002, TC-RT-003 и TC-RT-004 проверяют авторизацию с различными валидными входными данными, которые должны привести к успешной авторизации.

2. Техника анализа граничных значений

Эта техника применялась для проверки граничных значений входных данных. Например, TC-RT-020, TC-RT-021 и TC-RT-022 проверяют восстановление пароля с некорректными паролями, которые не соответствуют требованиям по длине, наличию заглавных букв и использованию только латинских символов.

Автотесты имеют названия отражающие ожидаемый результат и объект тестирования.

Команда для запуска всех тестов в пакете "tests":

python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests

Команда для запуска отдельного теста, например, в файле test_reg_page_check.py:

python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests\test_reg_page_check.py -k "test_reg_page_check_all_fields_text"

ENG

# Graduation Project: A Real-World Case Study at Rostelecom Information Technologies
33.1. Final Project on Test Automation (PJ-04):

Completed by: Mansur Alimbekov QAP-193

Link to the checklist, test cases, and bug reports: https://disk.yandex.ru/i/FDiqY_aI9XK6Vg

During the project, manual testing was used to check the interface usability, system operation, and website responsiveness on mobile devices. Some test cases that could have been automated were performed manually, as manual testing allowed us to understand the system's logic, which was not clearly reflected in the client's brief. Automated testing was also used using Selenium WebDriver and the pytest library. This was used to test some of the authorization and registration scenarios, which are easily automated. Furthermore, automated testing reduced the time and cost of manually re-executing the same test cases and increased the flexibility of testing when making changes to the system. Regarding the application of test design techniques, the following were employed:

1. Equivalence Class Technique

This technique was used to identify sets of test input data that should result in identical system behavior. For example, TC-RT-001, TC-RT-002, TC-RT-003, and TC-RT-004 test authorization with different valid input data that should result in successful authorization.

2. Boundary Value Analysis Technique

This technique was used to test the boundary values ​​of input data. For example, TC-RT-020, TC-RT-021, and TC-RT-022 test password recovery with incorrect passwords that do not meet the length, capitalization, and Latin character requirements.

Automated tests are named to reflect the expected result and the object being tested.

Command to run all tests in a suite "tests":

python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests

Command to run a single test, for example in a file test_reg_page_check.py:

python -m pytest -v --driver Chrome --driver-path C:\chromedriver.exe tests\test_reg_page_check.py -k "test_reg_page_check_all_fields_text"

