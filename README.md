##maNand XBOX 360 Corrupted Nand Checker##

##PROJECT STATUS##: 🟠
# 🟠 - Working but in Testing phase, 🟢 - Working, 🔴 - Not Working

#This simple Python program uses Machine Learning to check if a nand dump the user provides is "Good" in terms of corruption. Corrupted nands are a huge problem in XBOX 360 modding scene. Prevent your XBOX 360 from getting bricked with this tool!

##CHANGELOG: nOnE##

##FUTURE GOALS##:
-Enrich the algorithm with more training data (Hard to collect as many XBOX 360 consoles are needed)
-Build a user-friendly GUI

###HOW TO USE##:
##WINDOWS##:
#Assuming you have python installed:
-Run CMD
-type: cd "<maNand directory>" (keep the double quotation marks, you may have spaces between your folder names)
-type: python main.py
*MAKE SURE THE "BAD" AND "GOOD" FOLDERS ARE IN THE MAIN maNand DIRECTORY*

##LINUX##:
#Assuming you have python installed:
#RUN maNand: cd "<maNand directory>" (keep the double quotation marks, you may have spaces between your folder names)
*MAKE SURE THE "BAD" AND "GOOD" FOLDERS ARE IN THE MAIN maNand DIRECTORY*

##Needed Libraries:##
-pip3 install numpy
-pip3 install -U scikit-learn
-Install Tkinter package: https://www.geeksforgeeks.org/how-to-install-tkinter-on-linux/
-pip3 install os-sys
