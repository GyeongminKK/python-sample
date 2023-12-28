import multiprocessing
import time

def worker(index):
    print(f"Worker {index} started")
    time.sleep(2)
    print(f"Worker {index} finished")

if __name__ == "__main__":
    print("Main process started")

    processes = []

    # 3개의 프로세스 생성
    for i in range(3):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)
        process.start()

    # 모든 프로세스가 종료될 때까지 기다림
    for process in processes:
        process.join()

    print("Main process finished")