import java.io.*;
import java.net.*;



public class ChatClientt{



	public static void main(String[] args)

	{

		Socket s = new Socket("192.168.40.255",10500); //bind socket

		System.out.println("Server connected");

		

		

		PrintWriter input = new PrintWriter(s.getOutputStream());

		input.Println("Selamat pagi!");

		input.flush();

		

		InputStreamReader fromclient = new InputStreamReader (s.getInputStream);

		BufferedReader br = new BufferedReader(fromclient);

		

		String msg = br.readLine();

		System.out.println("Server:" + word);

		

		

		

		

	}

}
