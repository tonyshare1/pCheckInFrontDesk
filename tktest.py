import Tkinter as tk


dctUI = {}

def cmdBtnLogin ():
    print "login"
    dctUI['DbgText'].insert('end', 'login')

    #Take GoogleSheedID to login
    #Then Output to LoginStatus


def cmdBtnIdSearch ():
    print "Search"
    dctUI['DbgText'].insert('end', 'login')

    #TK:Read in IdEntry
    #GSheet: Search Id Entry, identify in which row
    #GSheet: Read Row
    #TK:        Display on NameOutput, CheckInTime, CheckInOutput

def cmdBtnCheckIn ():
    print "CheckIn"
    dctUI['DbgText'].insert('end', 'login')

    #GSheet: update grid
    #Do search again, for update


'''------------------------------------UI component-------------------------------'''
lst = [ 
        [#Row1 
            { "name": "Check-in System",
              "type": "Label",
              "text": ""      #not required for Label
            } 
        ] , 
        [#Row2
            { "name": "GoogleSheetID",
              "type": "Label",
              "text": ""      #not required for Label
            }, 
            { "name": "GoogleSheetIdInput",
              "type": "Entry",
              "text": "SheetID-text-Default"      #not required for Label
            }, 
            { "name": "Login",
              "type": "Button",
              "text": "Label1-text",
              "action": cmdBtnLogin
            } 
        ] , 
        [#Row3
            { "name": "LoginStatus",
              "type": "Label",
              "text": ""
            } ,
            { "name": "LoginOutput",
              "type": "Entry",
              "text": ""      #not required for Label
            }, 
        ],
        [#Row4
            { "name": "IdInput",
              "type": "Label",
              "text": "Search-Using-ID"
            }, 
            { "name": "IdEntry",
              "type": "Entry",
              "text": ""
            }, 
            { "name": "IdSearch",
              "type": "Button",
              "text": "Label1-text",
              "action": cmdBtnIdSearch
            } 
        ] , 
        [#Row5
            { "name": "Name",
              "type": "Label",
              "text": "Label1-text"
            } ,
            { "name": "NameOutput",
              "type": "Entry",
              "text": ""
            }, 
        ] , 
        [#Row6 
            { "name": "CheckIn?",
              "type": "Label",
              "text": "Label1-text"
            }, 
            { "name": "CheckInOutput",
              "type": "Entry",
              "text": ""
            }, 
        ] , 
        [#Row7 
            { "name": "CheckedInTime:",
              "type": "Label",
              "text": "Label1-text"
            }, 
            { "name": "CheckInTime",
              "type": "Entry",
              "text": ""
            }, 
            { "name": "CheckIn",
              "type": "Button",
              "text": "Label1-text",
              "action": cmdBtnCheckIn
            } 
        ] , 
        [#Row8
            { "name": "DbgText",
              "type": "Entry",
              "text": ""
            }, 
        ] , 
    ]
'''        [ 
            {   "name" : "test2",
                "type": "Label"
            }, 
            {   "name" : "test3",
                "type": "Button"} 
            ] 
        ]'''
def mCreateComponent( oTk, lComponent , rw=0, cl=0):
    print "Start creating GUI component"
    
    for entry in lst:
        for dct in entry: 
            print "Start Adding Things"
            
            if dct['type'] == 'Label':
                item = tk.Label( oTk, text = dct['name'])
            elif dct['type'] == 'Button':
                if 'action' in dct:
                    cmd = dct['action']
                else:
                    cmd = ""
                #print cmd
                item = tk.Button( oTk, text = dct['name'], command = cmd)
            elif dct['type'] == 'Entry':
                if 'text' in dct:
                    strVar = tk.StringVar(oTk, value=dct['text'])
                else:
                    strVar = tk.StringVar(oTk, value='')

                item = tk.Entry( oTk, text = dct['name'], textvariable = strVar)
                print dct['text']
            else:
                print "error"
                print dct
                exit(1)
            #Assign common parameter here, things like 
            #width, hight
            item.grid(row = rw, column = cl)
            if 'action' in dct :
                #item.command = dct['action'] 
                #print "add command"
                pass
            #Register to dictionary-UI for future use
            dctUI[ dct['name'] ] = item

            cl = cl+1

        rw = rw+1
        cl = 0



root = tk.Tk()

root.title("TITLE bar")

mCreateComponent( root, lst )

root.mainloop()
