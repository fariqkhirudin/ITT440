import java.io.*;
import java.net.*;



public class ChatClient{



	public static void main(String[] args)

	{

		Socket s = new Socket("192.168.40.255",10500); //bind socket

		System.out.println("Connecting to server.");


		PrintWriter input = new PrintWriter(s.getOutputStream());

		

		input.println("Selamat pagi.");
		input.flush();
		

		InputStreamReader fromclient = new InputStreamReader (s.getInputStream);
		BufferedReader br = new BufferedReader(fromclient);
		String serverMsg = br.readLine();

		System.out.println("Server:" + serverMsg);

		

		

		

		

	}

}
  