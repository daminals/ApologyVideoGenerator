package gui;

import javax.xml.stream.events.Comment;
import java.io.IOException;

import java.io.*;
import java.security.PublicKey;
import java.util.*;

public class callProgram implements Runnable{

    public String ID;
    public String reason;

    public callProgram(String ID, String reason){
        this.ID = ID;
        this.reason = reason;
    }


    public static void main(String[] args) throws IOException {
        //runMainPY("1234","bcuz");
        //System.out.println(gen_ID(4));

    }


    public static void printResults(Process process) throws IOException {
        BufferedReader stdInput = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String s = null;
        while ((s = stdInput.readLine()) != null)
        {
            System.out.println(s);
        }
    }



    public static void runMainPY(String ID, String reason) {
        try {
            String[] command = new String[] {"/bin/zsh","-c","cd python && source venv/bin/activate && python main.py main --bool_inp=True --ID='"+ID+"' --apolo='"+reason+"'" };
            Process p = Runtime.getRuntime().exec(command);

            printResults(p);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static String gen_ID(int range){
        String ID = "";
        int rand;
        for (int i=0;i<range;i++){
            rand = (int) (Math.random() * 10);
            ID += Integer.toString(rand);
        }
        return ID;
    }

    @Override
    public void run() {
        runMainPY(ID,reason);

    }

    /*

    public static void Venv(){
        try {
            Process p = Runtime.getRuntime().exec(command);
            printResults(p);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void correctDir(){
        String[] command = new String[] {"/bin/zsh","-c", "cd python"};
        try {
            Process p = Runtime.getRuntime().exec(command);
            printResults(p);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    */
}
