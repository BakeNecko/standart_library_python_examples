"""
10.4 multiprocessing: использование процессов вместо потоков
Doc: https://docs.python.org/3/library/multiprocessing.html

Модуль multiprocessing включаетАИ, обеспечивающий распределение работы
 между несколькими процессами на основе API многопоточной обработки
(см. раздел 10.3). В некоторых случаях использование процессов вместо потоков
позволяет организовать параллельное выполнение задачи c использованием
нескольких ядер CPU, реализация чего c помощью потоков невозможна из-за
глобальной блокировки интерпретатора Python.

В силу сходства модулей multiprocessing и threading первые несколько
примеров, приведенных в этом разделе, — это видоизмененные версии ранее
рассмотренных примеров многопоточной обработки. Последующие примеры
иллюстрируют возможности, предоставляемые модулем multiprocessing,
но недоступные в модуле threading.

В зависимости от платфомы, выбирается 1н из 3х методов запуска доп. процесса:
1. fork - Родительский процесс использует os.fork() для форка интерпретатора Python.
          Дочерний процесс, когда он запускается, фактически идентичен родительскому процессу.
          Все ресурсы родительского процесса наследуются дочерним процессом.
          Обратите внимание, что безопасное форкирование многопоточного (multithreaded) процесса проблематично.
          Доступно только в Unix. По умолчанию в Unix.

2. spawn - Родительский процесс запускает новый процесс интерпретатора python.
           Дочерний процесс наследует только те ресурсы, которые необходимы для выполнения метода run() объекта process.
           В частности, ненужные дескрипторы файлов и хэндлы от родительского процесса не будут унаследованы.
           Запуск процесса с помощью этого метода довольно медленный по сравнению с использованием fork или forkserver.
           Доступен в Unix и Windows. По умолчанию используется в Windows и macOS.

3. forkserver - Когда программа запускается и выбирает метод запуска forkserver, запускается серверный процесс.
                С этого момента всякий раз, когда требуется новый процесс, родительский процесс подключается
                к серверу и запрашивает у него fork нового процесса. Процесс fork-сервера является однопоточным,
                поэтому для него безопасно использовать os.fork(). Никакие ненужные ресурсы не наследуются.
                Доступен на платформах Unix, поддерживающих передачу файловых дескрипторов по трубам Unix.
"""