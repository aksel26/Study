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

### Exception발생시키기

```java
public class ExceptionTest3 {

	public static void main(String[] args) {
		int i = 10;
		int j = 0;
		
        try {
		int k = divide(i, j);
		System.out.println(k);
		}catch(IllegalArgumentException e){
			System.out.println(e.toString());
		}
	}
	public static int divide(int i, int j) throws IllegalArgumentException{ 
	if(j==0){
//System.out.println("2번째 변수는 0이면 된됩니다.") 
//return 0; 
//리턴 변수가 k로 가서 0이 출력되는데
//0으로 나눈값이 0이 아니므로 
//잘못된 값이 출력된 경우다.
//이 때 강제로 오류를 발생시키는 것이 throw
		throw new IllegalArgumentException("0으로 나눌수 없습니다");//throw : 해당 라인에서 오류가 발생한다는 의미
	}
    
	{
		int k = i / j;
		return k;
	}
}
}
```

### 사용자 정의 Exception

```
public class 클래스이름 extends Exception{

	...
}
```

Exception 이나 exception의 후손을 상속받아 만들어진 클래스

- 사용자 정의 Exception이유
  - 클래스 이름만으로 어떤 오류가 발생했는지 알려줘 직관성을 높여줌

- runtime exception : 컴파일 상황에서 오류나지는 않음
- checked exception : 반드시 오류를 처리해야 하는 exception

BizException 클래스 정의

```java
public class BizException extends RuntimeException {
	public BizException(String msg) {
	super(msg);
}
	public BizException(Exception ex) {
		super(ex);
	}
	}
```

BizService 클래스

```java
public class BizService {
	public void bizMethod(int i) throws BizException {
		System.out.println("비즈니스 메서드 시작");
		if (i < 0)
			throw new BizException("매개변수 i는 0이상이어야 합니다");
		System.out.println("비즈니스 메서드 종료");
	}
}
```

BizExam 사용자정의 Exception 실행

```java
public class BizExam {

	public static void main(String[] args) {
		BizService biz= new BizService();
		biz.bizMethod(5);
		try{
			biz.bizMethod(-3);
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
}
```

출력

| 비즈니스 메서드 시작<br/>비즈니스 메서드 종료<br/>비즈니스 메서드 시작<br/>Programmers.BizException: 매개변수 i는 0이상이어야 합니다<br/>	at Programmers.BizService.bizMethod(BizService.java:7)<br/>	at Programmers.BizExam.main(BizExam.java:9) |
| ------------------------------------------------------------ |
|                                                              |

