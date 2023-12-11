import concurrent.futures
import math
def process_chunk(chunk_a, chunk_b):
    result_chunk = []
    for char_a, char_b in zip(chunk_a, chunk_b):
        if char_b == 'X':
            result_chunk.append(char_a)
        elif char_b == '0':
            result_chunk.append('0')
        elif char_b == '1':
            result_chunk.append('1')
        else:
            print("B 파일에 예상치 못한 문자가 있습니다.")
            exit()
    return ''.join(result_chunk)

def process_file_chunked(chunk_size, a_content, b_content, start_index, end_index):
    result_chunks = []
    for i in range(start_index, end_index, chunk_size):
        chunk_a = a_content[i:i+chunk_size]
        chunk_b = b_content[i:i+chunk_size]
        result_chunk = process_chunk(chunk_a, chunk_b)
        result_chunks.append(result_chunk)
    return result_chunks

if __name__ == "__main__":
    # A 파일 읽기
    with open('A', 'r') as file_a:
        a_content = file_a.read()

    # B 파일 읽기
    with open('B', 'r') as file_b:
        b_content = file_b.read()

    # 길이 확인
    if len(a_content) != len(b_content):
        print("A 파일과 B 파일의 길이가 다릅니다.")
        exit()

    # 병렬 처리를 위한 설정
    chunk_size = 1000000 # 적절한 크기로 조절
    num_chunks = math.ceil(len(a_content) / chunk_size)

    print(num_chunks)
    
    # 결과를 저장할 리스트
    result_chunks = []

    # ProcessPoolExecutor를 사용하여 병렬 처리
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        for i in range(num_chunks):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size
            future = executor.submit(process_file_chunked, chunk_size, a_content, b_content, start_index, end_index)
            futures.append(future)

        # 결과를 모으기
        for future in concurrent.futures.as_completed(futures):
            result_chunks.extend(future.result())

    # 결과 파일 쓰기
    with open('result', 'w') as result_file:
        result_file.write(''.join(result_chunks))

    print("합치기가 완료되었습니다.")