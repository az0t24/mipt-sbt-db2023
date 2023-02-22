## Задание
Согласно теореме CAP к какой части вы можете отнести СУБД:
+ DragonFly 
+ ScyllaDB
+ ArenadataDB

## Решение
Сформулируем ***теорему CAP***:

В любой реализации распределённых вычислений возможно обеспечить не более двух из трёх следующих свойств:
+ согласованность данных (consistency) — во всех вычислительных узлах в один момент времени данные не противоречат друг другу;
+ доступность (availability) — любой запрос к распределённой системе завершается корректным откликом, однако без гарантии, что ответы всех узлов системы совпадают;
+ устойчивость к разделению (partition-tolerance) — расщепление распределённой системы на несколько изолированных секций не приводит к некорректности отклика от каждой из секций.

### DragonFly
На [официальном сайте](https://dragonflydb.io/) в разделе _Highly Scalable_ написано, что _"Dragonfly is architected to scale vertically on a single machine, saving teams the cost and complexity of managing a multi-node cluster. For in-memory datasets up to 1TB, Dragonfly offers the simplest and most reliable scale on the market"_, что говорит нам о том, что система не может быть разделена на несколько машин, то есть **отсутствует** свойство **partition tolerance**.
Также на этом же сайте можно заметить, что выделяются такие качества, как производительность и эффективность. Откуда получаем, что система обладает свойствами **consistency** и **availability**.

Можем отнести ее к **CA**.

### ScyllaDB
На официальном сайте в разделе [глоссарий](https://docs.scylladb.com/stable/glossary.html) находим упоминание теоремы САР и то, что ScyllaDB реализует свойства **availability** и **partition-tolerance**, жертвуя при этом **consistency**.

Значит, можем отнести данную СУБД к **AP** (что также подтверждает [статья](https://docs.scylladb.com/stable/architecture/architecture-fault-tolerance.html)).

### ArenadataDB
Опять же переходим на [официальный сайт](https://arenadata.tech/products/arenadata-db/), где в первом же разделе нам сообщают, что ArenadataDB - аналитическая, распределённая СУБД, т. е. выполнено **partition-tolerance**. Прочитав информацию на сайте, мы также можем обнаружить раздел *Ключевые преимущества Arenadata DB*, где упоминается свойство **consistency**.

Таким образом, данную СУБД можно отнести к **CP**.
