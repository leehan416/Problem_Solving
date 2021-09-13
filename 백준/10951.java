import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			try {
				String text = sc.nextLine();
				System.out.println(Integer.valueOf(text.split(" ")[0]) + Integer.valueOf(text.split(" ")[1]));
			} catch (Exception e) {
				break;
			}
		}

	}
}