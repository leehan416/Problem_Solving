import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int sum = 0;
		int num = Integer.valueOf(sc.nextLine());
		String array = sc.nextLine();
		String[] list = array.split("");
		for (int i = 0; i < num; i++) {
			int value = Integer.valueOf(list[i]);
			sum += value;
		}
		System.out.println(sum);
	}
}