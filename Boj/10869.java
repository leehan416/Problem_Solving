import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String N = sc.nextLine(); // intput

		String[] Cut = N.split(" ");

		int A = Integer.valueOf(Cut[0]);
		int B = Integer.valueOf(Cut[1]);

		System.out.println(A + B);
		System.out.println(A - B);
		System.out.println(A * B);
		System.out.println(A / B);
		System.out.println(A % B);
		


	}
}