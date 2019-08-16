## 계층형 쿼리 (start with .. connect by)

### 계층 LEVEL 구하기

SELECT MAX(LEVEL)
FROM EMP
START WITH mgr IS NULL
CONNECT BY PRIOR empno=mgr;

- max(level) : 트리구조의 최대 깊이
- START WITH : 시작 조건
- CONNECT BY PRIOR : 조인 조건

### 계층 구조 조회하기

SELECT LEVEL, empno, deptno, mgr, job, sal FROM emp
START WITH mgr IS NULL
CONNECT BY PRIOR empno=mgr;

#### LPAD 이용 구조화

SELECT LEVEL, **LPAD(' ', 4*(LEVEL-1))** || empno,mgr, **CONNECT_BY_ISLEAF**
FROM emp
START WITH mgr IS NULL
CONNECT BY PRIOR empno=mgr;

- CONNECT_BY_ISLEAF : 가장 최하위를 1로 표시

## 서브쿼리

### 메인 쿼리 & 서브 쿼리

SELECT * FROM  emp 
WHERE  deptno = <u>( SELECT  deptno</u>
<u>FROM  dept</u>
<u>WHERE  deptno = 10 );</u>

### 인라인 뷰

SELECT * FROM ( <u>SELECT ROWNUM NUM,ENAME FROM EMP</u> ) a
WHERE NUM < 5; 

### 단일행 & 다중행 서브쿼리

- 반환하는 행 수 1개 : 단일행 (비교 연산자 사용)

- 반환하는 행수 여러개 : 다중행 ( IN, ALL, ANY, EXISTS )

  - IN : OR개념, 하나라도 만족하면 참

    select ename, dname, sal
    from emp, dept
    where emp.deptno= dept.deptno
    and emp.empno
    in (select empno from emp where sal>2000);

    

  - ALL : 모두 동일해야 참

    select * from emp 
    where deptno<= all(20,30);

    

  - ANY : 서브쿼리 결과중 하나라도 <u>동일</u>하면 참

    

  - EXISTS : 하나라도 존재하면 참

    select ename, dname, sal
    from emp,dept
    where emp.deptno = dept.deptno
    and exists ( select 1 from emp where sal>2000);

### 스칼라 서브쿼리

반드시 한 행과 한 칼럼만 반환



### 연관 Correlated 서브쿼리

서브쿼리 내에서 메인 쿼리 내의 칼럼을 사용하는 것



## 그룹 함수

### ROLLUP

GROUP BY의 칼럼 내에서 Subtotal을 만들어 준다

### Grouping 함수

- ROLLUP, CUBE, GROUPING SETS에서 생성되는 합계 값을 구분

## 윈도우 함수

행과 행간의 관계를 정의하기 위해 제공됨

순위, 합계, 평균, 행 위치 등을 조작 가능

### 윈도우 함수 구조

- ARGUMENTS(인수) : 0~N개의 인수 설정

- PARTITION BY ; 전체 집합을 기준에 의해 소그룹으로 나눈다

- ORDERED BY

- WINDOWING : 행 기준의 범위를 정한다.

  - ROWS : 물리적 결과의 행 수,
- RANGE : 논리적 값에 의한 범위
  - BETWEEN ~ AND
- UNBOUNDED PRECEDING
  - UNBOUNDED FOLLOWING
- CURRENT ROW

## 순위 함수

- RANK : 동일한 순위는 동일한 값 부여
- DENSE_RANK : 동일한 순위는 하나의 건수로 계산
- ROW_NUMBER : 동일한 순위에 대해 고유의 순위를 부여함

## 집계함수

- SUM
- AVG
- COUNT
- MAX & MIN

## 행 순서관련 함수

- FIRST_VALUE : 파티션에서 가장 처음에 나오는 값을 구한다
  							MIN함수 사용할 수 도 있음
- LAST_VALUE : 파티션에서 가장 나중에 나오는 값
  						  MAX함수 사용할 수 도 있음
- LAG : 이전 행을 가지고 온다
- LEAD : 특정 위치의 행을 가지고 옴, 기본값은 1

## 비율 관련 함수

- CUME_DIST : 전체 건수에서 현재 행보다 작거나 같은 건수에 대한 누적 백분율 조회 (누적 분포상에 위치를 0~1사이의 값)
-  PERCENT_RANK ; 제일 먼저 나온것을 0으로 (늦게 나온것은 1) 하여 값이 아닌 행의 순서별 백분율 조회
- NTILE : 전체 건수를 ARGUMENT 값으로 N등분 한 결과를 조회
- RATIO_TO_REPORT : 파티션 내에 전체 SUM에 대한 행 별 칼럼 값의 백분율을 소수점까지 조회

## 테이블 파티션

### 파티션 기능

- 대용량 테이블을 여러개 데이터 파일에 분리해서 저장
  - 입력, 수정, 삭제, 조회 성능 향상
- 각각 파티션 별로 독립적으로 관리 가능. <u>파티션별로 백업하고 복구가 가능</u>하면 <u>파티션 전용 인덱스 생성</u>도 가능
- 테이블 스페이스간에 이동 가능
- 데이터 조회 시, 데이터의 범위를 줄여 성능 향상

### Range Partition

- 값의 범위를 기준으로 여러개의 파티션으로 나누어 저장함

### List Partition

- 특정 값을 기준으로 분할

### Hash Partition

- 해시함수를 사용해 DBMS가 알아서 분할하고 관리함

### 파티션 인덱스

- 4가지 유형,
  - 파티션 키 이용해 인덱스 생성 : Prefixed Index
  - 해당 파티션만 사용 : Local Index

