# 10.5.12.3 Отправка данных подроцессу
"""
В обоих предыдущих примерах использовался только один канал связи,
который обеспечивал чтение данных из второго процесса.
Часто возникает необходимость в передаче данных команде для последующей обработки.
Следующий пример определяет сопрограмму для выполнения команды tr в Unix, которая
преобразует символы, поступающие в ее входной поток. В данном случае
команда tr используется для преобразования букв из нижнего регистра в верхний.

Сопрограмма to_upper() получает в качестве аргумента входную строку и
порождает второй процесс, выполняющий команду "tr [:lower:] [:upper:]".
"""
import asyncio
import asyncio.subprocess


async def to_upper(input):
    print('in to_upper')

    create = asyncio.create_subprocess_exec(
        'tr', '[:lower:]', '[:upper:]',
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    print('launching process')
    proc = await create
    print(f'pid {proc.pid}')
    """
    Затем сопрограмма to_upper() использует метод communicate() экземпляра
    Process для отправки входной строки команде и читает весь результирующий
    вывод в асинхронном режиме. Как и в случае версии того же метода для экземпляра 
    subprocess.Popen, метод communicate() возвращает все байтовые строки,
    выводимые этим методом. Если же команда может выводить слишком большой
    объем данных, которые будут потреблять много памяти, или же входные данные
    не могут быть предоставлены все сразу, или вывод должен обрабатываться инкрементно, 
    то, возможно, вместо вызова метода communicate() лучше использовать непосредственно 
    дескрипторы stdin, stdout и stderr экземпляра Process.
    """
    print('communication with process')
    stdout, stderr = await proc.communicate(input.encode())
    """
    После выполнения операций ввода-вывода организуется ожидание полного 
    завершения процесса, что гарантирует корректное выполнение операций 
    по освобождению ресурсов.
    """
    print('waiting for process to complete')
    await proc.wait()
    """
    Далее можно проверить код завершения процесса, декодировать выходную
    байтовую строку и сформировать на основании этого результат, возвращаемый 
    сопрограммой
    """
    return_code = proc.returncode
    print(f'return code {return_code}')
    results = ''
    if not return_code:
        results = bytes(stdout).decode()
    return return_code, results


if __name__ == '__main__':
    """
    В основной части программы задается строка сообщения, которую необходимо 
    преобразовать, создается цикл событий для выполнения сопрограммы to_upper() 
    и выводятся результаты.
    """
    MESSAGE = """This message will be converted to all caps."""

    event_loop = asyncio.get_event_loop()
    try:
        return_code, results = event_loop.run_until_complete(
            to_upper(MESSAGE)
        )
    finally:
        event_loop.close()
    if return_code:
        print(f'error exit {return_code}')
    else:
        print('Original: {!r}'.format(MESSAGE))
        print('Changed : {!r}'.format(results))
    """
    Вывод отображает последовательность выполняемых операций, 
    а также исходное и преобразованное сообщения.
    """