import subprocess

if __name__ == '__main__':
    completed = subprocess.run(['ls', '-l'])
    print('returncode:', completed.returncode)
    # установка знач. True для аргумента shell функции run() порождает вспомог. просецц оболочки,
    # в котором затем и выполняется команда
    completed = subprocess.run('echo $HOME', shell=True)
    print('returncode (with shell=True):', completed.returncode)
