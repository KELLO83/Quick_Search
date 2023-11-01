# Quick_Search


---
인공지능 처리부분 

1. GUI로부터 사용자가 탐색할 이미지 경로와 탐색할 객체 정보를 Main Controller 전달
2. Deep_Learning Controller 는 Multi Detect 실행 매개변수  img_path 전달
3. Multi Detect 실행도중 Filter.py 실행하여 찾고자하는 객체만 Pandas.DataFrame 업데이트 및 DataFrame의 정보를 .txt 파일로 저장
4. .txt 파일 기반으로 Deep_Learning Controller 에서 import crop을 호출하여 매개변수 .txt 파일의 경로 전달
5. crop 함수는 특정 디렉토리를 생성하여 crop된 이미지 저장
6. 만약 디렉토리 crop된 이미지중 image shpae (3,150,150) 미만일떄 (3,200,200) 증폭
7. 이후 처리된 이미지를 디렉토리에 전달하여 Main Contrller 전달

---
