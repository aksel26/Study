## SQL 최적화 원리

### 옵티마이저와 실행 계획

- 옵티마이저
  - SQL 실행시 어떻게 실행할 것인지에 대한 계획 - 실행계획( Execution Plan)
  - DBMS의 소프트웨어
  - 성능의 차이가 발생하기 때문에 중요함

- 특징
  - 데이터 딕셔너리- 오브젝트 통계, 시스템 통계 등의 정보로 비용 정보 계산 - 최저 비용으로 선택

- 옵티마이저의 실행계획 확인

  desc plan_table

  

### 옵티마이저 종류

- 실행 방법

  SQL 실행 - Parsing (문법 검사 & 구문 분석) - Fetch (데이터 인출)

  ​					Parsing : <u>비용기반</u> or 규칙기반 실행계획 수립

  - 옵티마이저 엔진

    Query Transformer : SQL문을 효율적으로 실행하기 위해 변환
    변환되어도 결과는 동일	

    Estimator : 통계정보로 SQL 실행 비용 계산

    Plan Generator :  실행 계획 수립
    15개의 우선순위를 기준으로 실행 계힉 수립

### 인덱스

- 데이터를 빠르게 검색 할 수 있는 방법

- 인덱스 키로 정렬(SORT)되어 있기 때문에 빠르게 정렬 가능

  - 오름차순 및 내림차순 탐색 가능

- 1 테이블, 여러개 인덱스 생성 가능
  1인덱스, 여러개의 칼럼 구성 가능

- 테이블 생성시 기본키는 자동으로 인덱스 생성되고,
   이름은 SYSXXXX

- 인덱스 구조 : Root Block, Branch Block, Leaf Block

  - Root Block : 가장 사우이
  - Branch Block : 다음 단계 주소를 가지고 있는 포인터
  - Leaf Block : (SORTED) 인덱스 키 & ROWID로 구성 
    Double linked list형태 : 양방향 탐색 가능

- 인덱스 생성

  : CREATE INDEX

  한개 이상의 칼럼 사용해 생성
  기본적으로 오름차순 DESC옵션도 있음

#### 인덱스 스캔

 1. 인덱스 유일 스캔 (Index Unique Scan)

    키 값이 중복하지 않는 경우 발생

    select * from emp where empno=7369;
    ![15](https://user-images.githubusercontent.com/50945713/63224116-88a4d780-c1fa-11e9-9650-f47c069c7dc7.png)

	2. 인덱스 범위 스캔 (Index Range Scan)

    특정 범위 조회 <u>WHERE 문</u> 사용할 경우 발생 (Like, Between)

    데이터 양이 적은 경우는 full scan이 될 수 있음

    인덱스의 Leaf Block의 특정 범위를 스캔한 것

    ![rangescan](https://user-images.githubusercontent.com/50945713/63224143-f224e600-c1fa-11e9-8dd9-deb9134a4c54.png)

	3. 인덱스 전체 스캔 (Index Full Scan)

    인덱스 키가 많은 경우 Leaf Block의 처음부터 끝까지 읽음

    ![fullscan](https://user-images.githubusercontent.com/50945713/63224168-5778d700-c1fb-11e9-87eb-8742bc2d0b7b.png)

### 실행 계획

1. dept 테이블 sys_CXXXX를 index unique scan

2. dept 테이블에서 rowid 사용 조회

3. emp 테이블 full scan

4. nested loop 방식 조인으로 최종 결과

   nested loop : 데이터를 먼저 dept테이블(Outer Table) 에서 찾고 그다음 emp테이블(Inner Table)을 찾는 것 **(Random Access)**

### 옵티마이저 조인

- Nested Loop 조인

  - 외부테이블의 크기가 작은 것을 먼저 찾는 것이 중요

    select <u>/* + ordered use_nl (b) +*/</u> * from emp a, dept b where a.deptno=b.deptno
    and a.deptno=10;

    use_nl : nested loop 수행 힌트

- Sort Merge 조인

  - 2개의 테이블 Sort_Area 메모리 공간에 모두 로딩 후 Sort,
    sort 완료 후 Merge
  - Sort가 발생하므로 데이터 양이 많아지면 성능 저하 ;
    디스크에 있는 임시 영역에서 수행되기 때문

### Hash 조인

- 2개의 테이블 중 작은 테이블을HASH메모리에 로딩,
  조인 키로 해시 테이블 생성

- 해시 함수로 주소를 계산, 주소로 테이블을 조인하므로 CPU연산이 많음

  



