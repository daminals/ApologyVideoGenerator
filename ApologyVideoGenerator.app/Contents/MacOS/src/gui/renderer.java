package gui;

import java.io.*;

public interface renderer {
    static void printResults(Process process) throws IOException {
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String s = null;
        while ((s = stdInput.readLine()) != null)
        {
            System.out.println(s);
        }
    }
    static String runMainPY(String ID, String reason) {
      String arguments = "cd python && source venv/bin/activate && python main.py main --cli_input=true --ID='"+ID+"' --apolo='"+reason+"'";
      System.out.println("running..");
        try {
            String[] command = new String[] {"/bin/zsh","-c", arguments };
            Process p = Runtime.getRuntime().exec(command);
            printResults(p);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return "python/Finished/apology"+ID+".mp4";
    }
    static String gen_ID(int range){
        String ID = "";
        int rand;
        for (int i=0;i<range;i++){
            rand = (int) (Math.random() * 10);
            ID += Integer.toString(rand);
        }
        return ID;
    }
}
