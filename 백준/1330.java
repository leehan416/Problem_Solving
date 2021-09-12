import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String input  = scan.nextLine();
		int a = Integer.valueOf(input.split(" ")[0].trim());
		int b = Integer.valueOf(input.split(" ")[1].trim());
		if (a > b) System.out.println(">");
	    else if (a == b) System.out.println("==");
		else System.out.println("<");
	}
}