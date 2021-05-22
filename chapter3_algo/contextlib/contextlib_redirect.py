# 3.4.6
# Плохо спроектированный библиотечный код может осуществлять запись данных
# непосредственно в поток sys.stdout или sys.stderr, не предоставляя аргументов,
# позволяющих конфигурировать другие варианты вывода. В подобных
# случаях, когда возможность доступа к исходному коду для внесения в него изменений,
# позволяющих управлять выводом c помощью аргумента, отсутствует, можно
# перехватывать вывод c помощью менеджеров контекста redirect_stdout() и redirect_stderr().
from contextlib import redirect_stderr, redirect_stdout
import io
import sys


def misbehaving_function(a):
    sys.stdout.write('(stdout) A: {!r}\n'.format(a))
    sys.stderr.write('(stderr) A: {!r}\n'.format(a))


capture = io.StringIO()

with redirect_stdout(capture), redirect_stderr(capture):
    misbehaving_function(5)
print(capture.getvalue())

# Оба менеджера контекста,
# redirect_stdout () и redirect__stderr (), изменяют глобальное
# состояние, подменяя объекты, содержащиеся в модуле sys (раздел 17.2); по этой
# причине их следует использовать c осторожностью. Фактически эти функции не являются
# потокобезопасными, поэтому их вызовы в многопоточном приложении могут приводить к
# неопределенным результатам. Кроме того, они могут взаимодействовать c другими операциями,
# которые рассчитывают на подключение стандартных потоков вывода к
# терминальным устройствам.