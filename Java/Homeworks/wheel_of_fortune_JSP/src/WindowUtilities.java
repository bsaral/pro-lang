package hmwrk;

import javax.swing.*;
import java.awt.*;
/** A few utilities that simplify using windows in Swing. */
public class WindowUtilities {
/** Tell system to use native look and feel, as in previous
* releases. Metal (Java) LAF is the default otherwise.
*/
public static void setNativeLookAndFeel() {
try {
UIManager.setLookAndFeel
(UIManager.getSystemLookAndFeelClassName());
} catch(Exception e) {
System.out.println("Error setting native LAF: " + e);
}
}

}