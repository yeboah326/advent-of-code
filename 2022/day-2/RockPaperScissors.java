import java.io.File;
import java.util.HashMap;
import java.util.Scanner;

public class RockPaperScissors {
    public static void main(String[] args) throws Exception {
        // partOne("/home/ultron/Documents/Projects/advent-of-code/2022/day-2/sample.txt");
        partTwo("/home/ultron/Documents/Projects/advent-of-code/2022/day-2/input.txt");
    }

    public static void partOne(String filename) throws Exception {
        Scanner scanner = new Scanner(new File(filename));
        String elf;
        String human;

        Integer score = 0;

        while (scanner.hasNextLine()) {

            String[] line = scanner.nextLine().split(" ");
            elf = line[0];
            human = line[1];

            // Values
            HashMap<String, Integer> values = new HashMap<>();
            values.put("A", 1);
            values.put("B", 2);
            values.put("C", 3);
            values.put("X", 1);
            values.put("Y", 2);
            values.put("Z", 3);

            if (values.get(human).equals(values.get(elf))) {
                score += 3 + values.get(human);
            } else {
                switch (elf) {
                    case "A":
                        if (human.equals("Z"))
                            score += values.get(human);
                        if (human.equals("Y"))
                            score += 6 + values.get(human);
                        break;
                    case "B":
                        if (human.equals("X"))
                            score += values.get(human);
                        if (human.equals("Z"))
                            score += 6 + values.get(human);
                        break;
                    case "C":
                        if (human.equals("Y"))
                            score += values.get(human);
                        if (human.equals("X"))
                            score += 6 + values.get(human);
                        break;

                }
            }
        }

        System.out.println(score);
    }

    public static void partTwo(String filename) throws Exception {
        Scanner scanner = new Scanner(new File(filename));
        String elf;
        String instruction;

        Integer score = 0;

        // Loose map
        HashMap<String, Integer> looseMap = new HashMap<>();
        looseMap.put("A", 3);
        looseMap.put("B", 1);
        looseMap.put("C", 2);

        // Win map
        HashMap<String, Integer> winMap = new HashMap<>();
        winMap.put("A", 2);
        winMap.put("B", 3);
        winMap.put("C", 1);

        // Draw map
        HashMap<String, Integer> drawMap = new HashMap<>();
        drawMap.put("A", 1);
        drawMap.put("B", 2);
        drawMap.put("C", 3);

        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split(" ");
            elf = line[0];
            instruction = line[1];

            switch (instruction) {
                case "X":
                    score += looseMap.get(elf);
                    break;
                case "Y":
                    score += 3 + drawMap.get(elf);
                    break;
                case "Z":
                    score += 6 + winMap.get(elf);
            }

        }
        System.out.println(score);

    }
}