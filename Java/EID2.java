/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		 Scanner input = new Scanner(System.in);
        int test = input.nextInt();
        for (int i = 0; i < test; i++) {
            int[] child = new int[3];
            int[] t = new int[3];
            for (int j = 0; j < 3; j++) {
                child[j] = input.nextInt();
            }
            for (int j = 0; j < 3; j++) {
                t[j] = input.nextInt();
            }
            boolean loop = true;
            int temp1 ;
            int temp2 ;
            while (loop)
            {
                loop = false;
                

                for (int j = 0; j < 2 ; j++) {
                    if(child[j] > child[j+1])
                    {
                        temp1 = child[j];
                        child[j] = child[j+1];
                        child[j+1] = temp1 ;

                        temp2 = t[j];
                        t[j] = t[j+1];
                        t[j+1] = temp2;
                        loop = true;
                    }
                }
            }
            boolean ans = true;
            for (int j = 0; j < 2; j++) {
                
                if(child[j] < child[j+1] && t[j] >= t[j+1])
                {
                    ans = false ;
                }
                if(child[j] == child[j+1] && t[j] != t[j+1])
                {
                    ans = false;
                }
            }
            if (ans)
            {
                System.out.println("FAIR");
            }
            else{
                System.out.println("NOT FAIR");
            }
        }
	}
}
