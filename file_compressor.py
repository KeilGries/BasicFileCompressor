import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text('Select files to compress:', background_color='black')
input1 = sg.Input('')
choose_button1 = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text('Select destination folder:', background_color='black')
input2 = sg.Input('')
choose_button2 = sg.FolderBrowse('Choose', key='folder')

compress_button = sg.Button('Compress')
output_label = sg.Text(key='output', background_color='black', text_color='green')

window = sg.Window("File Compressor", background_color='black',
                                      layout=[[label1, input1, choose_button1],
                                              [label2, input2, choose_button2],
                                              [compress_button, output_label]])

while True:
    event, values = window.read()
    try:
        filepaths = values['files'].split(';')
        folder = values['folder']
        make_archive(filepaths, folder)
        window['output'].update(value='Compression completed!')
    except AttributeError:
        break

window.close()