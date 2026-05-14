import java.util.*;

public class OptimizationExamples {

    // =========================
    // 1. O(n²) Duplicate Search
    // =========================
    public static boolean containsDuplicate(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }

    // =====================================
    // 2. Inefficient String Concatenation
    // =====================================
    public static String concatenateWords(List<String> words) {
        String result = "";

        for (String word : words) {
            result += word;
        }

        return result;
    }

    // ==========================
    // 3. O(n²) Two Sum Problem
    // ==========================
    public static int[] twoSum(int[] nums, int target) {

        for (int i = 0; i < nums.length; i++) {

            for (int j = i + 1; j < nums.length; j++) {

                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[]{-1, -1};
    }

    // ==================================
    // 4. Repeated List.contains() Calls
    // ==================================
    public static List<Integer> intersection(
            List<Integer> list1,
            List<Integer> list2
    ) {

        List<Integer> result = new ArrayList<>();

        for (Integer num : list1) {

            if (list2.contains(num)) {
                result.add(num);
            }
        }

        return result;
    }

    // ===================================
    // 5. Recomputing Fibonacci Recursively
    // ===================================
    public static int fibonacci(int n) {

        if (n <= 1) {
            return n;
        }

        return fibonacci(n - 1)
                + fibonacci(n - 2);
    }

    // ================================
    // 6. Bubble Sort Implementation
    // ================================
    public static void bubbleSort(int[] arr) {

        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {

            for (int j = 0; j < n - i - 1; j++) {

                if (arr[j] > arr[j + 1]) {

                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    // ====================================
    // 7. Counting Frequency Inefficiently
    // ====================================
    public static Map<Integer, Integer> frequencyCount(
            int[] nums
    ) {

        Map<Integer, Integer> freq = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int count = 0;

            for (int j = 0; j < nums.length; j++) {

                if (nums[i] == nums[j]) {
                    count++;
                }
            }

            freq.put(nums[i], count);
        }

        return freq;
    }

    // ====================================
    // 8. Repeated Database Simulation
    // ====================================
    public static void fetchUsers(List<Integer> userIds) {

        for (Integer id : userIds) {

            simulateDatabaseCall(id);
        }
    }

    public static void simulateDatabaseCall(int id) {

        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Fetched user " + id);
    }

    // ================================
    // 9. Finding Max Value Inefficiently
    // ================================
    public static int findMax(int[] nums) {

        Arrays.sort(nums);

        return nums[nums.length - 1];
    }

    // ====================================
    // 10. Nested Loop Matrix Comparison
    // ====================================
    public static boolean matricesEqual(
            int[][] matrix1,
            int[][] matrix2
    ) {

        for (int i = 0; i < matrix1.length; i++) {

            for (int j = 0; j < matrix1[i].length; j++) {

                if (matrix1[i][j] != matrix2[i][j]) {
                    return false;
                }
            }
        }

        return true;
    }

    // =========================
    // Main Method for Testing
    // =========================
    public static void main(String[] args) {

        int[] nums = {1, 2, 3, 4, 1};

        System.out.println(
                containsDuplicate(nums)
        );

        List<String> words = Arrays.asList(
                "AI",
                "Code",
                "Optimizer"
        );

        System.out.println(
                concatenateWords(words)
        );

        int[] result = twoSum(
                new int[]{2, 7, 11, 15},
                9
        );

        System.out.println(
                Arrays.toString(result)
        );

        System.out.println(
                fibonacci(10)
        );
    }
}
