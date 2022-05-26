import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt(); // intput
		int a=1;
		while (true) {
			if (N == 0)
				break;
			a*=N;
			N--;
		}
		System.out.println(a);
	}
}