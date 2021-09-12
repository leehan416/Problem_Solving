import java.util.Scanner;

public class Main {
	
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);

		int textlength = Integer.valueOf(sc.nextLine());

		String text = sc.nextLine();
		String[] textArray = text.split("");

		if (textlength <= 25) {
			System.out.println(text);
			return;
		}
		String cutText = "";
		

		for (int i = 11; i < text.length() - 11; i++) {
			cutText += textArray[i];
		}
		String[] cutTextArray = cutText.split("");
		if (cutText.contains(".")) {
			for (int i = 0; i < cutTextArray.length; i++) {
				if (cutTextArray[i].equals(".")) {
					if (i == cutTextArray.length - 1) {
						for (int k = 0; k < 11; k++)
							System.out.print(textArray[k]);
						System.out.print("...");
						for (int k = textArray.length - 11; k < textArray.length; k++)
							System.out.print(textArray[k]);
						break;
						// ...으로 생략가능
					} else {
						for (int k = 0; k < 9; k++)
							System.out.print(textArray[k]);
						System.out.print("......");
						for (int k = textArray.length - 10; k < textArray.length; k++)
							System.out.print(textArray[k]);
						break;
						// ......으로 생략가능
					}
				}
			}
		} else {
			for (int k = 0; k < 11; k++)
				System.out.print(textArray[k]);
			System.out.print("...");
			for (int k = textArray.length - 11; k < textArray.length; k++)
				System.out.print(textArray[k]);
			// ...으로 생략가능
		}

	}
}