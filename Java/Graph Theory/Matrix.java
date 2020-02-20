public class Matrix 
{
	public Matrix() {}
	
	/**
	Removes a row and a column from a 2D array. For example, cutGraph({
                                                          {1,2,3},
                                                          {1,2,3},
                                                          {1,2,3}}, 
                                                          returns
                                                          {
                                                          {1,3},
                                                          {1,3}
                                                          }
	 * @param arr The array
	 * @param i The column and row index to remove
	 * @return The new array
	 */
	public static int[][] cutGraph(int[][] arr, int i)
	{
		int[][] shortArray = new int[arr.length-1][arr.length-1];
		
		for (int x = 0; x < i; x++)
			for (int y = 0; y < i; y++)
				shortArray[x][y] = arr[x][y];
		for (int x = i + 1; x < arr.length; x++)
			for (int y = 0; y < i; y++)
				shortArray[x-1][y] = arr[x][y];
		
		for (int x = 0; x < i; x++)
			for (int y = i + 1; y < arr.length; y++)
				shortArray[x][y-1] = arr[x][y];

		for (int x = i + 1; x < arr.length; x++)
			for (int y = i + 1; y < arr.length; y++)
				shortArray[x-1][y-1] = arr[x][y];
		
		return shortArray;
	}
}
