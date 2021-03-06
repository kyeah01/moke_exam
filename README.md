# WEB 월말평가 대비

> 웹 월말평가를 대비하여 Django 예시문제를 출제하였습니다.
>
>1~2차 공지를 통하여
>
>- model form을 사용한 CRUD구현
>- 회원가입, 로그인, 로그아웃, 좋아요 시스템 구현
>- forms.py, templates, views.py부분에 문제가 출제됨
>
>등이 공개되었습니다.
>
>
>
>시험에서 명심할 점
>
>- 명세의 파일명, 변수명을 완벽하게 따라야 함.
>- 미리 작성된 프로젝트에 지정된 공백(주석)아래에 답을 작성하여야 합니다.
>- import 관련 문제가 나올 수 있습니다.



### 예상문제

1. 로그인 뷰를 구현하려고 한다. GET방식으로 로그인에 필요한 form을 제공하고, POST방식으로 form을 받아 로그인을 수행하려고 한다. 아래의 조건을 만족하는 view를 작성하시오.

   1. GET방식으로 로그인에 필요한 form을 제공하려고 한다.

   2. POST방식으로 로그인에 필요한 데이터를 받고, 로그인하려고 하는 사용자를 검증한 다음 로그인시킨다.

      

2. 회원가입 view를 구현하려고 한다. 아래의 조건을 만족하는 view를 작성하시오.

   1. GET방식으로 회원가입에 필요한 form을 제공하려고 한다.

   2. POST방식으로 회원가입에 필요한 데이터를 받고, 사용자를 회원가입 시킨다.

   3. 회원가입시 페이지에서 현재까지 회원가입한 회원들의 숫자를 보여주려고 한다.

      

3. 로그아웃을 위한 view를 구현하시오. 아래의 조건을 만족하는 view를 작성하시오.

   1. 로그인된 사용자는 들어오지 못하게 한다.

      

4. posts 앱의 post등록을 위한 폼을 만들려고 한다. 이때 필요한 form을 만드시오.



### Import Test

<hr>

1. HTTP method로 POST만을 허용하게하는 Django 내장 데코레이터를 import 하기 위한 코드를 작성하시오

   ```python
   
   ```

2. 로그인된 경우에만 들어올 수 있게하는 Django 내장 데코레이터를 import 하기 위한 코드를 작성하시오

   ```python
   
   ```

3. login을 위한 view를 생성하기 위해 필요한 메소드나 클래스를 import하기 위한 코드를 작성하시오

   ```python
   
   ```

4. logout을 위한 view를 생성하기 위해 필요한 메소드나 클래스를 import하기 위한 코드를 작성하시오

   ```python
   
   ```

5. signup을 위한 view를 생성하기 위해 필요한 메소드나 클래스를 import하기 위한 코드를 작성하시오

   ```python
   
   ```

6. form을 작성하기 위해 필요한 Django의 내장 메소드나 클래스를 import하는 코드를 작성하시오

   ```python
   
   ```

7. 찾는 데이터가 없을 경우, 404에러를 뿜는 메소드를 import하기 위한 코드를 작성하시오.(두가지)

   ```python
   
   ```

   