package org.example;
public class Main
{
    public static void main(String[] args) {
        int[][] ocean = new int[10][13];
        final String ANSI_YELLOW = "\u001B[33m";
        final String ANSI_RESET = "\u001B[0m";
        final String ANSI_CYAN = "\u001B[36m";

        Solution dfs = new Solution();

        for (int i = 0; i < ocean.length; i++) {
            for (int j = 0; j < ocean[i].length; j++) {
                ocean[i][j] = (int) (Math.random() * 2) ;
                if (ocean[i][j] == 1){
                    System.out.print(ANSI_YELLOW + ocean[i][j] + "\t" + ANSI_RESET);
                }
                else{
                    System.out.print(ANSI_CYAN +ocean[i][j] + "\t" + ANSI_RESET);
                }
            }
            System.out.println();
        }

        System.out.println("Number of islands: " + Solution.countIslands(ocean));

    }
}