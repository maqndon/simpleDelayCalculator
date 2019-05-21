import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

#data from
#http://www.sengpielaudio.com/calculator-bpmtempotime.htm
# 60,000 ms (1 minute) / Tempo (BPM) = Delay Time in ms for quarter-note beats

#60,000 / 120 BPM = 500 ms
#60,000 / 750 ms = 80 BPM
#60,000 / 96 BPM = 625 ms
#60,000 / 833.333 ms = 72 BPM

#Calculation of the delay timet for a quarter note (crotchet) at the tempo b in bpm.
#t = 1 / b. Therefore: 1 min / 96 = 60,000 ms / 96 = 625 ms.
#
#1/4 = quarter-note echo
#1/8 = eighth-note echo
#1/8T = eighth-note triplet echo
#1/16 = sixteenth-note echo
#Example: Song tempo is 120 BPM.
#Set delay time to 250 for eighth note echo.
#Conversion Tempo to Beats per minute • Delay values to the nearest millisecond.

ms=60000;

print = sg.Print

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

def notesCombo():
    for note in notes:
        return (note)

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