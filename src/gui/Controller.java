package gui;
import java.io.File;

import javafx.scene.media.*;
import javafx.fxml.Initializable;
import javafx.geometry.*;
import javafx.scene.control.*;
import javafx.scene.layout.*;

import java.net.URL;
import java.util.ResourceBundle;

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

    }

    MediaPlayer mediaPlayer;
    Media media = new Media(new File("src/media/video.mp4").toURI().toString());

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        pane.setPadding(new Insets(0,0,0,13));
        leUserControl.setVisible(false);
        Timer.setVisible(false);

        fileName.setText("video.mp4");
        fileName.setVisible(false);

        mediaPlayer = new MediaPlayer(media);
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
