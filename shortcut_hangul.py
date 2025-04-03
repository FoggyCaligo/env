import keyboard
import mouse
import pynput
# import string

# from jamo import j2h

import os
import pyautogui

'''
alt space -> mode change
<insert mode>
hjkl -> vim format 방향키

좌수 : 클릭 (a(마우스<-> 방향키. 기본:방향키) s가운데클릭 d 우클릭 f좌클릭(vimium이랑 중복조작 되지 않는지 확인 필요)   우수 :  조작  (hjkl)


'''






class Shortcut:
    def __init__(self):

        self.eng_to_jamo = {
            'r': 'ㄱ', 'R': 'ㄲ', 's': 'ㄴ', 'e': 'ㄷ', 'E': 'ㄸ', 'f': 'ㄹ',
            'a': 'ㅁ', 'q': 'ㅂ', 'Q': 'ㅃ', 't': 'ㅅ', 'T': 'ㅆ', 'd': 'ㅇ',
            'w': 'ㅈ', 'W': 'ㅉ', 'c': 'ㅊ', 'z': 'ㅋ', 'x': 'ㅌ', 'v': 'ㅍ', 'g': 'ㅎ',
            'k': 'ㅏ', 'o': 'ㅐ', 'i': 'ㅑ', 'O': 'ㅒ', 'j': 'ㅓ', 'p': 'ㅔ',
            'u': 'ㅕ', 'P': 'ㅖ', 'h': 'ㅗ', 'y': 'ㅛ', 'n': 'ㅜ', 'b': 'ㅠ',
            'm': 'ㅡ', 'l': 'ㅣ'
        }
        self.buffer = []

        self.hangul = False

        # keyboard.unhook_all_hotkeys()
    
        self.mode_flag = False 
        self.isMouse = False

        self.mouse = pynput.mouse.Controller()
        # self.mouse.release(pynput.mouse.Button.left)
        # self.mouse.release(pynput.mouse.Button.right)
        # self.mouse.release(pynput.mouse.Button.middle)
        self.shift = False
        self.alt = False
        self.ctrl = False

        self.scrollSpeed = 5 
        
        self.isSlow = True
        self.speedFast = 50
        self.speedSlow = 15
        self.speed = self.speedSlow

        self.keyboard_ctrl = pynput.keyboard.Controller()
        
        
        #조합키 상태
        self.shift = False
        self.alt = False
        self.ctrl = False
        self.space = False

        #입력키
        self.etc = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFJHIJKLMNOPQRSTUVWXYZ01234567890/'        
        #모든 키
        self.cmds = 'jkil uo w asdf JKIL'
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


        print('ctrl',keyboard.is_pressed('ctrl'),'shift',keyboard.is_pressed('shift'),'alt',keyboard.is_pressed('alt')) 


        #shift 입력 시
        if(key=='shift' or key=='right shift'):
            if(self.shift==False):
                keyboard.press('shift')
                keyboard.press('right shift')
                self.shift = True
        #모드 변경시 (shift + space)
        elif(key=='space'):
            if(self.shift==True):
                self.mode_flag = True if self.mode_flag==False else False
                keyboard.release('shift')
                keyboard.release('right shift')
                self.shift = False
                self.isMouse = False
                # self.mouse.release(pynput.mouse.Button.left)
                # self.mouse.release(pynput.mouse.Button.right)
                # self.mouse.release(pynput.mouse.Button.middle)

                print('mode ',self.mode_flag)
                return
        #ctrl 
        elif(key=='ctrl'):
            self.ctrl = True
            keyboard.press('ctrl')     
        elif(key=='right ctrl'):
            self.ctrl = True
            keyboard.press('right ctrl')  
        #alt
        elif(key=='alt'): 
            self.alt = True
            keyboard.press('alt')
        elif(key=='right alt'):
            # self.alt=True
            self.hangul = True if self.hangul==False else False
            print('hangul : ',self.hangul)
            # keyboard.press('shift+alt')
            # keyboard.press_and_release('shift+alt')
        #모드 아니면 해당 키 입력 후 종료
        if(self.mode_flag == False):
            #대문자
            if(key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                cmd = 'shift'+'+'+key.lower() 
                # print(cmd)
                keyboard.press(cmd)
            #그 외
            elif key in string.ascii_lowercase:
                keyboard.press(key)
            elif self.hangul==True:
                self.write_hangul(key)
            else:
                keyboard.press(key)

            return
        


        if self.shift==True and key=='tab':
            keyboard.release('shift')
            keyboard.release('right shift')
            keyboard.release('ctrl')
            keyboard.release('right ctrl')
            keyboard.release('alt')
            # self.mouse.release(pynput.mouse.Button.left)
            # self.mouse.release(pynput.mouse.Button.middle)

            self.__del__()
            os._exit(0) 
        #모드 중인데 단축키 입력 시
        if self.ctrl==True : 
            if(key in "fsewcvxzygam/"):
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
            # print('mouse left')
            self.mouse.press(pynput.mouse.Button.left)
            # mouse.key_down(pynput.mouse.Button.left)
            # keyboard.press('left')
            # keyboard.press('mouse left')
            # keyboard.press('mouse left')
            # mouse.press('left')
        elif(key==self.mouseRight):
            self.mouse.press(pynput.mouse.Button.right)
            # mouse.press('right')
        elif(key==self.mouseMiddle):
            self.mouse.press(pynput.mouse.Button.middle)
            # mouse.press('middle')
        #마우스 모드일때
        if(self.isMouse==True):
            #움직임
            if(key == self.left):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                # self.x = mouse.get_position()[0]-speed
                # self.y = mouse.get_position()[1]
                # mouse.move(self.x,self.y, 0.5)
                self.mouse.move(-speed,0)
            elif(key==self.up):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                # self.x = mouse.get_position()[0]
                # self.y = mouse.get_position()[1]-speed
                # mouse.move(self.x,self.y, 0.5)
                self.mouse.move(0,-speed)

            elif(key==self.down):
                
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                # self.x = mouse.get_position()[0]
                # self.y = mouse.get_position()[1]+speed
                # mouse.move(self.x,self.y, 0.5)
                self.mouse.move(0,speed)
            elif(key==self.right):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                # self.x = mouse.get_position()[0]+speed
                # self.y = mouse.get_position()[1]
                # mouse.move(self.x,self.y, 0.5)
                self.mouse.move(speed,0)
            #언맵드
        #방향키 모드일때 
        elif(self.isMouse==False):
            if(key == self.left):
                keyboard.press('left')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('left') 
                        # print('left')
            elif(key==self.up):
                keyboard.press('up')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('up') 
                        # print('up')
            elif(key==self.down):
                keyboard.press('down')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('down') 
                        # print('down')
            elif(key==self.right):
                keyboard.press('right')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('right') 
                        # print('right')
            #$블록지정
            elif(key==self.shiftleft):
                keyboard.press('shift+left')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+left') 
                        # print('shiftleft')
                print('shiftleft')
            elif(key==self.shiftright):
                # keyboard.press('shift')
                keyboard.press('shift+right')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+right') 
                        # print('shifright')
                # print('shiftright')
            elif(key==self.shiftup):
                keyboard.press('shift+up')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+up') 
                        # print('shiftup')
                # print('shiftup')
            elif(key==self.shiftdown):
                keyboard.press('shift+down')
                # keyboard.press('down')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('shift+down') 
                        # print('shiftdown')
                # print('shiftdown')
        
        print('ctrl',keyboard.is_pressed('ctrl'),'shift',keyboard.is_pressed('shift'),'alt',keyboard.is_pressed('alt')) 

        





    #키 릴리즈
    def alter_keys_release(self,key):
        key = str(key).replace('KeyboardEvent(','').replace(' up)','')
        #조합키
        if(key=='space'): 
            keyboard.release('space')
        if(key=='shift' or key=='right shift'):
            keyboard.release('shift')
            keyboard.release('right shift')
            self.shift = False
        if(key=='ctrl'):
            keyboard.release('ctrl')
            self.ctrl = False
        if(key=='right ctrl'):
            keyboard.release('right ctrl')
            self.ctrl = False
        if(key=='alt'):
            keyboard.release('alt')
            self.alt = False
        # if(key=='right alt'):
            # self.hangul = False
            # print('en')
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
                # mouse.release('left')
            elif(key==self.mouseRight):
                self.mouse.release(pynput.mouse.Button.right)
                # mouse.release('right')
            elif(key==self.mouseMiddle):
                # mouse.release('middle')
                self.mouse.release(pynput.mouse.Button.middle)
        #매핑된 키면
        elif(key in self.cmds):
            keyboard.release(key)



    
    def __del__(self):
        # keyboard.unhook_all()
        # keyboard.unhook_all_hotkeys()
        # mouse.unhook_all()
        keyboard.release('shift')
        keyboard.release('right shift')
        keyboard.release('ctrl')
        keyboard.release('right ctrl')
        keyboard.release('alt')
        keyboard.release('right alt')
        keyboard.release('space')
        
        self.mouse.release(pynput.mouse.Button.left)
        self.mouse.release(pynput.mouse.Button.right)
        self.mouse.release(pynput.mouse.Button.middle)
        
        mouse.release(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.right)
        mouse.release(pynput.mouse.Button.middle)


        return
    

    def write_hangul(self,key):
        if key in self.eng_to_jamo:
            # self.keyboard_ctrl.press(self.eng_to_jamo[key])
            # self.keyboard_ctrl.release(self.eng_to_jamo[key])
            keyboard.write(self.eng_to_jamo[key])





Shortcut = Shortcut()
# 무한 루프를 돌면서 이벤트를 감지합니다.
# keyboard.wait()
keyboard.wait()