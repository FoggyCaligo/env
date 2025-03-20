import keyboard
import mouse







class Shortcut:
    def __init__(self):
        self.mode_flag = False
        
        self.shift = False
        self.alt = False
        self.ctrl = False
        
        # keyboard.press('space')
        #모드 변경    
        keyboard.add_hotkey('shift+space', lambda: self.changeMode(), suppress=True)

        #shift
        keyboard.on_press_key('shift', lambda _: True if self.shift==False else False)
        keyboard.on_release_key('shift', lambda _: True if self.shift==False else False)
        #alt
        keyboard.on_press_key('alt', lambda _: True if self.shift==False else False)
        keyboard.on_release_key('alt', lambda _: True if self.shift==False else False)
        #ctrl
        keyboard.on_press_key('ctrl', lambda _: True if self.shift==False else False)
        keyboard.on_release_key('ctrl', lambda _: True if self.shift==False else False)
        

        #방향키&마우스 모드
        # self.main()

        # #방향키 입력
        keyboard.add_hotkey('h',lambda:  self.arrowAlter('left'), suppress=True)
        keyboard.add_hotkey('j',lambda:  self.arrowAlter('down'), suppress=True)
        keyboard.add_hotkey('k',lambda:  self.arrowAlter('up'), suppress=True)
        keyboard.add_hotkey('l',lambda:  self.arrowAlter('right'), suppress=True)


        
        # # keyboard.add_hotkey('shift+H',lambda:  self.arrowAlter('shift+left'), suppress=True)
        # # keyboard.add_hotkey('shift+J',lambda:  self.arrowAlter('shift+up'), suppress=True)
        # # keyboard.add_hotkey('shift+k',lambda:  self.arrowAlter('shift+down'), suppress=True)
        # # keyboard.add_hotkey('shift+l',lambda:  self.arrowAlter('shift+right'), suppress=True)
        keyboard.add_hotkey('H',lambda:  self.arrowAlter('shift+left'), suppress=True)
        keyboard.add_hotkey('J',lambda:  self.arrowAlter('shift+up'), suppress=True)
        keyboard.add_hotkey('k',lambda:  self.arrowAlter('shift+down'), suppress=True)
        keyboard.add_hotkey('l',lambda:  self.arrowAlter('shift+right'), suppress=True)
        
        #마우스 움직임
        
    def changeMode(self):
        try:
            self.mode_flag= False if self.mode_flag==True else True
            print(self.mode_flag, "mode changed")
        except:
            print("change mod failed")
            pass



    
    def arrowAlter(self,dir):
        try:
            if(self.mode_flag==True): 
                keyboard.press(dir)
                print(dir)
        except:
            print("Arrow input failed")
            pass

    

    def pressKey(self,key):
        # for each in key:
        try:
            keyboard.press(key)
        except:
            print("pressing",key," failed")

        








Shortcut = Shortcut()
# 무한 루프를 돌면서 이벤트를 감지합니다.
keyboard.wait()