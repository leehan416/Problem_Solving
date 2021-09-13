import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = Integer.valueOf(sc.nextLine());
		for (int i = 0; i < num; i++) {
			String array = sc.nextLine();
			String[] list = array.split(" ");
			System.out.println(Integer.valueOf(list[0])+Integer.valueOf(list[1]));
		}
	}
}