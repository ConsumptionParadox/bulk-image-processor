# bulk-image-processor

<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/GUI.png" width="600">
<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/input.png" width="500">
<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/result.png" width="500">

### Summary 
Quickly converts all images in a folder to .png files and prepends a desired brand as well as a desired suffix ( currently used for image orientation ). Note that this application also removes any symbols or spaces from the initial file name but adds underscores after prepended brand name and before appeneded orientation. The code is nondestructive meaning the original files are kept completely intact. This was coded for MacOS and so there is a .DS_Store check to avoid halting execution as well as any data loss. It should work fine one windows but keep in mind it has not been tested. 

### Requirements 
* Python 3 (written and tested in Python 3.10)
* PIL (pillow module)
* PYSimpleGUI

### Usage 

1. Run main.py (ensure both toolset.py is stored within the same folder). This will activate the GUI interface: 

<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/GUI.png" width="600">

2. After selecting your folder of images (source folder) as well as the output folder (destination folder), select your brand from the drop down menu: 

<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/SelectBrand.png" width="600">

3. Then select the orientation of the image where P: Primary, F: Front, B: Back, L: Left, R: Right, and A: Additional:

<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/Orientation.png" width="600">

4. Enable the 'Confirm Name' checkbox if desired. This allows for the user to override the new name if it is incorrect or a different name is desired for a particular file: 

<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/Enable.png" width="600">

5. Press the 'Start' button located on the bottom right to begin the process. If 'Confirm Name' was enabled, a new window will appear allowing the user to override the new name before commiting to saving. Once a desired name is chosen, select 'OK' to proceed to the next file. Note: If 'Confirm Name' is disabled, processing the file names will happen very quickly. Testing with hundreds of images at once only took about 3 seconds: 

<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/confirm.png" width="600">

### Input Images:
<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/input.png" width="600">

### Output Images: 
<img src="https://github.com/ConsumptionParadox/bulk-image-processor/blob/main/img/result.png" width="600">


