import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = Integer.valueOf(sc.nextLine());
		String[] userInput = new String[num];
		for (int i = 0; i < num; i++) 
			userInput[i] = sc.nextLine();
		for (int i = 0; i < num; i++) {
			int score = 0;
			int value = 1;
			String[] textArray = userInput[i].split("");
			for (int j = 0; j < textArray.length; j++) 
				if (textArray[j].equals("O")) score += value++;
				else value = 1;
			System.out.println(score);
		}
	}
}