import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int[] list = new int[9];
		int M = 0;
		for (int a = 0; a < 9; a++) {
			int h = scan.nextInt();
			list[a] = h;
		}
		int val = 0;
		for (int a = 0; a < 9; a++) {
			if (M < list[a]) {
				val = a;
				M = list[a];
			}
		}
		System.out.print(M + "\n" + ++val);
	}
}
