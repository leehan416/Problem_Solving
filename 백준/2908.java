import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String num = sc.nextLine();
		String[] numList = num.split("");

		String temp = numList[0];
		numList[0] = numList[2];
		numList[2] = temp;

		temp = numList[4];
		numList[4] = numList[6];
		numList[6] = temp;
		int num1 = Integer.valueOf(numList[0] + numList[1] + numList[2]);
		int num2 = Integer.valueOf(numList[4] + numList[5] + numList[6]);
		if (num1 > num2)
			System.out.println(num1);
		else
			System.out.println(num2);

	}

}
