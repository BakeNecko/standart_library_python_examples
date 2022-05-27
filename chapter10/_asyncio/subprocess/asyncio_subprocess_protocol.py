# 10.5.12.1 Использование абстракции Protocol с подпроцессами
"""
В следующем примере сопрограмма запускает процесс, выполняющий команду
df в Unix, которая определяет размер свободного пространнства на локальных
дисках. Для запуска процесса и его связывания с классом Protocol, которому
известно, как прочитать вывод команды df и выполнить его синтаксический анализ,
используется метод subprocess_exec(). Методы класса Protocol вызываются автоматически
на основании событий ввода-вывода подроцесса. Посколько для аргументов stdin и stderr
устновленны знаения None, эти каналы передачи данных не подключены к новому процессу.
"""
import asyncio
import functools


async def run_df(loop: 'asyncio.AbstractEventLoop'):
    print('in run_df')

    cmd_done = asyncio.Future(loop=loop)
    factory = functools.partial(DFProtocol, cmd_done)
    proc = loop.subprocess_exec(
        factory,
        'df', '-hl',
        stdin=None,
        stderr=None,
    )
    try:
        print('launching process')
        transport, protocol = await proc
        print('waiting for process to complete')
        await cmd_done
    finally:
        transport.close()

    return cmd_done.result()


def _parse_results(output):
    """
    Вывод команды разбирается в последовательность словарей, сопоставляющих
    имена заголовков c их значениями для каждой строки вывода. Результирующий
    список является возвращаемым значением.
    """
    print('parsing results')
    # Вывод содержит одну строку заголовков, каждый из
    # которых представляет собой одно слово. Каждая
    # последующая строка соответствует отдельной файловой
    # системе, а столбцы соответствуют заголовкам
    # (предполагается, что имена точек монтирования не содержат пробелов).
    if not output:
        return []
    lines = output.splitlines()
    headers = lines[0].split()
    devices = lines[1:]
    return [
        dict(zip(headers, line.split()))
        for line in devices
    ]


class DFProtocol(asyncio.SubprocessProtocol):
    """
    Класс DFProtocol происходит от класса SubprocessProtocol, определяющего API,
    который позволяет классу обмениваться данными с другим процессом посредством каналов.
    В качестве аргумента done ожидается экземпляр Future, который будет использоваться
    вызывающим кодом для наблюдения за завершением процесса
    """
    FD_NAMES = ['stdin', 'stdout', 'stderr']

    def __init__(self, done_future: 'asyncio.Future'):
        transport: 'asyncio.SubprocessTransport'
        self.done = done_future
        self.buffer = bytearray()
        super(DFProtocol, self).__init__()

    def connection_made(self, transport: 'asyncio.SubprocessTransport'):
        """
        Как и в случае обмена данными через сокет, метод connection_made()
        вызывается при установлении входных каналов связи с новым процессом.
        Аргумент transport является экземпляром подкласса BaseSubprocessTransport.
        Он может читать выходные данные процесса и записывать данные в поток ввода
        процесса, если процесс был сконфигурирован для получения входных данных.
        """
        print('process startd {}'.format(transport.get_pid()))
        self.transport = transport

    def pipe_data_received(self, fd, data):
        """
        Если процесс сгенерировал вывод, вызывается метод pipe_data_received()
        c дескриптором с^айла, в который были записаны данные, и данные читаются из
        канала. Класс Protocol сохраняет данные, полученные из канала стандартного
        вывода процесса, в буфере для последующей обработки.
        """
        print(f'func: pipe_data_received | args: ("fd": {fd}, "data": {data})')
        print('read {} bytes from {}'.format(len(data), self.FD_NAMES[fd]))
        if fd == 1:
            self.buffer.extend(data)

    def process_exited(self) -> None:
        """
        При завершении процесса вызывается метод process_exited(). Код завершения
        можно получить c помощью объекта transport, вызвав метод get_returncode().
        В этом случае при условии отсутствия ошибок, доступный вывод декодируется
        и анализируется, прежде чем будет возвращен через экземпляр Future.
        Если же возникают ошибки, то предполагается, что результат пуст.
        Установка результата фьючерса информирует сопрограмму run_df()
        о завершении процесса, после чего закрываются ресурсы и возвращается результат.
        """
        print('proces_existed')
        return_code = self.transport.get_returncode()
        print('return code {}'.format(return_code))
        result = []
        if not return_code:
            cmd_output = bytes(self.buffer).decode()
            result = _parse_results(cmd_output)
        self.done.set_result((return_code, result))


if __name__ == '__main__':
    """
    Сопрограмма run_df() выполняется c помощью метода run_until_complete().
    Вывод содержит размер свободного пространства на каждом устройстве.
    """
    event_loop = asyncio.get_event_loop()
    try:
        return_code, results = event_loop.run_until_complete(
            run_df(event_loop)
        )
    finally:
        event_loop.close()

    if return_code:
        print(f'error exit {return_code}')
    else:
        print('\nFree space:')
        for r in results:
            print('{Mounted:25}: {Avail}'.format(**r))
    """
    Представленный ниже вывод показывает последовательность выполняемых
    действий и размер свободного пространства для каждого из дисков системы, 
    в которой выполняется данная программа
    """
