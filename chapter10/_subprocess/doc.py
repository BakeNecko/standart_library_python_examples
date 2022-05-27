"""
Модуль subprocess отвечает за выполнение следующих действий:
 1. порождение новых процессов
 2. соединение c потоками стандартного ввода, стандартного вывода,
 3. стандартного вывода сообщений об ошибках и получение кодов возврата от этих процессов

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
- выполняет команду, описанную args. Ожидает завершения команды, а затем возвращает код возврата.
----------------------------------------------------------------------------------------------
subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
- выполняет команду, описанную args. Ожидает завершения команды, а затем завершается, если код возврата 0,
или поднимает исключение CalledProcessError, объект которого возвращает код завершения атрибутом returncode
----------------------------------------------------------------------------------------------
subprocess.check_output(
args, *, input=None, stdin=None, stderr=None,
shell=False, universal_newlines=False, timeout=None,
)
- выполняет команду и возвращает её вывод. Поднимает исключение CalledProcessError, если код возврата ненулевой.
----------------------------------------------------------------------------------------------
subprocess.check_output(
args, *, input=None, stdin=None, stderr=None,
shell=False, universal_newlines=False, timeout=None,
)
выполняет команду и возвращает её вывод. Поднимает исключение CalledProcessError, если код возврата ненулевой.
----------------------------------------------------------------------------------------------
subprocess.DEVNULL - значение, которое может использоваться в качестве аргумента stdin, stdout или stderr.
Означает, что будет использован специальный файл devnull.

subprocess.PIPE - значение, которое может использоваться в качестве аргумента stdin, stdout или stderr.
Означает, что для дочернего процесса будет создан пайп.

subprocess.STDOUT - значение, которое может использоваться в качестве аргумента stderr.
Означает, что поток ошибок будет перенаправлен в поток вывода.
----------------------------------------------------------------------------------------------
subprocess.Popen(
    args, bufsize=-1, executable=None, stdin=None, stdout=None,
    stderr=None, preexec_fn=None, close_fds=True, shell=False,
    cwd=None, env=None, universal_newlines=False, startupinfo=None,
    creationflags=0, restore_signals=True, start_new_session=False,
    pass_fds=()
)
Выполняет программу в новом процессе. args – строка или последовательность аргументов программы.
Обычно первым указывают исполняемую программу, а затем аргументы, но также ее можно указать в параметре executable.

with Popen(["ifconfig"], stdout=PIPE) as proc:
    log.write(proc.stdout.read())

Popen.poll() - если процесс завершил работу - вернёт код возврата, в ином случае None.

Popen.wait(timeout=None) - ожидает завершения работы процесса и возвращает код возврата.
Если в течение timeout процесс не завершился,
поднимется исключение TimeoutExpired

Popen.communicate(input=None, timeout=None) - взаимодействовует с процессом: посылает данные, содержащиеся в input
в stdin процесса, ожидает завершения работы процесса, возвращает кортеж данных потока вывода и ошибок.
При этом в Popen необходимо задать значение PIPE для stdin (если вы хотите посылать в stdin),
stdout, stderr (если вы хотите прочитать вывод дочернего процесса).

Popen.send_signal(signal) - посылает сигнал signal.

Popen.terminate() - останавливает дочерний процесс.

Popen.kill() - убивает дочерний процесс.
"""
