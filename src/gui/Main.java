package gui;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.fxml.*;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import javafx.scene.media.*;

public class Main extends Application{

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("gui.fxml"));

        primaryStage.setTitle("Apology Video Generator");
        primaryStage.getIcons().add(new Image("file:src/media/Ico.png"));
        primaryStage.setScene(new Scene(root, 700, 400));
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}

