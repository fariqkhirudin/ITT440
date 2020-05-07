import java.net.*;
import java.io.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.util.Date;
import java.io.PrintWriter;

public class DateClient2 {
	

	private static final String SERVER_IP = "192.168.40.135";
	private static final int SERVER_PORT = 9090;

	public static void main(String args[]) throws IOException
	
    {

	Socket socket = new Socket(SERVER_IP, SERVER_PORT);

	InputStream in = socket.getInputStream();
	BufferedReader input = new BufferedReader(new InputStreamReader(in));
	String serverResponse = input.readLine();

	System.out.println(serverResponse);

	socket.close();
	
	}
}
