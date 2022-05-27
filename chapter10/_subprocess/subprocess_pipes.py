"""
Соединение сегментов канала.
Несколько команд можно соеденить, чтобы они образовали конвейер
в стиле оболочки Unix, создав отдельные экземпляры Popen и объединив
в одну цепочку их каналы ввода и вывода.
"""
import subprocess

cat = subprocess.Popen(
    ['cat', '$HOME/.bashrc'],
    stdout=subprocess.PIPE,
)

grep = subprocess.Popen(
    ['grep', 'export'],
    stdin=cat.stdout,
    stdout=subprocess.PIPE
)

cut = subprocess.Popen(
    ['cut', '-f', '3', '-d:'],
    stdin=grep.stdout,
    stdout=subprocess.PIPE,
)

if __name__ == '__main__':
    end_of_pip = cut.stdout
    print('Included files:')
    for line in end_of_pip:
        print(line.decode('utf-8').strip())
