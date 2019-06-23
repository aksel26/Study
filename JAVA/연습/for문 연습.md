Q) 알파벳 역순

```java
for (char i = 'Z'; i >= 'A'; i--) {
			System.out.print(i);
		}
```

Q) 알파벳 5개씩 출력

```java
int count = 0;
	
	for (char ch='A'; ch<='Z'; ch++) {
	count++;
	if( count % 5 ==0) {
		System.out.println(ch);
	}else {
		System.out.print(ch);
    }	
	}
```

```
<Output>
ABCDE
FGHIJ
KLMNO
PQRST
UVWXY
Z
```



Q ) 입력받은 숫자의 합

```java
Scanner input = new Scanner(System.in);
		int tot = 0;
		for(int i = 0 ; i <5 ; i ++) {
		int num = input.nextInt();
			tot+=num;
		}
		System.out.println(tot);
```

Q ) 구구단 출력

```java
for (int i = 1; i < 10; i++) {
			for (int j = 2; j < 10; j++) {
				System.out.print(j + "*" + i + "=" + i * j + "\t");
			}
			System.out.println();
```

```
<Output>
2*1=2	3*1=3	4*1=4	5*1=5	6*1=6	7*1=7	8*1=8	9*1=9	
2*2=4	3*2=6	4*2=8	5*2=10	6*2=12	7*2=14	8*2=16	9*2=18	
2*3=6	3*3=9	4*3=12	5*3=15	6*3=18	7*3=21	8*3=24	9*3=27	
2*4=8	3*4=12	4*4=16	5*4=20	6*4=24	7*4=28	8*4=32	9*4=36	
2*5=10	3*5=15	4*5=20	5*5=25	6*5=30	7*5=35	8*5=40	9*5=45	
2*6=12	3*6=18	4*6=24	5*6=30	6*6=36	7*6=42	8*6=48	9*6=54	
2*7=14	3*7=21	4*7=28	5*7=35	6*7=42	7*7=49	8*7=56	9*7=63	
2*8=16	3*8=24	4*8=32	5*8=40	6*8=48	7*8=56	8*8=64	9*8=72	
2*9=18	3*9=27	4*9=36	5*9=45	6*9=54	7*9=63	8*9=72	9*9=81
```

Q ) 별찍기 ( 5X5) 1

```java
		for (int i = 0; i < 5; i++) {
			for (int j = 0; j < 5; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
```

```
<Output>
*****
*****
*****
*****
*****
```

Q) 별찍기 2

```java
		for (int i = 0; i < 6; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}
```

```
<output>
*
**
***
****
*****
```

Q ) 별찍기 3

```java
for ( int a =1 ; a<=4; a++) {
		for (int b = 1 ; b<=4  ; b ++) {
			if(a<=b) {
				System.out.print("★");
			}else {
				System.out.print(" ");
			}
		}System.out.println();
	}
```

```
<output>
★★★★
 ★★★
  ★★
   ★
```

Q ) 별찍기 4 

```java
package lab.java;

import java.util.Scanner;

public class Test2 {

	public static void main(String[] args) {
		for( int i = 0 ; i< 6 ; i++) {
			for (int j = 0 ; i>j ; j++) {
				System.out.print("☆");
				
			}for( int k = 0 ; k<5-i ; k ++) {
				System.out.print("★");
			}
			System.out.println();
			}
```

<출력>
★★★★★
☆★★★★
☆☆★★★
☆☆☆★★
☆☆☆☆★
☆☆☆☆☆

Q) 숫자 출력

```java
for( int i =1 ; i<=5 ; i ++) {
		for(int j = i; j<=4+i ;j ++) {
			System.out.print(j);
		}System.out.println();
	}
```

12345
23456
34567
45678
56789



문 ) 입력받은 숫자의 팩토리얼 구하기

```java
Scanner input = new Scanner(System.in);
				int num = input.nextInt();
				int result = 1;
				for ( int i = num ; i>0 ; i--) {
					 result*=i;
				}System.out.println(result);
```

Q) 20 까지의 짝수의 합

```java
int sum1 = 0;
	for (int i = 1 ; i <=20 ; i ++) {
		if( i % 2== 0 ) {
			sum1 += i ;
		}
	}System.out.println(sum1);
```

Q) 33~45 까지 짝수 구하기

```java
for(int i=33 ; i<=45 ;i++) {
		
		if ( i % 2 ==0 ) {
			System.out.println(i+" 는 짝수" );
		}else {
			System.out.println(i );
		}
	}
```

Q) 소수 구하기

```java
	for ( int i = 1 ; i <= 100 ; i ++) {
		int count= 0;
		for ( int j =1 ; j<=i; j++) {
			if ( i% j ==0 ) {
				count ++;			
			}
		}
		if(count ==2) {
			System.out.println(i + " 는  소수");
		}
	}
}
}
```

Q ) 3개 추의 조합

```java
System.out.println("2g 3g 5g total");
	int hap = 0;
	for (int i = 1; i <=5; i ++) {
		for (int j = 1; j<=5 ;j ++) {
			for (int k = 1; k<=5 ; k++) {
				hap = (i*2)+(j*3)+(k*5);
				
				if( hap>=40 && hap <=45) {
					System.out.println(i+" "+j+" "+k+" "+hap);
				}
			}
		}
```

```
<Output>
2g 3g 5g total
1 5 5 42
2 4 5 41
2 5 5 44
3 3 5 40
3 4 5 43
3 5 4 41
4 3 5 42
4 4 4 40
4 4 5 45
4 5 4 43
5 2 5 41
5 3 5 44
5 4 4 42
5 5 3 40
5 5 4 45
```

