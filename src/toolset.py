from pathlib import Path
from PIL import Image
import shutil
import PySimpleGUI as sg


# Insert your common image folder paths as defaults
_source_dir = Path('')
_dest_dir = Path('')


def empty_destination(dest_dir=_dest_dir):
    '''
    Clears the contents of destination folder to prevent overlap

        Parameters:
            dest_dir (str): Path to the destination folder
    '''
    print('clearing dest')
    for file in Path(dest_dir).iterdir():
        file.unlink()
    print('done')

def copy_files_to_dest(source_dir=_source_dir, dest_dir=_dest_dir):
    '''
    Copies files from source folder to destination folder for processing

        Parameters:
            dest_dir (str): Path to the folder to output images
            source_dir (str): Path to folder to retrieve images for processing
    '''
    print('copying files')
    for file in Path(source_dir).iterdir():
        print(file)
        if str(file) != 'ConvertImage/source/in/.DS_Store':
            if file.is_file():
                shutil.copy(file, dest_dir)
    print('files copied')

def convert_to_png(dest_dir=_dest_dir, convert_to='.png'):
    print('converting')
    for image_to_convert in Path(dest_dir).iterdir():
        if str(image_to_convert) != f"{image_to_convert.parent}/.DS_Store":
            if image_to_convert.is_file() and image_to_convert.suffix != convert_to:
                #original file
                old_name = image_to_convert.stem
                new_extension = '.png'
                directory = image_to_convert.parent

                # creating image object
                img = Image.open(image_to_convert)

                #what to rename files
                new_name = f"{old_name}{new_extension}"
                img.save(f'{directory}/{new_name}')

                image_to_convert.unlink()

def brand_image(brand:str, img_pos:str = "P", enabled = False, dest_dir=_dest_dir):
    print('Branding')
    for path in Path(dest_dir).iterdir():
        if str(path) != f"{path.parent}/.DS_Store":
            if path.is_file():
                #original file
                old_name = path.stem
                old_extension = path.suffix
                directory = path.parent

                #removing any special characters from the name:
                name = ''.join(char for char in old_name if char.isalnum())

                #what to rename files
                new_path = f"{brand}_{name}_{img_pos}"

                #add path, confirm name change if enabled:
                new_path = f"{confirm_change(new_path, enabled)}{old_extension}"

                #renaming the actual path
                path.rename(Path(directory, new_path))

#optional
def confirm_change(_name: str, _enabled : bool):
    '''If enabled, does a confirmation check that allows for the overwriting of new name'''
    if _enabled:
        layout = [
            [sg.Input(f'{_name}', key='-INPUT-', font='Franklin 20'), sg.Button('OK', key='-CONFIRM-')]
        ]
        window = sg.Window('Confirm', layout)
        event,values = window.read()

        if event == '-CONFIRM-':
            window.close()
            return values['-INPUT-']
            
    
    else:
        return _name

def process_images(brand_name, image_orientation, enabled : bool, source_dir, dest_dir):
    empty_destination(dest_dir)
    copy_files_to_dest(source_dir, dest_dir)
    convert_to_png(dest_dir)
    brand_image(brand_name.upper(), image_orientation.upper(), enabled, dest_dir)

def DisplayUI():
    '''Change brand names to your desired name prefix'''
    title = 'File Brander'
    brands = ['G2G','FUSION','LEVO','ELIT','CGC','GCM']
    orientations = ['P','F','B','L','R','A']
    layout = [
        [sg.Text("Source Folder: ", font = 'Franklin 20',expand_x = True), sg.Input( key='-SOURCEIN-',change_submits=True, ), sg.FolderBrowse(key="-SOURCEFOLDER-", initial_folder=_source_dir)],
        [sg.Text("Destination Folder: ", font = 'Franklin 20', expand_x = True), sg.Input(key='-DESTIN-'), sg.FolderBrowse(key="-DESTFOLDER-", initial_folder=_dest_dir)],
        [sg.Text('Brand: ',key='-BRANDTEXT-', font = 'Franklin 20', expand_x = True), sg.Combo(brands, key='-BRAND-', default_value=brands[0], font= '16', expand_x = True,readonly=True)],
        [sg.Text('Orientation: ', key='-ORIENTEXT-', font = 'Franklin 20'), sg.Combo(orientations, key='-ORIENTATION-', default_value=orientations[0],font= '16', expand_x = True, readonly=True)],
        [sg.Text('Confirm Name: ',key='-BRANDTEXT-', font = 'Franklin 20'), sg.Checkbox('Enable', key='-ENABLE-',font= '16', expand_x = True)],
        [sg.Button('Start',key='-START-')]
    ]
    window = sg.Window(title, layout)

    while True:
        event,values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        if event == '-START-':
            print(values)
            process_images(
                values['-BRAND-'],
                values['-ORIENTATION-'],
                values['-ENABLE-'],
                values['-SOURCEFOLDER-'],
                values['-DESTFOLDER-']
            )
            #window.close()
            
                    
def StartApp():
    DisplayUI()
    

#one liner
#sg.Window('', [[sg.Input(), sg.Button('OK'), sg.Button('Cancel')]]).read()