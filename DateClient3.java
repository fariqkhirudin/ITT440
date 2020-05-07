import java.io.*;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.util.Date;

public class DateClient3 {
	

	private static final String SERVER_IP = "192.168.40.135";
	private static final int SERVER_PORT = 4455;
	public static void main(String args[]) throws IOException
	
    {

	Socket socket = new Socket(SERVER_IP, SERVER_PORT);

	BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
	//String serverResponse = input.readLine();
	

	PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
	out.println("Selamat pagi!");
	out.flush();
	//System.out.println(serverResponse);
	
	}
}
