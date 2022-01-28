<br>

# Django로 만드는 맛집 프로젝트[2팀]  

<br>

## **개발환경**
+ PyCham Community 
+ GitHub

<br>

## **사용 기술**
  ### **백엔드**   
  + Python(3.9)
  + Django
  + DJango ORM
     
 ### **데이터베이스**
  + Mysql

 ### **프론트엔드**
  + Javascript
  + HTML, CSS

<br>

  ## **주요 키워드**
  + REST API
  + Git 관리

<br>

  ## **구현 기능**
  + **user app**
    + 회원가입/회원탈퇴 로직
    + 로그인/로그아웃 로직 + 소셜네트워크 로그인
    + 회원수정/암호변경/ID찾기
    + 이메일인증
     
  + **hplace app**
    + 게시글 작성/수정/삭제    
    + 각 상점 위치 GPS 지도
    + 실시간 날씨 api
    + 실시간 누적방문자 api
   
  + **comments app**
    + 코멘트 작성/삭제
  
  <br><br>
  
  ## **시스템 구조**
  ![image](https://user-images.githubusercontent.com/97924823/151324844-d1bc32f2-e43f-4139-b02e-0918374a3b12.png)
  
  
  ## **ERD 구조**
![KakaoTalk_20220127_145038159](https://user-images.githubusercontent.com/96184680/151300028-0553fcc6-ff9d-4946-935d-37a727c17c6d.png)
  
  <br><br>
  
  ### **프로젝트 진행 과정 중 핵심 문제점과 해결방법**
  
   임홍인
   >**1. 구글 네이버 api**<br>
   > **문제점** : 소셜네트워크(구글, 네이버)를 활용해 로그인을 할 수 있는 기능 + DB연동 오류
   ><br>
   > **해결방안** : Django 라이브러리 'allauth'를 활용하여 superuser를 생성하고 각 소셜네트워크(구글, 네이버) 개발자 사이트에서 Client ID와 Secret Code 값을 얻고,
   localhost:8000/admin 관리자페이지에서 적용 후 각 개발자사이트에 리디렉션(callback)링크에 값을 설정한다. ex. 메인도메인 구글 172.0.0.1/8000, 네이버 localhost:8000/
       
   <br>
   
   안현동
   >1. 카카오 지도 api
   >>**A. http 프로토콜 사용시 HTML5 위치정보 사용제한**<br>
   >> 문제점 : http와 같이 보안설정이 되지 않은 사이트에서 사용자의 위치를 Geolocation API를 사용할 수 없음*<br>
   >> 해결방안 : SSL 인증서를 발급받아 https 프로토콜로 변환<br><br>
   >>**B. SSL 인증서 발급**<br>
   >> 문제점 : Window용 Let's Encrypt로 SSL인증서를 발급받으려 했으나 시간의 한계가 있었음<br>
   >> 해결방안 : ngrok이라는 로컬 컴퓨터의 개발 환경을 인터넷으로 공유해주는 툴을 사용해 테스트 시도<br><br>
   >>**C. 카카오 지도 마커<br>**
   >> 문제점 : 현재위치와 도착위치를 설정했으나 출발마커와 도착마커의 구분에 한계<br>
   >> 해결방안 : 현재, 도착위치의 마커 이미지를 따로 설정해 표기<br>

<br>

  송화랑
  
   > 문제점 : 게시글에 댓글 작성란을 만들어서 댓글을 작성하면 url이 바뀌지않고 그 게시글에 출력되는 방법으로 하려고 예정, 하지만 생각보다 복잡해서 따로 댓글 작성, 댓글 리스트 html을                      만드려고했으나 조금 더 노력을 하여 결국 원래 예정대로 구현<br>
   > 해결방안 : 댓글작성란 중 바뀌는 부분(사용자이름, 작성시간, 내용)을 변수로 바꿈, 댓글내용을 저장하고 게시글로 redirect해주는 함수를 사용하여 게시글로 보내줌
   

   > 문제점 : 구글 애널리틱스에 대해 알아보는데만 많은 시간이 소요되었고 어떻게 사용해야하는건지 이것저것 시도할 때도 많은 시간이 소요 하지만 실수를 발견하고 줄여가며                                      결국 홈페이지에 방문자수 표기를 구현<br>
   > 해결방안 : 구글 api의 서비스계정 안에 있는 json파일, 구글 애널리틱스 설정에서 서비스계정 등록, python에서 구글 클라이언트 설치/json파일 경로 설정/구글 애널리틱스 id 등록을 통해                       모두 연동케 함, 출력값을 홈페이지에 구현

<br>

   유재중
   >**Email 인증**<br>
   > **문제점** : 회원가입의 Email 인증(토큰 값을 사용)을 적용 시키는 기능
   ><br>
   > **해결방안** : 랜덤 숫자 발송 및 입력을 통한 인증 방식을 사용 및 Email 자동 저장으로 사용자가 별도 수정 불가, 차후 발송 값에 토큰을 활용한 하이퍼링크 적용으로 구현 예정
       
<br>
   



