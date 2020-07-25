#!/bin/zsh

cd "$(dirname "$0")"

/Library/Java/JavaVirtualMachines/jdk-14.0.1.jdk/Contents/Home/bin/java --module-path /Users/kogan/javafx/javafx-sdk-14.0.1/lib --add-modules=javafx.base,javafx.controls,javafx.fxml,javafx.graphics,javafx.media,javafx.swing,javafx.web,javafx.swt --add-modules javafx.base,javafx.graphics --add-reads javafx.base=ALL-UNNAMED --add-reads javafx.graphics=ALL-UNNAMED -Djava.library.path=/Users/kogan/javafx/javafx-sdk-14.0.1/lib -Dfile.encoding=UTF-8 -classpath /Users/kogan/Desktop/Comp-Projects/github/ApologyVideoGenJava/out/production/test2:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/src.zip:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx-swt.jar:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx.web.jar:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx.base.jar:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx.fxml.jar:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx.media.jar:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx.swing.jar:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx.controls.jar:/Users/kogan/javafx/javafx-sdk-14.0.1/lib/javafx.graphics.jar gui.Main

