import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int problemNum;
		int studentsNum;
		int[] scoreArray;

		int[] studentsArray;
		int[] studentsScore;

		String userInput = sc.nextLine(); // 첫 입력

		problemNum = Integer.valueOf(userInput.split(" ")[0]);
		studentsNum = Integer.valueOf(userInput.split(" ")[1]);

		scoreArray = new int[problemNum];

		studentsArray = new int[studentsNum];
		studentsScore = new int[studentsNum];

		userInput = sc.nextLine(); // 두번째 입력

		for (int i = 0; i < scoreArray.length; i++)
			scoreArray[i] = Integer.valueOf(userInput.split(" ")[i]);

		for (int i = 0; i < studentsNum; i++) {
			userInput = sc.nextLine();

			studentsArray[i] = Integer.valueOf(userInput.split(" ")[0]);

			studentsScore[i] = 0;

			for (int j = 1; j < problemNum + 1; j++) {

				studentsScore[i] += (userInput.split(" ")[j].equals("O")) ? scoreArray[j-1] : 0;

			}

		}
		int value = 0;
		int max = 0;

		for (int i = 0; i < studentsNum; i++) {
			if (max <= studentsScore[i]) {
				if (max == studentsScore[i]) {
					if (studentsArray[i] < studentsArray[value]) {
						value = i;
					}
				} else {
					max = studentsScore[i];
					value = i;
				}
			}
		}

		System.out.println(studentsArray[value] + " " + max);

	}

}