import java.io.File;
import java.util.Scanner;
public class Emails 
{
	public static void main(String[] args) throws Exception 
	{
	      Scanner input = new Scanner(new File("students.csv"));
	      String students = "";
	      String student = "";
	      
	      input.nextLine();
	      
	      while (input.hasNextLine())
	      { //sample student Bob Rogers with student id 1234
	    	  try {
			      String[] last = input.nextLine().split(","); // {"ROGERS}
			      String[] first = last[1].split("/"); // {B, 1234"}
			      
			      if (last[0].substring(1,last[0].length()).contains(" "))	
			    	  student = first[0].substring(0,1) + last[0].substring(1,last[0].indexOf(" ")) + last[0].substring(last[0].indexOf(" ") + 1) + first[1].substring(1,5);
			      else if ( last[0].substring(1,last[0].length()).contains("-")
)			    	  student = first[0].substring(0,1) + last[0].substring(1,last[0].indexOf("-")) + last[0].substring(last[0].indexOf("-") + 1) + first[1].substring(1,5);
			      else
			    	  student = first[0].substring(0,1) + last[0].substring(1,last[0].length()) + first[1].substring(1,5);
			      
			      students += student + "@bths.edu, ";

	    	  	}
	    	  catch (StringIndexOutOfBoundsException e)
	    	  {
	    	      input.nextLine();
	    	  }
	      }
	      	input.close();
	      	System.out.println(students);
	}
}
	
