import java.util.Scanner;

public class Main {
	static int[][] map;
	static int[] homeSize = new int[700];
	static int i = 0;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int size = Integer.valueOf(sc.nextLine());
		map = new int[size][size];
		
		for (int k = 0; k < size; k++) {
			String input = sc.nextLine();
			String[] inputArray = input.split("");
			for (int i = 0; i < size; i++) {
				map[k][i] = Integer.valueOf(inputArray[i]);
			}
		}

		for (int y = 0; y < size; y++) {
			for (int x = 0; x < size; x++) {
				if (map[y][x] == 1) {
					find(x, y);
					i++;
				}
			}
		}

		int length = 0;
		for (length = 0; homeSize[length] != 0;)
			length++;

		int[] array = new int[length];

		for (int l = 0; l < length; l++) {

			array[l] = homeSize[l];
		}

		for (int i = 0; i < length; i++) {
			for (int j = 0; j < length - 1 - i; j++) {
				if (array[j] > array[j + 1]) {
					int temp = array[j];
					array[j] = array[j + 1];
					array[j + 1] = temp;
				}
			}
		}

		System.out.println(length);
		for (int i = 0; i < length; i++) {
			System.out.println(array[i]);
		}
	}

	static void find(int x, int y) {

		if (map[y][x] == 0 || map[y][x] == 2) {
			return;
		}
		map[y][x]++;
		homeSize[i]++;

		try {
			find(x - 1, y);
		} catch (Exception e) {}
		try {
			find(x + 1, y);
		} catch (Exception e) {}

		try {
			find(x, y - 1);
		} catch (Exception e) {}

		try {
			find(x, y + 1);
		} catch (Exception e) {}

	}

}