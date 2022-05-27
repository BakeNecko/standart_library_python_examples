"""
Popen - Класс который предоставляет больше возможностей контроля
над выполнением команд и обработкой потоков ввода-вывода.

communicate() - читает весь вывод и ожидает завершения дочернего процесса,
прежде чем вернуть управление. Помимо этого сущ. возможнсоть читать и записывать
информацию с помощью отдельных дескрипторов каналов, исп. экземпляров Popen для инкрементного
обмена данными по мере выполнения программы.
"""
import subprocess

if __name__ == '__main__':
    proc = subprocess.Popen(
        'cat -; echo "to stderr" 1>&2',
        shell=True,
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    msg = 'throught stdin to stdout\n'.encode('utf-8')
    stdout_value, stderr_value = proc.communicate(msg)
    print('combined output: ', repr(stdout_value.decode('utf-8')))
    print('stderr value   :', repr(stderr_value))
