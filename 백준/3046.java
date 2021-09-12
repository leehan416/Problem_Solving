import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] input = scan.nextLine().split(" ");
		System.out.println((Integer.valueOf(input[1]) * 2) - Integer.valueOf(input[0]));
	}
}