import threading
import urllib
from queue import Queue
from urllib.parse import urlparse

import feedparser

num_fetch_threads = 2
enclosure_queue = Queue()

feed_urls = [
    'http://talkpython.fm/episodes/rss',
]


def message(s):
    print('{}: {}'.format(threading.current_thread().name, s))


def download_enclosures(q):
    """Это функция рабочего потока.
    Она обрабатывает элементы очереди один за другим.
    Потоки этого процесса-демона входят в бесконечный цикл
    и завершаются, только когда завершается осно. поток.
    """
    while True:
        message('looking for the nex enclosure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()


if __name__ == '__main__':
    for i in range(num_fetch_threads):
        worker = threading.Thread(
            target=download_enclosures,
            args=(enclosure_queue,),
            name=f'worker-{i}',
        )
        worker.setDaemon(True)
        worker.start()

    for url in feed_urls:
        response = feedparser.parse(url, agent='fetch_podcasts.py')
        for entry in response['entries'][:5]:
            for enclosure in entry.get('enclosures', []):
                parsed_url = urlparse(enclosure['url'])
                message(f'queuing {parsed_url.path.rpartition("/")[-1]}')
                enclosure_queue.put(enclosure['url'])

    message('*** main thread waiting')
    enclosure_queue.join()
    message('*** done')
