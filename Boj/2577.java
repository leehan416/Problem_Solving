import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int k = 1;
		int[] val = new int[10];
		for (int a = 0; a < 3; a++) {
			int h = scan.nextInt();
			k *= h;
		}
		String[] a = String.valueOf(k).split("");
		for (int i = 0; i < a.length; i++)
			val[Integer.valueOf(a[i])]++;
		for (int j = 0; j < 10; j++)
			System.out.println(val[j]);
	}
}