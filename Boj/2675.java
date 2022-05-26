import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = Integer.valueOf(sc.nextLine());
		String[] userInput = new String[num];
		int[] value = new int[num];
		String[] text = new String[num];
		for (int i = 0; i < num; i++) {
			userInput[i] = sc.nextLine();
			value[i] = Integer.valueOf(userInput[i].split(" ")[0]);
			text[i] = userInput[i].split(" ")[1];
		}
		for (int i = 0; i < num; i++) {
			String[] textArray = text[i].split("");
			for (int j = 0; j < text[i].length(); j++)
				for (int n = 0; n < value[i]; n++)
					System.out.print(textArray[j]);
			System.out.print("\n");
		}
	}
}