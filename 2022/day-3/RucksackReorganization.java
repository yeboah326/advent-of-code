import java.io.File;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Map.Entry;

public class RucksackReorganization {
    public static void main(String[] args) throws Exception {
        partOne("/home/ultron/Documents/Projects/advent-of-code/2022/day-3/sample.txt");
    }

    public static void partOne(String filename) throws Exception {
        String commonCharacter = "v";
        Scanner scanner = new Scanner(new File(filename));
        char currentCharacter;
        int total = 0;

        while (scanner.hasNextLine()) {
            String currentLine = scanner.nextLine();
            Map<Character, Integer> itemCount = new HashMap<>();
            char doubleItem = 'x';

            for (int i = 0; i < currentLine.length() / 2; i++) {
                itemCount.put(currentLine.charAt(i), 1);
            }

            for (int i = currentLine.length() / 2; i < currentLine.length(); i++) {
                currentCharacter = currentLine.charAt(i);
                if (itemCount.containsKey(currentCharacter)) {
                    itemCount.put(currentCharacter, itemCount.get(currentCharacter) + 1);
                } else {
                    itemCount.put(currentLine.charAt(i), 1);
                }
            }
            System.out.println(itemCount);

            for (Entry<Character, Integer> entry : itemCount.entrySet()) {
                doubleItem = entry.getKey();
                if (entry.getValue() == 2) {
                    if ((int) Character.valueOf(doubleItem) >= 65 & (int) Character.valueOf(doubleItem) <= 65)
                        total += (int) Character.valueOf(entry.getKey()) % 65 + 27;
                    if ((int) Character.valueOf(doubleItem) >= 97 & (int) Character.valueOf(doubleItem) <= 65)
                        total += (int) Character.valueOf(entry.getKey()) % 96;
                }
            }
        }

        System.out.println(total);
    }
}
