import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = Integer.valueOf(sc.nextLine());
		String inputList = sc.nextLine();
		float[] array = new float[num];
		float sum = 0;
		for (int i = 0; i < num; i++)
			array[i] += Integer.valueOf(inputList.split(" ")[i]);
		// ----------
		float max = 0f;
		for (int i = 0; i < num; i++)
			if (max < array[i])
				max = array[i];
		// ----------
		for (int i = 0; i < num; i++)
			array[i] = (float) (array[i] / max * 100.0);
		// ----------
		for (int i = 0; i < num; i++)
			sum += array[i];
		System.out.println(sum / num);
	}
}