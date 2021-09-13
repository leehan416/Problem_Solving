import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String num = sc.nextLine();
		int[] array = new int[Integer.valueOf(num.split(" ")[0])];

		String list = sc.nextLine();
		String[] listCut = list.split(" ");
		for (int i = 0; i < array.length; i++) {
			if (Integer.valueOf(listCut[i]) < Integer.valueOf(num.split(" ")[1]))
				System.out.print(listCut[i] + " ");

		}

	}
}
