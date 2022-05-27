import subprocess

if __name__ == '__main__':
    """stdout=subprocess.PIPE позволяет перехватить вызов для послед обработки"""
    completed = subprocess.run(
        ['ls', '-l'],
        stdout=subprocess.PIPE,
    )
    print('returncode: ', completed.returncode)
    print(f'Have {len(completed.stdout)} bytes in stodut: \n{completed.stdout.decode("utf-8")}')
