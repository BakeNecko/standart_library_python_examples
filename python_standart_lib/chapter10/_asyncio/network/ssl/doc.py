# 10.5.10 Использование SSL
"""
В модуле asyncio предусмотренна встроенная поддержка протокола SSL при
обмене данными через сокеты. Передача экземпляра SSLContext сопрограммам,
создающим серверные или клиентские соединения, активизирует эгу поддержку
и гарантирует настройку параметров SSL-протокола, прежде чем сокет будет
предоставлен приложению для использования.

Рассмотренные в предыдущем разделе эхо-сервер и эхо-клиент на основе
сопрограмм можно легко обновить для использования протокола SSL,
внеся незначительные изменения. Первый шаг заключается в создании
файлов сертификата и ключа. Команда наподобие следующей позволяет
создать самоподписанный сертификат.

$ openssl req -newkey rsa:2048 -nodes -keyout pymotw.key  -x509 -days 365 -out pymotw.crt
"""