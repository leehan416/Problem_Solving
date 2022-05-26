import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int min, max;
		int num = Integer.valueOf(sc.nextLine());
		String array = sc.nextLine();
		String[] list = array.split(" ");

		min = 1000001;
		max = -1000001;
		for (int i = 0; i < num; i++) {
			int value = Integer.valueOf(list[i]);

			if (min > value)
				min = value;

			if (max < value)
				max = value;
		}
		System.out.println(min + " " + max);
	}
}