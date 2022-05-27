"""
Чтобы обеспечить возможность отправки сигналов потомкам, не зная идентификаторы
их процессов, следует использовать группу процессов, ассоциирующую
дочерние процессы, что позволяет доставлять сигналы сразу всей группе. Группа
процессов создается при помощи функции os. setpgrp (), которая устанавливает
для идентификатора группы значение идентификатора текущего процесса. Все дочерние
процессы наследуют членство в группе от своего родителя. Поскольку эта
группа должна быть установлена только в оболочке, создаваемой объектом Popen и
его наследниками, то функция os. setpgrp () не должна вызываться в том же процессе,
в котором создается объект Popen. Вместо этого данная функция передается
конструктору Popen в качестве аргумента preexec_fn, так что огга выполняется после
вызова fork() в новом процессе до того, как использует функцию exec () для
выполнения оболочки. Отправка сигнала всей группе процессов осуществляется
при помощи функции os.killpg() со значением pid из экземпляра Popen.
"""
import os
import signal
import subprocess
import tempfile
import time
import sys


def show_setting_prgrp():
    print('Calling os.setpgrp() from {}'.format(os.getpid()))
    os.setpgrp()
    print('Process group is now {}'.format(os.getpid(), os.getpgrp()))
    sys.stdout.flush()


script = '''#!/bin/bash
echo "Shell script in process $$"
set -x
python3 singal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

if __name__ == '__main__':
    proc = subprocess.Popen(
        ['sh', script_file.name],
        preexec_fn=show_setting_prgrp
    )
    print('PARENT     : Pausing before signaling {}...'.format(proc.pid))
    sys.stdout.flush()
    time.sleep(1)
    print('PARENT     : Signaling process group {}'.format(proc.pid))
    sys.stdout.flush()
    os.killpg(proc.pid, signal.SIGUSR1)
    time.sleep(5)
