import java.util.Scanner;

public class WireframeCostCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input: Read integers N, M, X from a single line
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int X = scanner.nextInt();

        // Calculate the perimeter of the rectangle
        int perimeter = 2 * (N + M);

        // Calculate the total cost of the wireframe
        int cost = perimeter * X;

        // Output the cost
        System.out.println(cost);

        // Close the scanner
        scanner.close();
    }
}