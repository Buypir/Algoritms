package org.example;

public class Solution {
    static void DFS(int[][] array, int i, int j, int row, int column)
    {
        if (i < 0 || j < 0 || i > (row - 1) || j > (column - 1) || array[i][j] != 1)
        {
            return;
        }

        if (array[i][j] == 1)
        {
            array[i][j] = 0;
            DFS(array, i + 1, j, row, column);
            DFS(array, i - 1, j, row, column);
            DFS(array, i, j + 1, row, column);
            DFS(array, i, j - 1, row, column);
            DFS(array, i + 1, j + 1, row, column);
            DFS(array, i - 1, j - 1, row, column);
            DFS(array, i + 1, j - 1, row, column);
            DFS(array, i - 1, j + 1, row, column);
        }
    }

    static int countIslands(int[][] array)
    {
        int row = array.length;
        int column = array[0].length;
        int count = 0;
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < column; j++)
            {
                if (array[i][j] == 1)
                {
                    count++;
                    DFS(array, i, j, row, column);
                }
            }
        }
        return count;
    }
}
