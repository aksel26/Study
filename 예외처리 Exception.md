## 예외처리 Exception

```java
public class EexceptionExam {

	public static void main(String[] args) {
		int i = 3;
		int j = 0;

		try {
			int k = i / j;
			System.out.println(k); 
		} catch (ArithmeticException e) {
			System.out.println(e.toString());
//toString() : 예외클래스변수명.toString()
//예외의 정보를 알려주는 메서드
            
		}finally { //생략 가능
			System.out.println("무조건 실행");
		}
		System.out.println("main end");
	}
}

```



### throws

```java
public class ExceptionTest2 {

	public static void main(String[] args) {
		int i =10;
		int j =0;
		try {
			int k= divide(i, j);
			System.out.println(k);	
		}catch(ArithmeticException e) {
			System.out.println(e.toString());
		}
	}
public static int divide(int i, int j) throws ArithmeticException
//arithmetic exception을 넘길것이다
//,로 여러개 넘길 수 있다.
	{
		int k=i/j;
		return k;
	}
}
```

