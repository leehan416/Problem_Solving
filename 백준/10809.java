import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String text = sc.nextLine();
		char[] textList = text.toCharArray();
		int[] num = new int[26];
		for (int i = 0; i < 26; i++)
			num[i] = -1;
		for (int i = 0; i < textList.length; i++)
			if (num[textList[i] - 'a'] == -1)
				num[textList[i]  - 'a'] = i;
		for (int i = 0; i < num.length; i++) {
			System.out.print(num[i]);
			if (i != num.length - 1)
				System.out.print(" ");
		}
	}
}