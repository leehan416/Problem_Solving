import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a,b,c;
		a = scan.nextInt();
		for (b = 1; b != 10; b++) {
			System.out.println(a+" * "+ b + " = " + a*b);
		}
	}
}