# jstory - backend
---
#### consistently development
___

kakao login 으로 부터 access_token 받는 로직 구현

1. kakao login으로 부터 access_token 발행 [개발자 문서-token](https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#request-token)
  - 초기 로그인 요청이 들어오면 redirect_url(/oauth) 로 연결 한 다음 callback 주소로 부터 받은 code 를 통해서 access_token 발행
2. Database 를 통해서 카카오로 부터 받은 사용자 정보로 회원 가입 [개발자 문서-사용자 정보 가져오기](https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#req-user-info)
3. 로그아웃
4. 연결끊기 

백엔드 서버 작업 목록

1. 구현 코드 작성
2. 각 구현부 도커 작업
  - fastapi, uvicorn, nginx, database
3. 도메인 작업 후 서버 배포

fastapi 실행

```bash
$ uvicorn main:app --reload
```
