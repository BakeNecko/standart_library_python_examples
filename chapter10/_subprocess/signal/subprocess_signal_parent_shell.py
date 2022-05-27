"""
Группы/сеансы процессов

Если процесс, созданый экземпляром Popen, порождает подпроцессы,
то эти дочерние процессы не будут получать сигналы, посланные их родителю.
Как следствие, если исп. аргумент shell в конструкторе Popen, то будет нелегко
прекратить выполенение команды, запущенной в оболочке, путем отправки сигнала SIGINT/SIGTERM
"""
import os
import signal
import subprocess
import tempfile
import time
import sys

script = '''#!/bin/bash
echo "Shell script in process $$"
set -x
python3 singal_child.py
'''
script_file = tempfile.NamedTemporaryFile('wt')
script_file.write(script)
script_file.flush()

if __name__ == '__main__':
    proc = subprocess.Popen(['sh', script_file.name])
    print('PARENT      : Pausing before signaling {}...'.format(proc.pid))
    sys.stdout.flush()
    time.sleep(1)
    print('PARENT      : Signaling chile {}'.format(proc.pid))
    sys.stdout.flush()
    os.kill(proc.pid, signal.SIGUSR1)
    time.sleep(3)
