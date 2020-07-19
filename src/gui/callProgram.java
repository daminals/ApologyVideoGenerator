package gui;

import java.io.IOException;

import java.io.*;

public class callProgram {
    public static void main(String[] args) {
        //runCommand("1234","im just rly sorry ok");

        String[] command = new String[] {"/bin/zsh","-c", "python3 python/test.py main"};
        try {
            Process p = Runtime.getRuntime().exec(command);
            printResults(p);

        } catch (IOException e) {
            e.printStackTrace();
        }


    }

    public static void printResults(Process process) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line = "";
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
    }

    public static void runCommand(String ID, String reason) {
        String[] command = new String[] {"/bin/zsh","-c", "python3 python/main.py main --bool_inp=True --ID="+ID+" --apolo='"+ reason +"'"};
        try {
            //Process proc = new ProcessBuilder(command).start();
            //Process p = Runtime.getRuntime().exec(command);
            Process p = Runtime.getRuntime().exec(command);
            printResults(p);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
