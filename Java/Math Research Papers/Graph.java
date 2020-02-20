public class Graph 
{
	private int[] visitedVerticies;
	public Graph(int[] visited)
	{
		visitedVerticies = visited;
	}
	public int[] vicinity(int[][] matrix, int radius, int vertex, int currentMax)
	{		
		if (!contains(visitedVerticies, vertex))				//this checks if visitedVerticies contains vertex	 
		{													 	//and if not, adds vertex to visitedVerticies
			int[] temp = new int[visitedVerticies.length + 1];	//int[] visitedVerticies is an instance variable
															
			for (int i = 0; i < visitedVerticies.length; i++)			
				temp[i] = visitedVerticies[i];
			
			temp[temp.length - 1] = vertex;						
			visitedVerticies = temp;											
		}
		for (int i = 0; i < matrix.length; i++)
			if (
				matrix[vertex][i] != 0 						&&  // make sure it's an edge
				currentMax + matrix[vertex][i] <= radius 	&&  // make sure currentMax does not exceed radius
				i != vertex										// verify we don't backtrack
				)
				vicinity(matrix, radius, i, currentMax + matrix[vertex][i]);
		return visitedVerticies;
	}


	public static int[][] buildMatrix(int size, int width, int hor, int ver)
	{
		int[][] matrix = new int[size][size];
		int vertex;
		
		//Degree 4 vertices
		for (int y = 1; y < (size / width) - 1; y++)
			for (int i = 1; i < width - 1; i++)
			{
				matrix[y * width + i][y * width + i - 1] = hor;
				matrix[y * width + i][y * width + i + 1] = hor;
				matrix[y * width + i][y * width + i - width] = ver;
				matrix[y * width + i][y * width + i + width] = ver;
			}
		
		//top	
		for (int i = 1; i < width - 1; i++)
		{
			matrix[i + 1][i] = hor;
			matrix[i - 1][i] = hor;
			
			matrix[i][i + width] = ver;
		}
		//bottom
		for (int i = size - width + 1; i < size - 1; i++)
		{
			matrix[i + 1][i] = hor;
			matrix[i - 1][i] = hor;
			
			matrix[i][i - width] = ver;
		}
		//left
		for (int y = 1; y < (size / width) - 1; y++)
		{
			vertex = y * width;
			matrix[vertex][vertex + 1] = hor;
			
			matrix[vertex][vertex - width] = ver;
			matrix[vertex][vertex + width] = ver;
		}
		//right
		for (int y = 1; y < (size / width) - 1; y++)
		{
			vertex = size - width * y - 1;
			matrix[vertex][vertex - 1] = hor;
			
			matrix[vertex][vertex + width] = ver;
			matrix[vertex][vertex - width] = ver;
		}
		//corners
		matrix[1][0] = hor; 
		matrix[0][width] = ver;
		
		matrix[width - 2][width - 1] = hor;
		matrix[width - 1][width - 1 + width] = ver;
		
		matrix[size - width + 1][size - width] = hor;
		matrix[size - width][size - width - width] = ver;
		
		matrix[size - 2][size - 1] = hor;
		matrix[size - 1][size - 1 - width] = ver;
		return matrix;
	}
	
	
	public static boolean contains(int[] arr, int i)
	{
		for (int n : arr)
			if (n == i)
			return true;
		return false;
	}
	
	
	public static int[] add(int[] arr, int[] arr2)
	{
		int[] temp = new int[arr.length + arr2.length];
		for (int i = 0; i < arr.length; i++)
			temp[i] = arr[i];
		for (int i = arr.length; i < temp.length; i++)
			temp[i] = arr2[i - arr.length];
		
		return temp;
	}
	
	
	public static int[] add(int[] arr, int j)
	{
		int[] temp = new int[arr.length + 1];
		for (int i = 0; i < arr.length; i++)
			temp[i] = arr[i];
		
		temp[temp.length - 1] = j;
		arr = temp;
		return temp;
	}


	public static String printArray(int[] arr)
	  {
		  if (arr.length == 0)
			  return "[]";
	    String str = "[";
	    for (int i = 0; i < arr.length - 1; i++)
	        str += arr[i] + ", ";
	    str += arr[arr.length - 1] + "]";

	   return str;
	  }
	
	  public static void printArray(int[][] arr)
	  {
		  for (int[] a : arr)
			  System.out.println(printArray(a));
	  }
	  public static void arrayToTxt(int[][] arr) throws IOException
	  {
			FileWriter fw = new FileWriter("passwords.txt"); 
		    for (int[] a : arr)
		    {
		    	fw.write(printArray(a),0, printArray(a).length());
		    	fw.write(System.getProperty("line.separator"));       
		    }
			    fw.close(); 
	  }
	
	public static int indexOfMax(int[] arr)
	{
		 int max = 0;
		 for (int i = 1; i< arr.length; i++)
			 if (arr[max] < arr[i])
				 max = i;
		 return max;
	 }
	  
	 public static int[] unvistedDegree(int[][] matrix, boolean[] visited)
	 {	
		 int count = 0;
		 int[] degrees = new int[matrix.length];

		  
		 for (int j = 0; j < matrix.length; j++)
		 {
			 if (!visited[j])
			 {
				 for (int i = 0; i < matrix.length; i++)
					if (matrix[i][j] != 0 && !visited[i])
						count++;
				 degrees[j] = count;
			 }
			 else		 
				 degrees[j] = -1;
			 
			 count = 0;
		 }
		 return degrees;
	  }
	  
	  public static int[] solve(int[][] matrix, int radius)
	  {
		  Graph obj;
		  int count = 0;
		  int[] centers = new int[0];
		  int[] subgraph;
		  int minDegree;
		  boolean[] visited = new boolean[matrix.length];
		  
		  while (count < matrix.length)
		  {
			  obj = new Graph(new int[] {});				     //Creating a Graph object is necessary for the vicinity graph 
			  												     //since it holds the visited vertices specifically to its subgraph.
			  minDegree = indexOfMax(unvistedDegree(matrix, visited)); //vertex with greatest unvisited degree
			  subgraph = obj.vicinity(matrix, radius, minDegree, 0);   //subgraph of minDegree
			  
			  for (int n : subgraph) 							 //mark visited vertices
				  if (!visited[n])  
				  {
					  visited[n] = true;
					  count++;		
					  //tracks how many true's are in the visited array to save time
				  }
			  centers = add(centers, minDegree);				 //adds two arrays
			  System.out.println(count);							
		  }	 
		  return centers;
	}	
	  

	private static String printArray(boolean[] arr)
	{
		if (arr.length == 0)
			  return "[]";
	    String str = "[";
	    for (int i = 0; i < arr.length; i++)
		if (!arr[i])
		str += i + ", ";
	  return str;
	}

	public static int[][] cutGraph(int[][] arr, int low, int high)
	{
		int[][] shortArray = new int[arr.length - (high - low + 1)][arr.length - (high - low + 1)];

		for (int x = 0; x < low; x++)
			for (int y = 0; y < low; y++)
				shortArray[x][y] = arr[x][y];

		for (int x = high + 1; x < arr.length; x++)
			for (int y = 0; y < low; y++)
				shortArray[low + x - high - 1][y] = arr[x][y];

		for (int x = 0; x < low; x++)
			for (int y =  high + 1; y < arr.length; y++)
				shortArray[x][low + y - high - 1] = arr[x][y];

		for (int x = high + 1; x < arr.length; x++)
			for (int y = high + 1; y < arr.length; y++)
				shortArray[low + x - high - 1][low + y - high - 1] = arr[x][y];

		return shortArray;

	}
}
