package gui;

import java.io.IOException;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.sql.SQLOutput;

public class callProgram {
    public static void main(String[] args){
        ScriptPython scriptPython = new ScriptPython();
        scriptPython.runScript("test");
    }

}

class ScriptPython {
    Process mProcess;

    public void runScript(String script){
        Process process;
        try{
            process = Runtime.getRuntime().exec(new String[]{script,"arg1","arg2"});
            mProcess = process;
            System.out.println("Script should have been executed");
            BufferedReader in = new BufferedReader(new InputStreamReader(mProcess.getInputStream()));
            System.out.println("value is : "+in);

        }catch(Exception e) {
            System.out.println("Exception Raised" + e.toString());
        }
        InputStream stdout = mProcess.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(stdout,StandardCharsets.UTF_8));
        String line;
        try{
            while((line = reader.readLine()) != null){
                System.out.println("stdout: "+ line);
            }
        }catch(IOException e){
            System.out.println("Exception in reading output"+ e.toString());
        }
    }

}

