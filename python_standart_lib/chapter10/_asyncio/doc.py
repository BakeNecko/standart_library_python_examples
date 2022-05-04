# 10.5 asyncio: Асинхронные операции ввода-вывода цикл обытий и инструменты параллелизма
"""
Модуль asyncio предоставляет инструменты для создания приложений,
основнный на выполнении параллельный вычисленний с исп. сопрограмм.
В то время как модуль threading (10.3) рализует параллелизм вычислений
на основе потоков выполнения, а модуль multiprocessing (10.4) - на основе
исп. системных процессов, модуль asncio исп. подход на основе единственного
потока и единственного процесса, в котором отдельные части приложение кооперируются
для явного переключение задач в наиболее подходящие для этого моменты времени.
Чаще всего такой контекст переключния возникает тогда, когда при иной организации
работы программы она блокировалась бы, ожидания заверщения операций чтения или записи данных (I/O).
Однако модуль asyncion также позволяет откладывать выполнение кода на опред. будущий момент времени,
чтобы одна сопрограмма могла ожидать пока выполнится другя, завершится обработка системных сигналов или
распознаются другие события, которые могут стать причиной того, чтобы приложение изменило вычисления,
выполняемые в данный момент.

10.5.1 Принципы асинхронного параллелизма:
Большинство программ, в которых используются другие модели параллельных
вычислений, следует линейному стилю и основываются на соответствующем
изменении контекста за счет привлечения базовых средств управления
потоками и процессами, предлагаемых средой времени выполнения или
операционной системой. В случае приложений, основанных на использовании
модуля asyncio, требуется, чтобы код приложения явно обрабатывал изменения
контекста, используя для этого методы, которые корректно учитывают
несколько взаимосвязанных понятий.

В предлагаемом модулем asyncio фреймворке центральное место занимает
цикл событий — объект первого класса, ответственный за эффективную обработку
событий ввода-вывода и изменение контекста приложения. Предоставляются
несколько реализаций цикла событий, что обеспечивает наиболее эффективное
использование возможностей конкретной операционной системы. В то время как
обычно автоматически выбирается вариант цикла, предусмотренный по умолчанию,
существует возможность выбора определенной реализации цикла событий
самим приложением. Например, такой вариант может быть полезным при работе
под управлением Windows, где некоторые классы добавляют поддержку внешних
процессов способом, который может компенсировать неэффективность средств
сетевого ввода-вывода.

Приложение взаимодействует c циклом событий явным образом, регистрируя
подлежащий выполнению код и позволяя циклу событий выполнять необходимые
вызовы в коде приложения, если доступны ресурсы. Например, сетевой сервер
может открыть сокеты, а затем зарегистрировать их для получения уведомлений
о наступлении событий, представляющих интерес. Цикл событий может известить
сервер об установлении нового соединения или доступности новых данных, ожидающих
чтения. Ожидается, что код приложения должен вновь уступать управление, если в
данном контексте для него уже нет работы. Например, если в сокете больше нет данных,
которые следует прочитать, то сервер должен вновь вернуть управление циклу событий.

Механизм возврата управления циклу событий основан на использовании сопрограмм Python
— специальных функций, уступающих управление вызвавшему их коду без потери своего состояния.
Сопрограмма (очень похожи на функции-генераторы) — это конструкция языка, предназначенная
для параллельного выполнения операций. При вызове функции сопрограммы создается объект
сопрограммы, и вызывающий код может выполнить код этой функции, используя метод send()
объекта сопрограммы. Сопрограмма может приостановить выполнение, используя ключевое
слово await совместно c именем другой сопрограммы. На протяжении такой паузы состояние
сопрограммы сохраняется, что позволяет ей при пробуждении продолжить выполнение c
той точки, в которой оно было прервано.

В действительности в версиях Python, предшествующих версии 3.5, генераторы позволяют
реализовать сопрограммы без их поддержки со стороны платформы. Кроме того, модуль
asyncio предоставляет слой абстрагирования каналов и протоколов передачи данных
на основе классов, предназначенный для написания кода, в котором используются
функции обратного вызова вместо сопрограмм. В обеих моделях, классической и
основанной на сопрограммах, явное изменение контекста посредством повторного
вхождения в цикл событий заменяет его неявное изменение в рамках реализации
многопоточной модели Python.

Фьючерс(Future) — это структура данных, представляющая результат работы, которая
еще не завершена. Цикл событий может отслеживать переход объекта Future в
состояние “выполнено”, тем самым предоставляя возможность одной части приложения
ожидать, пока другая его часть завершит работу. Кроме фьючерсов модуль asyncio
включает другие примитивы параллелизма, такие как блокировки и семафоры.

Task — это подкласс Future, которому известно, как обернуть сопрограмму и
управлять ее выполнением. Цикл событий планирует выполнение задач на те
моменты времени, когда необходимые им ресурсы становятся доступными,
а производимые ими результаты могут быть использованы другими сопрограммами.
"""
