import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String text = sc.nextLine();
		String[] textArray = text.split(" ");
		int value = 0;
		for (int i = 0; i < textArray.length; i++)
			if (textArray[i].equals(""))
				value++;
		System.out.println(textArray.length - value);
	}
}