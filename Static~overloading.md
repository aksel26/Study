## 변수의 scope와 stataic 

```java
int globalScope=10'
static int (staticValue)=7;

public void scopeTest(int value){
int localScope=20;
System.out.println(localScope);
System.out.println(globalScope);
System.out.println(value);

}

public void scopeTest2(int value2){
System.out.println(localScope);//컴파일에러
System.out.println(globalScope);  //가능
System.out.println(value);// 컴파일 에러

System.out.println(value2);//가능

}

public static void main(String[] args)[
System.out.println(localScope);//컴파일에러
System.out.println(globalScope);  //컴파일 에러
System.out.println(value);// 컴파일 에러
System.out.println(StaticValue);
]
//모든 클래스는 인스턴스화 하지 않은 채로 사용할 수없다.
//static 을 사용하면 인스턴스화하지 않아도 사용 가능

//그렇다면 static하지 않은 변수를 사용하려면 ?
 //객체를 생성하면 됨!
 VariavleScopeExam v1=new VariavleScopeExam();
 VariavleScopeExam v2= new VariavleScopeExam()
   v1.globalScope=1323;
System.out.println(globalScope); //출력값 1323
    // 클래스 변수

v1.StaticValue=123;
v2.StaticValue=1232;
System.out.println(v1.StaticVal); //출력값 123
System.out.println(v1.StaticVal); //출력값 123
//static한 변수, 값을 저장할 수 있는 공간이 하나밖에 없어서 값을 공유한다.
     //클래스 이름을 직접 사용하는 것이 가능
System.out.println(VariableScopeExam.staticVal); 
     //클래스명.클래스 변수명
     
```

## 열거형 (Enum)

열거형 자체가 변수타입으로 사용 가능

특정값만 가져야 한다면 열거형으로 !!

```java
public static final Sting  MALE="MALE"; 
public static final Sting  FEMALE="FEMALE"; 
public class EnumExam {
	public static final String MALE="MALE";
	public static final String FEMALE="FEMALE";
	public static void main(String[] args) {
//젠더 중 2가지 값 외는 안나오도록 하고 싶으면 ?
		String gender1;
		gender1=EnumExam.MALE;
		gender1=EnumExam.FEMALE;
		
		gender1="boy";
		//gender1에 어느것이 대응되는지 애매함
        //gender1값이 string이기 때문에 어떠한 string값이 와도 오류가 안남
		//오류는 나지 않지만 컴파일시 오류발생
		//=> 열거형 사용
		Gender gender2;
		gender2=Gender.MALE;
		gender2=Gender.MALE;
		
		//gender2="boy";
		//enum 생성시 MALE,FEMALE외에 것을 넣으려고 하면
		//실행 전부터 오류발생
		
	}

}
//enum 이름 {값1,값2}
enum Gender{
	MALE,FEMALE;
}
```

## 생성자

< Car > 클래스

```java
public class Car {
	String name;
	int number;
	
	//생성자 정의 
	public Car(String n) {
		name=n;
	}
	}
```

< CarExam2 > 클래스

```java
public class CarExam2 {
	public static void main(String[] args) {

//Car c1=new Car();
		
		//Car() 생성자부분
		//객체가 될때 필드를 초기화하는 목적
		
		//Car클래스에서 생성자를 만들었더니
		//Car c1=new Car(); 오류발생
		//기본생성자 사용 불가

Car c2=new Car("소방차") ;
Car c3=new Car("구급차") ;
System.out.println(c2.name);
//소방차 출력
	}

}

```

## this

### 객체 자신을 참조하는 변수

```java
String name;
int number;


public Car(String n){	//String n 은 name의 약자인지 
number의 약자인지 모호함 
name=n;

public Car(String name){	
	name=name;				
	
}
//name으로 바꿨더니 name=name이 되고 메인 메서드에서 실행시키면 null값이 출력됨
public static void main(String[] args) {
Car c2=new Car("소방차") ;
Car c3=new Car("구급차") ;
System.out.println(c2.name); 
} 

//public Car(String name){ 에서의 name을 가리키고 있기 때문

public Car(String name){	
	this.name=name;				
	//나의 필드 name에다가 매개변수 String name을 넣는다
}
```

## 메서드 오버로딩

### 매개변수의 유형과 개수가 다르게 하여 같은 이름의 메소드를 여러 개 가질 수 있게하는 기술

```java
//매개변수 타입(이름은 중요하지 않음)과 수가 중요함

public class MyClass2 {
	public int plus( int x,int y) {
	return x+y;	
	}
	
	public int plus(int x, int y,int z) {
		return x+y+z;
	}
	public String plus(String a, String b) {
		return a+b;
}
}
```

```java
public class MethodOverloadExam {

	public static void main(String[] args) {
	MyClass2 m= new MyClass2();
	System.out.println(m.plus(4, 5));
	System.out.println(m.plus(5, 8, 9));
	System.out.println(m.plus("a", "jj"));
	}
}
```



## 생성자 오버로딩과this

매개변수와 수와 타입이 다르다면 생성자도 여러개 선언 가능하다

```java
public class Car {
	String name;
	int number;

	public Car() {
//		this.name="이름없음";
//		this.number=0;
//밑에 있는 생성자와 코드중복-->this()사용
		
		this(1341,"이름없음");
//		this() 는 중복코드 방지
//		매개변수 안에 알맞은 형식을 가지고 있는 메서드를 찾아 적용시킴.
	}
	public Car(int number,String name) {
		this.name=name;
		this.number=number;
	}
	}

---Main 메서드-----

Car c3=new Car() ; //이름없음, 0
Car c4=new Car(1231, "구급차");
```

