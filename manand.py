import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os
import tkinter as tk
from tkinter import filedialog
import warnings

print("""__  ______                    _____           __
\\ \\/ / __ \\____ ____  ____ __/__  /     _____/ /_  ____  ____
 \\  / / / / __ `/ _ \\/ __ `__ \\/ /     / ___/ __ \\/ __ \\/ __ \\
 / / /_/ / /_/ /  __/ / / / / / /__   (__  ) / / / /_/ / /_/ /
/_/_____/_\\__, /\\___/_/ /_/ /_/____/  /____/_/ /_/\\____/ .___/ 
        /____/                                       /_/   """)

root=tk.Tk()
root.withdraw() #Hide tk window
#root.title("maNand")
#root.geometry("500x500+300+100")
file_type=[("Binary files", "*.bin")] #Filetype constraint
#root.attributes("-alpha", 0.8) #window transparency

warnings.filterwarnings("ignore") #Ignore warning messages in console

#Reading Bytes
def extract_features(file_path):
    with open(file_path, 'rb') as file:
        byte_array = np.frombuffer(file.read(), dtype=np.uint8)
    #frequency calculation of each byte value (0-255)
    byte_counts = np.bincount(byte_array, minlength=256)
    return byte_counts / byte_counts.sum() #Normalization of each byte count , creating a probability distribution
# Load data
#good_files_dir = r'C:\Users\alex\Documents\CONSOLES\XBOX\J RUNNER\GOOD'
#good_files_dir=filedialog.askdirectory(title="Select Good Dump Data Folder!")
#bad_files_dir = r'C:\Users\alex\Documents\CONSOLES\XBOX\J RUNNER\BAD'
#bad_files_dir=filedialog.askdirectory(title="Select Bad Dump Data Folder!")

def check_folders(): #Checks if Bad and Good data folders are in the working dir
    current_dir = os.getcwd()
    good_files_dir = os.path.join(current_dir, 'GOOD')
    bad_files_dir = os.path.join(current_dir, 'BAD')
    good_exists = os.path.isdir(good_files_dir)
    bad_exists = os.path.isdir(bad_files_dir)
    return good_files_dir if good_exists else None, bad_files_dir if bad_exists else None
good_files_dir, bad_files_dir = check_folders() # Check for Good and Bad folders

X = []
y = []

# Extract features and labels for good files
for file_name in os.listdir(good_files_dir):
    file_path = os.path.join(good_files_dir, file_name)
    X.append(extract_features(file_path))
    y.append(1)  #Label for good files
#print(X)

# Extract features and labels for bad files
for file_name in os.listdir(bad_files_dir):
    file_path = os.path.join(bad_files_dir, file_name)
    X.append(extract_features(file_path))
    y.append(0)  #Label for bad files

X = np.array(X)
y = np.array(y)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Make predictions
y_pred = model.predict(X_test)

#Model evaluation
#print(f'Accuracy: {accuracy_score(y_test, y_pred)}')
#print(classification_report(y_test, y_pred))

#Input .bin and prediction
#def nand():
#    file_path=filedialog.askopenfilename(title="Select a nanddump.bin file", filetypes=file_type)
#    if file_path:
#        print("Selected File:", file_path)
nand=filedialog.askopenfilename(title="Select a nanddump.bin file",filetypes=file_type)

#import_button=tk.Button(root,text = "Input .Bin", command = nand)
#import_button.pack(pady=100)

if nand:
    print(f"Selected File: {nand}")
else:
    print(f"{nand} That's not a file directory!")
nand_features = extract_features(nand)
nand_pred = model.predict([nand_features])
a=print(f'Current Nand Status: {nand_pred[0]}')
if nand_pred == 1:
    print("Good Nand")
else:
    print("Bad Nand")

input("Press ENTER key to exit...")
