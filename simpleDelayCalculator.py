import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

ms=60000;

#notes to calculate
notes = {
    "Four whole notes":16,
    "Three whole notes":12,
    "Two whole notes":8,
    "One whole notes":4,
    "Half Note":2,
    "Quarter Note":1,
    "eighth note":0.5,
    "16th Note":0.25,
    "32th Note":0.125,
    "64th Note":0.0625
}
layout = [[sg.Text('Beats per Minute (BPM)', size=(18, 1)),sg.Text('Note value of delay', size=(20, 1)),sg.Text('Delay time (milliseconds)', size=(20, 1))],
          [sg.Input([],size=(20, 3), key='_bpm_'),sg.InputCombo(['','Four whole notes', 'Three whole notes', 'Two whole notes', 'One whole notes', 'Half Note', 'Quarter Note', 'eighth note', '16th Note', '32th Note', '64th Note'], size=(20, 3), key='_note_'), sg.Input([],size=(20, 3), key='_delay_',text_color='black')],
          [sg.RButton('Calculate Delay Time'), sg.Exit()]]

window = sg.Window('BPM Delay Time Calculator', layout)

while True:      
    event, values = window.Read()

    if event is None or event == 'Exit':
        break

    try:
        window.Element('_delay_').Update(value =(ms/int(values['_bpm_']))*notes[values['_note_']])
    except ValueError: 
        window.Element('_delay_').Update(value ='Please Only Integer')
    except:
        window.Element('_delay_').Update(value ='Please Select a Note')
        
window.Close()
