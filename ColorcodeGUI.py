import PySimpleGUI as sg
v=0
''' Selvavignesh contribution towards Electrocis. This is developed for educational purpose only '''
layout = [ [sg.Text("Color Coding of Resister", size=(60, 1), justification="center")],
           [sg.Text("Click colors from left to right of the Resistor:", size=(60, 1))],
           [sg.Button("Black",  button_color =("#ffffff", "#000000"), size =(15,3)),
           sg.Button("Brown",   button_color =("#ffffff", "#800000"), size =(15,3)), 
           sg.Button("Red",     button_color =("#ffffff", "#fc0000"), size =(15,3)),
           sg.Button("Orange",  button_color =("#ffffff", "#ff8000"), size =(15,3))],
           [sg.Button("Yellow", button_color =("#ffffff", "#fff900"), size =(15,3)),
           sg.Button("Green",   button_color =("#ffffff", "#00fa00"), size =(15,3)),
           sg.Button("Blue",    button_color =("#ffffff", "#0000ff"), size =(15,3)),
           sg.Button("Violet",  button_color =("#ffffff", "#8000ff"), size =(15,3))],
           [sg.Button("Gray",   button_color =("#ffffff", "#808080"), size =(15,3)),
           sg.Button("White",   button_color =("#f0f000", "#ffffff"), size =(15,3)),
           sg.Button("Gold",    button_color =("#ffffff", "#ffd700"), size =(15,3)),
           sg.Button("Silver",  button_color =("#ffffff", "#c0c0c0"), size =(15,3))],
           [sg.Button("No Color",button_color =("#ffffff", "#ff99cc"), size =(15,3))],
           [sg.Button("Exit",   button_color=("#000000","#00faff"), size= (500,1))],
           [sg.Text("https://github.com/selva-vignesh", size =(60,1),justification="right")]
         ]
window = sg.Window('ColorCode', layout, size= (575, 400))  
mul = ''
fst =''
scd =''
tolr = 0
def val(event):
        if event =="Black" :
            fst = scd = mul ='0'
            tolr = 0
        if event =="Brown" :
            fst = scd = mul ='1'
            tolr = 1
        
        if event =="Red" :
            fst = scd  = mul ='2'
            tolr = 2
            
        if event =="Orange" :
            fst = scd  = mul ='3'
            tolr = 0
        
        if event =="Yellow" :
            fst = scd  = mul ='4'
            tolr = 0
        
        if event =="Green" :
            fst = scd  = mul ='5'
            tolr = 0
        
        if event =="Blue" :
            fst = scd  = mul ='6'
            tolr = 0
        
        if event =="Violet" :
            fst = scd  = mul ='7'
            tolr = 0
            
        if event =="Grey" :
            fst = scd ='8'
            mul =1
            tolr = 0
            
        if event =="White" :
            fst = scd ='9'
            mul =1
            tolr = 0
        
        if event =="Gold" :
            fst = scd =0
            mul ='-1'
            tolr = 5
        
        if event =="Silver" :
            fst = scd =0
            mul =1
            tolr = 10
        
        if event =="No Color" :
            fst = scd =0
            mul =1
            tolr = 20

        return [fst,scd,mul,tolr]


j=0
try:
    while (1):
        value =''
        mult =1
        for i in range(4):
                event, values = window.read()
                if event == "Exit" or event == sg.WIN_CLOSED:
                        break   
                x = val(event)
                if i<2:
                    value =value+x[i]
                if i==2:
                    p = int(x[i])
                    mult = 10**(p)

                tolr = tolr +x[3]
        if event == "Exit" or event == sg.WIN_CLOSED:
                        break         

        value = [int(value), p,tolr]
        sg.popup("    The resistor value = {0} * 10^{1} Ohms (_+_ {2}%)     ".format(value[0],value[1],value[2]))
except:
    sg.popup("Error! Tolerance can't be the first/second value.")
    window.close()
window.close()