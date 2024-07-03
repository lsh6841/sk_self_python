import os,time
import re
#이메일 패턴
email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
MY_PATH = "./7_2/"

def find_file(f,path,dirlist2):
    while(1):
            dirlist1 = os.listdir(f"{MY_PATH}static")
            if(dirlist1 != dirlist2):
                #파일 수정 시간
                t = time.strftime("%H:%M:%S")
                #파일 추가
                diff1 = set(dirlist1) - set(dirlist2)
                #파일 삭제
                diff2 = set(dirlist2) - set(dirlist1)
                if diff1:
                    for file in diff1:
                        print(f"{t} {file}추가")
                        f.write(f"{t} {file}추가\n")
                        f.write("----------\n")
                        with open(f"{MY_PATH}static/{file}",'r',encoding='utf-8') as file:   
                            lines = file.readlines()
                            for num, line in enumerate(lines):
                                if line.startswith(("#","//")):
                                    print(f"{num}번째 줄 : {line}",end='')
                                    f.write(f"{num}번째 줄 : {line}")
                                em = email_pattern.findall(line)
                                if em:
                                    print(f"{num}번째 줄 이메일 : {em}")
                                    f.write(f"{num}번째 줄 이메일 : {em}")
                        f.write("\n----------\n")   
                if diff2:
                    for file in diff2:
                        print(f"{t} {file}삭제")
                        f.write(f"{t} {file}삭제\n")
                #break
            dirlist2 = dirlist1
            time.sleep(1)
            f.flush()

dirlist2 = os.listdir(f"{MY_PATH}static")
count = 0

#파일이 존재하면 'a'옵션으로 로그 추가
if f"{time.strftime("%m")}월_{time.strftime("%d")}일_보고서.txt" in os.listdir(f"{MY_PATH}quiz"):
    with open(f"{MY_PATH}quiz/{time.strftime("%m")}월_{time.strftime("%d")}일_보고서.txt","a",encoding="utf-8") as f:
       find_file(f,f"{MY_PATH}static",dirlist2)
#파일이 존재x 파일 포맷 작성 후 로그 추가
else:
    with open(f"{MY_PATH}quiz/{time.strftime("%m")}월_{time.strftime("%d")}일_보고서.txt","w",encoding="utf-8") as f:
        f.write(f"{time.strftime("%m")}월_{time.strftime("%d")}일 보고서\n작성자:이승훈\n주요 내용:신규 파일 탐지\n")
        find_file(f,f"{MY_PATH}static",dirlist2)
        
