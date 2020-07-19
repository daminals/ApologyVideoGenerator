package gui;
import java.io.*;

import javafx.scene.media.*;
import javafx.fxml.Initializable;
import javafx.geometry.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import java.nio.*;
import java.nio.file.*;


import java.net.URL;
import java.nio.file.FileSystems;
import java.nio.file.WatchService;
import java.security.PublicKey;
import java.util.*;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import javafx.util.Duration;


//TODO: Make program report current messages (processing audio... processing video... etc)

public class Controller implements Initializable {

    public Button build;
    public TextField videoText;
    public MediaView mediaView;
    public GridPane pane;
    public Label fileName;
    public Button play;
    public HBox leUserControl;
    public boolean pause_play = true;
    public Slider Timer;
    public String ID;

    ExecutorService avg = Executors.newFixedThreadPool(3);

    public void build(){
        String reason = videoText.getText();
        videoText.clear();
        System.out.println(reason);
        mediaView.setVisible(true);
        fileName.setVisible(true);
        leUserControl.setVisible(true);
        Timer.setVisible(true);

        mediaPlayer.currentTimeProperty().addListener((observable, oldTime, newTime) -> {
            Timer.setValue((newTime.toMillis() / mediaPlayer.getTotalDuration().toMillis())*100);
        });
        Timer.valueProperty().addListener((observable,oldValue,newValue) -> {
            if (Math.abs((double) newValue - (double) oldValue) >= 0.5) {
                Double difference = (double) newValue / 100;
                Duration bruh = Duration.millis(difference);
                Duration comp = bruh.multiply(mediaPlayer.getTotalDuration().toMillis());
                mediaPlayer.seek(comp);
            }
        });

        ID = callProgram.gen_ID(4);
        callProgram ApologyVideo = new callProgram(ID,reason);
        avg.execute(ApologyVideo);
        //callProgram.runMainPY(ID,reason);

        media = new Media(new File("python/Finished/apology"+ID+".mp4").toURI().toString());
        mediaPlayer = new MediaPlayer(media);
        mediaView .setMediaPlayer(mediaPlayer);

    }

    public MediaPlayer mediaPlayer;
    public Media media;
    public Media loading;

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        pane.setPadding(new Insets(0,0,0,13));
        leUserControl.setVisible(false);
        Timer.setVisible(false);

        fileName.setText("video.mp4");
        fileName.setVisible(false);
        loading = new Media(new File("src/media/ytload.mp4").toURI().toString());

        mediaPlayer = new MediaPlayer(loading);
        mediaPlayer.setAutoPlay(false);
        mediaView.setMediaPlayer(mediaPlayer);
        mediaView.setVisible(false);
    }

    public void play() {
        if (pause_play){
            play.setText("||");
            mediaPlayer.play();
            pause_play = false;
        }else{
            play.setText(">");
            mediaPlayer.pause();
            pause_play = true;
        }
    }
}
