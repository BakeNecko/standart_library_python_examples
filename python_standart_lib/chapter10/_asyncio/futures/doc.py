# 10.5.4 Асинхронное получение результатов
"""
Экземпляр Future представляет результат еще не завершенной работы. Цикл
событий может отслеживать переход экземпляра Future в состояние "выполнено" (done),
ем самым предоставляя возможность одной части приложения ожидать,
пока другая его часть завершит работу.
"""