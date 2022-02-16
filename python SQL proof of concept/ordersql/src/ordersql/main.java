package ordersql;

import java.io.*;

public class main {
	
		public static void main(String a[]) {
			try {
				ProcessBuilder builder = new ProcessBuilder();
				builder.command("python.exe", "../pythonsql.py");
				builder.redirectErrorStream(true);
				Process p = builder.start();
				BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
				String line;
		        while (true) {
		            line = r.readLine();
		            if (line == null) { break; }
		            System.out.println(line);
		        }
			}catch(Exception e) {}
		}
}
