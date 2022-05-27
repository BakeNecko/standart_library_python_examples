"""
Модуль weakref обеспечивает поддержку слабых ссылок на объекты.
Создание обычный сслыки приводит к увеличенияю счётчика ссылок на объект,
что препядствует его удалению сборщиком мусора.

Особенность слабой ссылки в том, что она позволяет ссылаться на объект,
не препядствуя его автоматическому удалению.
"""