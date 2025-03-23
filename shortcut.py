import keyboard
import mouse
import pynput
import string

import pyautogui

'''
alt space -> mode change
<insert mode>
hjkl -> vim format 방향키

좌수 : 클릭 (a(마우스<-> 방향키. 기본:방향키) s가운데클릭 d 우클릭 f좌클릭(vimium이랑 중복조작 되지 않는지 확인 필요)   우수 :  조작  (hjkl)


'''






class Shortcut:
    def __init__(self):

        


        # keyboard.unhook_all_hotkeys()

        self.mode_flag = False 
        self.isMouse = False

        # self.mouse = Controller()
        self.mouse = pynput.mouse.Controller()
        self.shift = False
        self.alt = False
        self.ctrl = False

        self.scrollSpeed = 5 
        
        self.isSlow = True
        self.speedFast = 100
        self.speedSlow = 15
        self.speed = self.speedSlow

        self.keyboard_ctrl = pynput.keyboard.Controller()
        
        
        #조합키 상태
        self.shift = False
        self.alt = False
        self.ctrl = False
        self.space = False

        #입력키
        self.etc = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFJHIJKLMNOPQRSTUVWXYZ01234567890'        
        #모든 키
        self.cmds = 'hjkl ui w asdf HJKL'
        #방향키
        self.left = self.cmds[0]
        self.down = self.cmds[1] 
        self.up = self.cmds[2]
        self.right = self.cmds[3]
        #방향키 블록지정
        self.shiftleft = self.cmds[15]
        self.shiftdown = self.cmds[16]
        self.shiftup = self.cmds[17]
        self.shiftright = self.cmds[18]
        #페이지 업다운 
        self.pgDn = self.cmds[5]
        self.pgUp = self.cmds[6] 
        #가속
        self.mouseSlow = self.cmds[8]
        self.arrowSize = 5
        #마우스변경
        self.mouseChange = self.cmds[10]
        #마우스버튼
        self.mouseMiddle = self.cmds[11]
        self.mouseRight = self.cmds[12]
        self.mouseLeft = self.cmds[13]
        #마우스스크롤



        #키 입력 감지
        #모드 변경    
        # keyboard.add_hotkey('shift+space', lambda: self.changeMode(), suppress=True)
        #키 다운
        keyboard.on_press(self.alter_keys_press, suppress=True) 
        #키 업
        keyboard.on_release(self.alter_keys_release,suppress=True)

  


    
    #키 프레스
    def alter_keys_press(self,key):
        key = str(key).replace('KeyboardEvent(','').replace(' down)','')
        print(key)
        #조합키 입력 시
        if(key=='shift' or key=='right shift'):
            if(self.shift==False):
                keyboard.press('shift')
                keyboard.press('right shift')
                self.shift = True
              
        elif(key=='space'):
            if(self.shift==True):
                self.mode_flag = True if self.mode_flag==False else False
                print('mode ',self.mode_flag)
                return
            else: 
                keyboard.press('space')
                
        elif(key=='ctrl' or key=='right ctrl'):
            self.ctrl = True
            keyboard.press('ctrl')       
        elif(key=='alt'): 
            self.alt = True
            keyboard.press('alt')
 
        #모드 아니면 해당 키 입력 후 종료
        if(self.mode_flag == False):
            if(key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                cmd = 'shift'+'+'+key.lower() 
                print(cmd)
                keyboard.press(cmd)
            else:
                keyboard.press(key)

            return

        #모드 중인데 단축키 입력 시
        if(self.ctrl==True):
            if(key in "sewcvxzyga"):
                keyboard.press('ctrl+'+key)
                return

        #모드 중인데 매핑안된 키 입력 시
        if(key not in self.cmds and key in self.etc):
            # self.mode_flag = False
            # self.isMouse = False
            # print('mode ',self.mode_flag)
            print('key not mapped')
            return   
        if(key not in self.cmds):
            keyboard.press(key)
                        



        
        
        
        #가속 여부 : 가속
        if(key==self.mouseSlow):
            self.isSlow = False
            self.speed = self.speedFast
            return 
    
        #마우스<->방향키 입력 시
        if(key == self.mouseChange):
            self.isMouse = True if self.isMouse==False else False
            return
        #페이지 업다운 입력 시
        if(key==self.pgUp):
            keyboard.press('pgUp')
            return
        if(key==self.pgDn):
            keyboard.press('pgDown')
            return
        #마우스 버튼
        if(key==self.mouseLeft):
            self.mouse.press(pynput.mouse.Button.left)
        elif(key==self.mouseRight):
            self.mouse.press(pynput.mouse.Button.right)
        elif(key==self.mouseMiddle):
            self.mouse.press(pynput.mouse.Button.middle)
        #마우스 모드일때
        if(self.isMouse==True):
            #움직임
            if(key == self.left):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.x = mouse.get_position()[0]-speed
                self.y = mouse.get_position()[1]
                mouse.move(self.x,self.y, 0.5)
            elif(key==self.up):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.x = mouse.get_position()[0]
                self.y = mouse.get_position()[1]-speed
                mouse.move(self.x,self.y, 0.5)
            elif(key==self.down):
                
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.x = mouse.get_position()[0]
                self.y = mouse.get_position()[1]+speed
                mouse.move(self.x,self.y, 0.5)
            elif(key==self.right):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.x = mouse.get_position()[0]+speed
                self.y = mouse.get_position()[1]
                mouse.move(self.x,self.y, 0.5)
            #언맵드
        #방향키 모드일때 
        elif(self.isMouse==False):
            if(key == self.left):
                keyboard.press('left')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('left') 
                        print('left')
            elif(key==self.up):
                keyboard.press('up')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('up') 
                        print('up')
            elif(key==self.down):
                keyboard.press('down')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('down') 
                        print('down')
            elif(key==self.right):
                keyboard.press('right')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('right') 
                        print('right')
            #$블록지정
            elif(key==self.shiftleft):
                keyboard.press('shift+left')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+left') 
                        print('shiftleft')
                print('shiftleft')
            elif(key==self.shiftright):
                # keyboard.press('shift')
                keyboard.press('shift+right')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+right') 
                        print('shifright')
                print('shiftright')
            elif(key==self.shiftup):
                keyboard.press('shift+up')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+up') 
                        print('shiftup')
                print('shiftup')
            elif(key==self.shiftdown):
                keyboard.press('shift+down')
                # keyboard.press('down')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+down') 
                        print('shiftdown')
                print('shiftdown')
        





    #키 릴리즈
    def alter_keys_release(self,key):
        key = str(key).replace('KeyboardEvent(','').replace(' up)','')
        # print(key)s
        #조합키
        if(key=='space'): 
            keyboard.release('space')
        if(key=='shift' or key=='right shift'):
            keyboard.release('shift')
            keyboard.release('right shift')
            self.shift = False
        if(key=='ctrl' or key=='right ctrl'):
            keyboard.release('ctrl')
            self.ctrl = False
        if(key=='alt'):
            keyboard.release('alt')
            self.alt = False
        #모드 아니면 해당 키 릴리즈 후 종료
        if(self.mode_flag == False):
            keyboard.release(key) 
            return
        #가속 여부 : 감속
        if(key==self.mouseSlow):
            self.isSlow = True
            self.speed = self.speedSlow
            return
        #마우스 버튼
        if(self.isMouse):
            if(key==self.mouseLeft):
                self.mouse.release(pynput.mouse.Button.left)
            elif(key==self.mouseRight):
                self.mouse.release(pynput.mouse.Button.right)
            elif(key==self.mouseMiddle):
                self.mouse.release(pynput.mouse.Button.middle)
        #매핑된 키면
        elif(key in self.cmds):
            keyboard.release(key)



    #모드 변경 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ   s
    def changeMode(self):
        try:
            if(self.mode_flag==True):
                self.mode_flag=False
                self.isMouse = False
                print("keyboard mode ")
            else:
                self.mode_flag=True
                self.isMouse = False
                print("custom mode")
        except:
            print("change mod failed")
            # shortcut.__del__()
            # shortcut = Shortcut()
            keyboard.wait()

       
    
    def __del__(self):
        keyboard.unhook_all()
        keyboard.unhook_all_hotkeys()
        # keyboard.unhook_all_word_listeners()
        mouse.unhook_all()
        

        return






Shortcut = Shortcut()
# 무한 루프를 돌면서 이벤트를 감지합니다.
keyboard.wait()