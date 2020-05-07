import java.io.*;
import java.net.*;
import java.util.*;
public class DateClient {

    public static void main(String[] args) throws IOException {

        if (args.length != 1) {

            System.err.println("Pass the server IP as the sole command line argument");

            return;

        }

        var socket = new Socket(args[0], 9090);

        var in = new Scanner(socket.getInputStream());

        System.out.println("Server response: " + in.nextLine());

    }

}
