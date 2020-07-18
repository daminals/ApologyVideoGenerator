package sample;

import java.io.File;
import java.net.MalformedURLException;
import javafx.fxml.Initializable;
import javafx.geometry.Insets;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.media.Media;
import javafx.scene.media.MediaView;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.fxml.*;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.media.*;
import java.net.URL;
import java.util.ResourceBundle;


public class Controller implements Initializable {

    public Button build;
    public TextField videoText;
    public MediaView mediaView;
    public GridPane pane;
    public Label fileName;

    public void build(){
        String reason = videoText.getText();
        videoText.clear();
        System.out.println(reason);
        mediaView.setVisible(true);
        mediaPlayer.setAutoPlay(true);

    }

    MediaPlayer mediaPlayer;
    Media media = new Media(new File("src/media/video.mp4").toURI().toString());

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        pane.setPadding(new Insets(0,0,0,13));

        mediaPlayer = new MediaPlayer(media);
        mediaPlayer.setAutoPlay(false);
        mediaView.setMediaPlayer(mediaPlayer);
        mediaView.setVisible(false);

        }

}
