import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

import javax.print.attribute.standard.NumberUp;
import javax.print.attribute.standard.NumberUpSupported;

public class CalorieCounting {
    public static void main(String[] args) throws Exception {
        System.out.println("Most: " + partOne());
        System.out.println("Top three: " + partTwo());
    }

    public static int partOne() throws Exception {
        Scanner scanner = new Scanner(new File("input.txt"));
        int max = 0;
        int tempSum = 0;

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.isEmpty()) {
                if (tempSum > max) {
                    max = tempSum;
                }
                tempSum = 0;
            } else {
                tempSum += Integer.parseInt(line);
            }
        }

        scanner.close();

        return max;

    }

    public static Integer partTwo() throws Exception {
        Scanner scanner = new Scanner(new File("input.txt"));
        ArrayList<Integer> numbers = new ArrayList<>();
        int tempSum = 0;

        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.isEmpty()) {
                numbers.add(tempSum);
                tempSum = 0;
            } else {
                tempSum += Integer.parseInt(line);
            }
        }
        // numbers.sort(Comparator.reverseOrder());
        Collections.sort(numbers);
        return numbers.get(numbers.size() - 1) + numbers.get(numbers.size() - 2) + numbers.get(numbers.size() - 3);

    }
}