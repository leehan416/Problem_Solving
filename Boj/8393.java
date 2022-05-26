import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt(); // intput
		int a = 1;
		int c = 0;
		while (true) {
			if (N < a) {
				break;
			}
			c += a;
			a++;
		}
		System.out.println(c);
	}
}