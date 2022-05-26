import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(); // intput
		int a = 1; // The Number of Star
		String out = "*";
		while (a <= N) {
			System.out.println(out);
			a++;
			out += "*";
		}
	}
}