# Написать декоратор @thread_async, который будет вызывать декорируемую функцию в отдельном потоке и
# возвращать временный объект-представитель AsyncResult. Он должен представлять два метода:
#
# is_ready() - возвращает True, если фоновое вычисление завершилось, иначе False.
#
# get_value() - возвращает результат, если фоновое вычисление завершено, иначе засыпает, пока результат
# не будет посчитан и потом все равно возвращает его.
from threading import Thread


def thread_async(function_to_decorate):
    def wrapper(*args):
        class AsyncResult(Thread):
            def __init__(self, func, args):
                Thread.__init__(self)
                self.func = func
                self.args = args
                self.result = None
                return

            def run(self):
                print('Я в run')
                self.result = self.func(*self.args)

            def is_ready(self):
                print('Я в is_ready, %s', self.isAlive())
                return not self.isAlive()

            def get_value(self):
                if self.is_ready():
                    print('Я в get_value true')
                    return self.result
                else:
                    while not self.is_ready():
                        print('Я в get_value false')
                        self.join()
                    print("FINISHED")
                    return self.result

        print("Передали ли мне что-нибудь?:")
        print(args)
        b = AsyncResult(function_to_decorate, args)
        b.start()
        return b
    return wrapper


@thread_async
def factorial(n):
    fac = 1
    i = 0
    while i < n:
        i += 1
        fac = fac * i
    return fac


if __name__ == '__main__':
    a = factorial(150000)
    print(a.get_value())
