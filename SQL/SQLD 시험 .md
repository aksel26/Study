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

    