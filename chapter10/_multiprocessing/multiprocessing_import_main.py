"""
Одним из отличий примеров, иллюстрирующих многопроцессную обработку,
от примеров, которые приводились при обсуждении многопоточности, является
дополнительная защита той части кода, которая должна выполняться только при
запуске сценария как основной программы. В силу особенностей способа запуска
новых процессов дочерний процесс должен иметь возможность импортировать
сценарий, содержащий целевую функцию. Обертывание основной части приложения
кодом проверки на __main_ гарантирует, что она не будет выполняться
рекурсивно в каждом дочернем процессе при импортировании модуля. Целевую
функцию можно также импортировать из другого сценария. Например, в сценарии
multiprocessing_import_main.py используется рабочая функция, определенная
в другом модуле. Зачастую необх. в доп. защите возникает при использовании метода
spawn (Windows)
"""
import multiprocessing
import multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(
            target=multiprocessing_import_worker.worker
        )
        jobs.append(p)
        p.start()