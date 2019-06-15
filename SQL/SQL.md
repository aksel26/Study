- WITH 

  긴 쿼리문에서 반복적으로 사용하는 서브쿼리를 먼저 정의해 재사용 가능하도록 함

  ```sql
  WITH
  별칭 as (서브쿼리),
  별칭 as (서브쿼리),
  select ~ from 
  ```

- 집합 연산자

  서로다른 select의 결과를 단일 결과 집합으로 만드는 연산자

  - 합 : UNION : 중복행 제외 
  - ​       UNION ALL :중복 포함
  - 교 : INTERSECT
  - 차 : MINUS

  ```SQL
  SELECT ~ FROM ~[WHERE~][GROUP BY~][HAVING~]
  UNION/ UNION ALL/ INTERSECT/ MINUS
  SELECT ~ FROM ~[WHERE~][GROUP BY~][HAVING~]
  ```

  - SELECT문에서 1) 컬럼갯수, 2) 컬럼타입이 같아야한다!

  - 정렬된 값은 첫번째 칼럼값을 기준으로 정렬된다.

    - 다른 컬럼으로 정렬하려면 ?

    ​		-> 마지막 SELECT문에서 ORDER BY 사용하면 된다.

- ROLL UP / CUBE

  GROUP BY 의 확장 기능!

  - ROLL UP : 단계별 소계

  - CUBE : 총계

    - ROLL UP

      - 예제1) 부서별 급여 합계와 전체 합계를 조회

        - ```sql
          SELECT deptno,sum(sal) 연봉합 from emp group by rollup(deptno);	
          
          --union all 이용
          select deptno,sum(sal)  연봉합 from emp group by deptno union all 
          select null deptno, sum(sal) 연봉합 from emp ;
          ```

          ![](C:\Users\HK\Pictures\UNION ALL.PNG)

          부서별 사원의 급여와 소계 & 전체합계

          ```sql
          select deptno, empno,sum(sal) 연봉합 from emp group by rollup(deptno,empno);
          ```

          부서별 인원수와 급여 합계

          ```sql
          select b.dname, a.job , sum(a.sal) sal, count (a.empno) emp_count from emp a, dept b 
          where a.deptno=b.deptno group by b.dname,a.job; --rollup  사용 전
          
          select b.dname, a.job, sum(a.sal) sal, count(a.empno) emp_count from emp a,dept b
          where a.deptno=b.deptno group by rollup(b.dname,a.job); 
          --누적 합을 구할 때 유용하다.
          ```

          

    - CUBE : 큐브가 없으면 두개의 ROLLUP 을 이용해야 한다.

      - ```SQL
        SELECT B.DNAME,A.JOB ,SUM(A.SAL) SAL ,COUNT(A.EMPNO) EMP_COUNT FROM
        DEPT B, EMP A WHERE B.DEPTNO=A.DEPTNO
        GROUP BY ROLLUP(B.DNAME,A.JOB)
        UNION
        SELECT ' ', JOB,SUM(SAL) SAL ,COUNT(EMPNO) EMP_COUNT FROM EMP GROUP BY ROLLUP(JOB);-- CUBE 사용하지 않을 때
        
        SELECT DNAME,JOB ,SUM (SAL) SAL, COUNT(EMPNO) EMP_COUNT FROM EMP A, DEPT B
        WHERE A.DEPTNO=B.DEPTNO
        GROUP BY CUBE (B.DNAME, A.JOB);
        ```

      - Cross Tab에 대한 Summary를 추출하는데 사용된다.

    - GROUPING SETS

      - ```SQL
        SELECT NULL DEPTNO,JOB, SUM(SAL) FROM EMP GROUP BY JOB UNION ALL 
        SELECT DEPTNO,NULL JOB, SUM(SAL) FROM EMP GROUP BY DEPTN
        
        SELECT DEPTNO, JOB, SUM(SAL) FROM EMP GROUP BY GROUPING SETS(DEPTNO,JOB); -- GROUPING SETS 사용
        ```

        <출력>![](C:\Users\HK\Pictures\GROUPING SETS 예제.png)

