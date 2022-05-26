import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String text = sc.nextLine();
		char[] textArray = text.trim().toLowerCase().toCharArray();
		int[] usedChar = new int[250];
		for (int i = 0; i < textArray.length; i++) {
			usedChar[textArray[i]]++;
		}
		int max = 0;
		int index = 0;
		boolean value = false;
		for (int i = 'a'; i <= 'z'; i++) {
			if (max < usedChar[i]) {
				max = usedChar[i];
				value = false;
				index = i;
			} else if (max == usedChar[i] && max != 0) {
				value = true;
			}
		}
		if (value) {
			System.out.println("?");
		} else {	
			System.out.println(Character.toString(index).toUpperCase());
		}

	}

}