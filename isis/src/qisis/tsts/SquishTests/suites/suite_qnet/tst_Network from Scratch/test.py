import os

def main():
    try:
        os.mkdir(os.path.expandvars('$ISISROOT/src/qisis/tsts/SquishTests/output'))
    except Exception:
        pass
    try:
        os.unlink(os.path.expandvars('$ISISROOT/src/qisis/tsts/SquishTests/output/') + 'NetworkFromScratch.net')
    except Exception:
        pass
    
    startApplication("qnet")
    
    # Open cube list
    activateItem(waitForObjectItem(":qnet_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Open control network and cube list"))
    snooze(0.5)
    mouseClick(waitForObject(":fileNameEdit_QLineEdit"), 95, 13, 0, Qt.LeftButton)
    type(waitForObject(":fileNameEdit_QLineEdit"), "../src/qisis/tsts/SquishTests/input/Ground/Extracted_AllOverlaps.lis")
    type(waitForObject(":_QListView"), "<Return>")

    clickButton(waitForObject(":Select a control network.Cancel_QPushButton"))
    
    mouseClick(waitForObject(":Control Network Navigator_QComboBox"), 105, 0, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Control Network Navigator_QComboBox", "Cubes"), 55, 6, 0, Qt.LeftButton)
    waitForObjectItem(":Navigator_List", "I01113006RDR\\.cub")
    doubleClickItem(":Navigator_List", "I01113006RDR\\.cub", 81, 8, 0, Qt.LeftButton)
    waitForObjectItem(":Navigator_List", "I01812006RDR\\.cub")
    doubleClickItem(":Navigator_List", "I01812006RDR\\.cub", 59, 12, 0, Qt.LeftButton)
    waitForObjectItem(":Navigator_List", "I02174006RDR\\.cub")
    doubleClickItem(":Navigator_List", "I02174006RDR\\.cub", 53, 9, 0, Qt.LeftButton)
    
    
    sendEvent("QMouseEvent", waitForObject(":qnet.viewport_QWidget_2"), QEvent.MouseButtonPress, 245, 245, Qt.MidButton, 4, 0)
    sendEvent("QMouseEvent", waitForObject(":qnet.viewport_QWidget_3"), QEvent.MouseButtonRelease, 245, 245, Qt.MidButton, 0, 0)
    clickButton(waitForObject(":Error.OK_QPushButton"))

    mouseClick(waitForObject(":qnet.viewport_QWidget_2"), 270, 207, 0, Qt.LeftButton)
    clickButton(waitForObject(":Warning.OK_QPushButton"))
    
    sendEvent("QMouseEvent", waitForObject(":qnet.viewport_QWidget_3"), QEvent.MouseButtonPress, 256, 306, Qt.RightButton, 4, 0)
    sendEvent("QMouseEvent", waitForObject(":qnet.viewport_QWidget_3"), QEvent.MouseButtonRelease, 256, 306, Qt.RightButton, 0, 0)
    type(waitForObject(":Point ID:_QLineEdit_2"), "Point_001")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Return>")
    mouseClick(waitForObject(":Right Measure_QComboBox"), 98, 7, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I02174006RDR\\.cub"), 105, 7, 0, Qt.LeftButton)
    mouseClick(waitForObject(":VP2"), 42, 129, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Left Measure.Edit Lock Measure_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 102, 6, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I06281019RDR\\.cub"), 50, 7, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Find_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.OK_QPushButton"))
    clickButton(waitForObject(":Right Measure.Ignore Measure_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    mouseClick(waitForObject(":QnetToolScroll.Right Measure_QGroupBox"), 92, 47, 0, Qt.LeftButton)
    mouseClick(waitForObject(":Right Measure_QComboBox"), 81, 12, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I08528020RDR\\.cub"), 54, 6, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Find_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 197, 7, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I09439017RDR\\.cub"), 93, 3, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Find_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.OK_QPushButton"))
    clickButton(waitForObject(":Right Measure.Ignore Measure_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 97, 12, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I17426045RDR\\.cub"), 66, 5, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Find_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Register_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 106, 4, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I27759024RDR\\.cub"), 57, 5, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Find_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Register_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 99, 4, 0, Qt.LeftButton)
    mouseClick(waitForObject(":QnetToolScroll.Left Measure_QGroupBox"), 362, 48, 0, Qt.LeftButton)
    mouseClick(waitForObject(":Left Measure_QComboBox"), 333, 15, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Left Measure_QComboBox", "I06281019RDR\\.cub"), 212, 8, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 75, 1, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I17426045RDR\\.cub"), 47, 4, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    sendEvent("QMouseEvent", waitForObject(":Left Measure.Edit Lock Measure_QCheckBox"), QEvent.MouseButtonPress, 307, 0, Qt.LeftButton, 1, 0)
    sendEvent("QMouseEvent", waitForObject(":Left Measure.Edit Lock Measure_QCheckBox"), QEvent.MouseButtonRelease, 307, 0, Qt.LeftButton, 0, 0)
    mouseClick(waitForObject(":Left Measure_QComboBox"), 325, 8, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Left Measure_QComboBox", "I17426045RDR\\.cub"), 113, 10, 0, Qt.LeftButton)
    clickButton(waitForObject(":Right Measure.Edit Lock Measure_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 123, 11, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I09439017RDR\\.cub"), 91, 4, 0, Qt.LeftButton)
    clickButton(waitForObject(":Right Measure.Edit Lock Measure_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    mouseClick(waitForObject(":VP2"), 144, 147, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.No_QPushButton"))
    mouseClick(waitForObject(":Left Measure_QComboBox"), 330, 7, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Left Measure_QComboBox", "I09439017RDR\\.cub"), 196, 4, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    mouseClick(waitForObject(":VP2"), 163, 152, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 101, 7, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I08528020RDR\\.cub"), 93, 5, 0, Qt.LeftButton)
    clickButton(waitForObject(":Right Measure.Edit Lock Measure_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    type(waitForObject(":VP2"), "<Down>")
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    clickButton(waitForObject(":Control Point.Ignore Point_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    mouseClick(waitForObject(":Right Measure_QComboBox"), 66, 10, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I02174006RDR\\.cub"), 59, 1, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Register_QPushButton"))
    clickButton(waitForObject(":Error.OK_QPushButton"))
    mouseClick(waitForObject(":VP2"), 155, 144, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.Yes_QPushButton"))
    clickButton(waitForObject(":Control Point.Ignore Point_QCheckBox"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.No_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Measure_QPushButton"))
    clickButton(waitForObject(":Qnet Tool Save Measure.No_QPushButton"))
    mouseClick(waitForObject(":Left Measure_QComboBox"), 384, 9, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Left Measure_QComboBox", "I06281019RDR\\.cub"), 261, 10, 0, Qt.LeftButton)
    mouseClick(waitForObject(":Left Measure_QComboBox"), 292, 4, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Left Measure_QComboBox", "I02174006RDR\\.cub"), 238, 6, 0, Qt.LeftButton)
    mouseClick(waitForObject(":Right Measure_QComboBox"), 207, 11, 0, Qt.LeftButton)
    mouseClick(waitForObjectItem(":Right Measure_QComboBox", "I02174006RDR\\.cub"), 136, 6, 0, Qt.LeftButton)
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    sendEvent("QMouseEvent", waitForObject(":qnet.viewport_QWidget_3"), QEvent.MouseButtonPress, 251, 292, Qt.RightButton, 4, 0)
    sendEvent("QMouseEvent", waitForObject(":qnet.viewport_QWidget_3"), QEvent.MouseButtonRelease, 251, 292, Qt.RightButton, 0, 0)
    
    
    mouseClick(waitForObject(":Point ID:_QLineEdit_2"), 2, 6, 0, Qt.LeftButton)
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Delete>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "2")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Backspace>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "1")
    
    #clickButton(waitForObject(":Create New ControlPoint.OK_QPushButton"))
    #clickButton(waitForObject(":New Point Id.OK_QPushButton"))
    
    mouseClick(waitForObject(":Point ID:_QLineEdit_2"), 2, 6, 0, Qt.LeftButton)
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Delete>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "2")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Backspace>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "1")
    
    #clickButton(waitForObject(":Create New ControlPoint.OK_QPushButton"))
    #clickButton(waitForObject(":New Point Id.OK_QPushButton"))
    
    mouseClick(waitForObject(":Point ID:_QLineEdit_2"), 2, 6, 0, Qt.LeftButton)
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Right>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "<Delete>")
    type(waitForObject(":Point ID:_QLineEdit_2"), "2")
    
    clickButton(waitForObject(":Create New ControlPoint.OK_QPushButton"))
    clickButton(waitForObject(":QnetToolScroll.Save Point_QPushButton"))
    
    # Save resulting network
    activateItem(waitForObjectItem(":qnet_QMenuBar", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Save Control Network As..."))
    clickButton(waitForObject(":Choose filename to save under.toParentButton_QToolButton"))
    snooze(0.5)
    mouseClick(waitForObject(":fileNameEdit_QLineEdit_3"), 95, 13, 0, Qt.LeftButton)
    type(waitForObject(":fileNameEdit_QLineEdit_3"), "src/qisis/tsts/SquishTests/output/NetworkFromScratch.net")
    snooze(0.5)
    type(waitForObject(":fileNameEdit_QLineEdit_3"), "<Return>")

    activateItem(waitForObjectItem(":qnet_QMenuBar_2", "File"))
    activateItem(waitForObjectItem(":qnet.File_QMenu", "Exit"))
    snooze(1)