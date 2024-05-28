<h1 align="center">maNand XBOX 360 Corrupted Nand Checker</h1>
<p align="center">
  <img src="https://img.shields.io/badge/PROJECT_STATUS-🟠-orange" alt="Project Status">
</p>
<p align="center">
  <strong>🟠 - Working but in Testing phase, 🟢 - Working, 🔴 - Not Working</strong>
</p>
<p align="center">
  This simple Python program uses Machine Learning to check if a NAND dump the user provides is "Good" in terms of corruption. Corrupted NANDs are a significant issue in the XBOX 360 modding scene. Prevent your XBOX 360 from getting bricked with this tool!
</p>
<p align="center">
  <em style="color:red;"><strong>Currently only 16MB nands are supported. 256MB or 4GB nands will not get the correct classification and the result will be misleading. DO NOT RISK IT</strong></em>
</p>
<h2 align="center">CHANGELOG</h2>
<p align="center">
  None
</p>
<h2 align="center">FUTURE GOALS</h2>
<ul align="center">
  <li>Enrich the algorithm with more training data (Hard to collect as many XBOX 360 consoles are needed)</li>
  <li>Build a user-friendly GUI</li>
</ul>
<h2 align="center">HOW TO USE</h2>
<h3 align="center">WINDOWS/LINUX</h3>
<p align="center">Assuming you have Python installed:</p>
<ol align="center">
  <li>Run CMD or Terminal</li>
  <li>Type: <code>cd "&lt;maNand directory&gt;"</code> (keep the double quotation marks, you may have spaces between your folder names)</li>
  <li>Type: <code>python main.py</code> or <code>python3 main.py</code> </li>
</ol>
<p align="center">MAKE SURE THE "BAD" AND "GOOD" FOLDERS ARE IN THE MAIN maNand DIRECTORY</p>
<h2 align="center">Needed Libraries</h2>
<ul align="center">
  <li>numpy</li>
  <li>scikit-learn</li>
  <li>Tkinter (Future package)</li>
  <li>os-sys</li>
</ul>
