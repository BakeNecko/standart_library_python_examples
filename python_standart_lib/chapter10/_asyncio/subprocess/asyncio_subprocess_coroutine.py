# 10.5.12.2 Вызов подроцессов с использованием сопрограмм
# и потоков ввода-вывода
"""
Вместо получения доступа к процессам посредством подкласса Protocol их
можно запускать непосредственно c помощью сопрограмм путем вызова функции
create_subprocess_exec (), указав ей, следует ли подключать к каналам потоки
ввода-вывода stdout, stderr и stdin. Результатом порождения подпроцесса
сопрограммой является экземпляр Process, который можно использовать для
манипулирования подпроцессом и обмена данными c ним.
"""
import asyncio
import asyncio.subprocess
from python_standart_lib.chapter10._asyncio.subprocess.asyncio_subprocess_protocol import _parse_results


async def run_df():
    print('in run_df')

    buffer = bytearray()

    create = asyncio.create_subprocess_exec(
        'df', '-hl',
        stdout=asyncio.subprocess.PIPE,
    )
    print('lauching process')
    proc = await create
    print('process started {}'.format(proc.pid))
    """
    В этом примере команда df не нуждается в иных входных данных, кроме 
    аргументов командной строки, поэтому следующий шаг заключается в чтении всего
    вывода. В случае экземпляров Protocol невозможно контролировать, какой объем 
    данных читается за один раз. В этом примере для чтения данных используется
    метод readline(), но для чтения данных, не разбитых на строки, также можно
    было бы использовать метод read(). Выходные результаты команды буферизуются, 
    как и в примере, в котором использовался объект протокола, поэтому их 
    синтаксический анализ может быть выполнен позднее
    """
    while True:
        line = await proc.stdout.readline()
        print('read {!r}'.format(line))
        if not line:
            print('no more output from command')
            break
        buffer.extend(line)
    """
    Если больше нечего читать, поскольку программа закончила свою работу, то
    метод readline() возвращает пустую байтовую строку. Чтобы гарантировать 
    надлежащее закрытие ресурсов процессом, организуется ожидание его полного 
    завершения c помощью ключевого слова await.
    """
    print('waiting for process to complete')
    await proc.wait()
    """
    В этот момент можно проверить код завершения, чтобы определить, какие
    именно действия следует выполнить после того, как процесс перестал 
    предоставлять результаты: выполнить синтаксический анализ вывода или обработать
    ошибку. Логика анализа вывода команды остается той же, что и в предыдущем
    примере, но она вынесена в отдельную функцию (здесь не представлена) ввиду
    отсутствия класса протокола, в котором ее можно было бы скрыть. 
    После выполнения анализа данных результаты и код завершения 
    возвращаются вызывающему коду.
    """
    return_code = proc.returncode
    print(f'return code {return_code}')
    results = []

    if not return_code:
        cmd_output = bytes(buffer).decode()
        results = _parse_results(cmd_output)
    return return_code, results

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        return_code, results = event_loop.run_until_complete(
            run_df()
        )
    finally:
        event_loop.close()

    if return_code:
        print(f'error exit {return_code}')
    else:
        print('\nFree space:')
        for r in results:
            print('{Mounted:25}: {Avail}'.format(**r))
