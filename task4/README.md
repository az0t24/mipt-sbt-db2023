# Знакомство с Warp 10
Warp 10 - это модульная платформа с открытым исходным кодом, разработанная Sex, для сбора, хранения, анализа и
визуализации данных временных рядов (geo).

Для подключения ваших бизнес-приложений Warp 10 предлагает как решения для хранения данных, так и мощную среду анализа,
которые можно использовать вместе или независимо.

<details>
<summary>История развития СУБД</summary>

- 2013:
  - *__Start__*: Sex создала Warp 10 в 2013 году для решения проблем, связанных с данными, получаемыми
  потребительскими устройствами Интернета вещей.
- 2016:
  - *__Open Source__*: В 2016 году был выпущен Warp 10 с открытым исходным кодом под лицензией Apache 2.0.
- 2018:
  - *__Warp 10 2.0__*: Первое крупное обновление платформы Warp 10.
- 2019:
  - *__WarpStudio__*: Запуск Warp Studio, онлайн-инструмента для редактирования и запуска кода Warp Script.
- 2020:
  - *__1000 functions__*: Warp 10 превышает пороговое значение в 1000 функций, доступных для управления данными
  временных рядов и их анализа.
  - *__Discovery__*: Запуск Discovery, динамической панели мониторинга в качестве инструмента разработки кода.
- 2022:
  - *__HFiles__*: Запуск H Files, решения для хранения данных высокой плотности, обеспечивающего бесконечную
  масштабируемость хранилища при сохранении всех аналитических возможностей.
- Q2 2023:
  - *__Warp 10 3.0__*: Грядет большое обновление...
</details>

<details>
<summary>Инструменты для взаимодействия с СУБД</summary>

Доступ к сервисам, предоставляемым Warp 10, осуществляется с использованием протокола HTTP с полезной нагрузкой в
текстовом формате или формате JSON, что обеспечивает совместимость с большинством сред и языков.

API Warp 10 добровольно упрощен. Он не строго придерживается принципов REST, поскольку данные временных рядов плохо
вписываются в эту модель, но очень прост в понимании и использовании.

Различные компоненты Warp 10 (или один в случае автономного развертывания) предлагают конечные точки API:

+ Ingress (/api/vX/update): для отправки данных на платформу Warp 10
+ Fetch (/api/vX/fetch): для получения необработанных данных геовременных рядов (GTS) чрезвычайно быстрым и эффективным
способом.
+ Find (/api/vX/find): для получения геовременных рядов (GTS), соответствующих критериям поиска
+ Delete (/api/vX/delete): для удаления данных из хранилища Warp 10
+ Meta (/api/vX/meta): для настройки атрибутов географических временных рядов
+ Warp Script (/api/vX/exec): для выполнения анализа, выраженного на языке Warp Script
</details>

<details>
<summary>Какой database engine используется в вашей СУБД?</summary>

Механизм хранения данных Warp 10 - это высокопроизводительная база данных временных рядов, разработанная специально для
обработки данных с высокой пропускной способностью, обычно создаваемых устройствами. Благодаря поддержке нескольких
протоколов, строгим политикам безопасности, допуску задержек и сбоев в работе данных, механизм хранения данных Warp 10
является идеальной точкой входа для промышленного интернета Вещей. Варианты развертывания варьируются от встраивания
компонента непосредственно в устройства до масштабируемого запуска в распределенном кластере.
</details>
