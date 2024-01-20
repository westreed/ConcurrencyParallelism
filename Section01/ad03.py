import logging
import threading
import time


def thread_func(name):
    logging.info(f"Sub-Thread {name}: starting")
    time.sleep(3)
    logging.info(f"Sub-Thread {name}: finishing")


if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s｜%(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', ))

    logging.info("Main-Thread: before running thread")

    # 서브 스레드 시작
    x.start()

    # x.join()
    # join()을 이용하면 메인 스레드가 자식 스레드의 작업이 끝날 때까지 대기함.

    logging.info("Main-Thread: wait for the thread to finish")

    logging.info("Main-Thread: all done")