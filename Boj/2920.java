import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String input = sc.nextLine();
		String[] inputList = input.split(" ");
		int[] array = new int[8];
		int value = 0;

		for (int i = 0; i < 8; i++) {
			array[i] = Integer.valueOf(inputList[i]);
			if (i + 1 == array[i])
				value++;

		}

		if (value == 8) {
			System.out.println("ascending");
			return;
		}
		value = 0;

		for (int i = 8, j = 0; i != 0; i--, j++)
			if (array[j] == i)
				value++;

		if (value == 8)
			System.out.println("descending");
		else
			System.out.println("mixed");

	}
}
