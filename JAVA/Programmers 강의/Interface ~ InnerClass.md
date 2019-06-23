## Interface

### 서로 관계가 없는 물체들이 상호 작용을 하기 위해서 사용하는 장치나 시스템

- 인터페이스 정의
  - 선언 전 어떤 기능들이 있으면 좋을까 ? 를 모아 놓은것
  - 구현하기 전이다!

```java
public interface TV{
	public [final] int MIN_VOLUME=0;
	public  int MAX_VOLUME=100;
	//인터페이스는 final없이도 상수 가능
	public void turnOn();
	public void turnOff();
	public void changeViolum(int volume);
	public void changeChannel(int channel);
    //추상메서드와 상수를 정의할 수 있다.
    //abstract, finaldmf 붙이지 않아도 자동으로 바뀜
}
```

- 인터페이스 구현

```java
public class LedTv implements TV {
//TV 인터페이스를 구현하겠다!
	@Override
	public void turnOn() {
		System.out.println("켜다"); 
	}
	@Override
	public void turnOff() {
		System.out.println("끄다");
	}
	@Override
	public void changeVolume(int volume) {
		System.out.println(volume+"볼륨");
	}
	@Override
	public void changeChannel(int channel) {
		System.out.println(channel+"채널");
	}
}
```

- 인터페이스가 가지고 있는 메소드를 하나라도 구현하지 않는다면 해당 클래스는 추상클래스가 된다.(추상클래스는 인스턴스를 만들 수 없음)

```java
public class LedExam {
	public static void main(String[] args) {
		TV tv=new LedTv();
		tv.turnOn();
		tv.turnOff();
		tv.changeChannel(8);
		tv.changeVolume(34);
	}
}
```

- 참조변수의 타입으로 인터페이스를 사용할 수 있다. 이 경우 인터페이스가 가지고 있는 메소드만 사용할 수 있다.

### Interface의 Default  Method & Static Method

- 기존 - 추상 메서드만
- 디폴트 스태틱 정의 가능
- 메서드 구현 가능
- 구현한 클래스에서는 디폴테 메서드를 오버라이딩 가능
- 인터페이스가 변경이 되면 인터페이스 구현 시 모든 클래스들이 해당 메서드를 모두 바꿔야 하는 문제가 생김
  -> 인터페이스에 메서들르 구현하기 위해 추가한 기능

```java
public interface Calculatro {
	public int plus(int i, int j);
	public int multiple(int i, int j);
	default int exec(int i, int j) {
		return i + j;
	}
	public static int exec2(int i, int j) {
	return i*j;}
	//static 메서드는 인터페이스명.메서드 형식으로만 호출해야함
}
```

```
public class MyCalculator implements Calculatro {
	@Override
	public int plus(int i, int j) {
		return i +j ;
	}
	@Override
	public int multiple(int i, int j) {
		return i*j;
	}
}
```

```java
public class MyCalTest {
	public static void main(String[] args) {
		Calculatro cal = new MyCalculator();
		cal.plus(3, 4);

		int i = cal.exec(3, 9);
		System.out.println(i); //디폴트 메서드

		System.out.println(Calculatro.exec2(7, 7));	 //static 메서드 구현
        // 주의 : 인터페이스명.메서드 형식으로 호출!

//인터페이스를 이용해 간단한 기능을 가지는 유틸리티성 인터페이스를 만들 수 있게 됨
	}
}
```



### 내부클래스

클래스 안에 선언된 클래스

형태에 따라 4가지로 불뉴

- 중첩클래스 or 인스턴스 클래스 
  - 클래스안에 인스턴스 변수 필드에 선언하는 위치에 선언

```java
public class InnerExam {
	class Cal{
		int value=0;
		public void plus() {
			value++;		
		}	
	}
	public static void main(String[] args) {
		InnerExam t= new InnerExam();//밖에 있는 InnerExam1의 객체를 만든 후
		InnerExam.Cal cal=t.new Cal(); //cal이라는 객체 생성됨
		cal.plus();
		System.out.println(cal.value);
	}
}
```



- 정적 중첩클래스 or 스태틱 클래스

```java
public class InnerExam2 {
static 	class Cal{
	int value=0;
	public void plus() {
		value++;		
	}	
}
	public static void main(String[] args) {
		InnerExam2.Cal cal= new nnerExam2.Cal();
//static이기 때문에 바로 cal생성
		cal.plus();
		System.out.println(cal.value);
	}
}
```

- 지역 중첩 또는 지역 클래스

```java
public class InnerExam3 {
public void exec() {
	class Cal{
		int value=0;
		public void plus() {
			value++;		
		}	
	}
	Cal cal=new Cal();
	cal.plus();
	System.out.println(cal.value);
	//메서드 안에서 해당 클래스 이용 가능
}
	public static void main(String[] args) {
		InnerExam3 inn = new InnerExam3();
		inn.exec();
	}
}
```

- 익명클래스

