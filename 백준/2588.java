import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		String[] cut = String.valueOf(b).split("");

		for (int k = 1;; k++)
			try {
				System.out.println(a * Integer.valueOf(cut[cut.length - k]));
			} catch (Exception e) {
				System.out.println(a * b);
				break;
			}
	}
}