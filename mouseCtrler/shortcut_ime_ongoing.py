import keyboard
import mouse
import pynput

import os
import hgtk

import pyautogui

'''
alt space -> mode change
<insert mode>
hjkl -> vim format 방향키

좌수 : 클릭 (a(마우스<-> 방향키. 기본:방향키) s가운데클릭 d 우클릭 f좌클릭(vimium이랑 중복조작 되지 않는지 확인 필요)   우수 :  조작  (hjkl)
'''

class Shortcut:
    def __init__(self):

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
        self.cmds = 'jkil ou w asdf JKIL'
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
        #키 다운
        keyboard.on_press(self.alter_keys_press, suppress=True) 
        #키 업
        keyboard.on_release(self.alter_keys_release,suppress=True)
    
    #키 프레스
    def alter_keys_press(self,key):
        key = str(key).replace('KeyboardEvent(','').replace(' down)','')
        print(key)

        #shift 입력 시
        if(key=='shift' or key=='right shift'):
            if(self.shift==False):
                keyboard.press('shift')
                keyboard.press('right shift')
                self.shift = True
        #모드 변경시 (shift + space)
        elif(key=='space'):
            if(self.shift==True):
            # if(keyboard.is_pressed('shift')  ):    
                self.mode_flag = True if self.mode_flag==False else False
                self.shift = False
                self.isMouse = False
                print('mode ',self.mode_flag)
                return
        #ctrl 
        elif(key=='ctrl' or key=='right ctrl'):
            self.ctrl = True
            keyboard.press('ctrl')       
        #alt
        elif(key=='alt'): 
            self.alt = True
            keyboard.press('alt')
        elif(key=='right alt'):
            keyboard.send('right alt')
            return
        
        if self.shift==True and key=='tab':
            self.__del__()
            os._exit(0) 
            return
        #단축키 입력 시
        if self.ctrl==True : 
            if(key in "fsewcvxzygamb/"):
                keyboard.press('ctrl+'+key)
                return  

        #모드 아니면 해당 키 입력 후 종료
        if(self.mode_flag == False):
            #대문자
            if(key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                keyboard.press('shift')
                keyboard.press('right shift')
                keyboard.press(key.lower())
            else:
                keyboard.press(key)
            return

        #모드 중인데 매핑안된 키 입력 시
        if(key not in self.cmds and key in self.etc):
            print('key not mapped')
            return   
        if(key not in self.cmds):
            keyboard.press(key)
            return
        
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
            return
        elif(key==self.mouseRight):
            self.mouse.press(pynput.mouse.Button.right)
            return
            # mouse.press('right')
        elif(key==self.mouseMiddle):
            self.mouse.press(pynput.mouse.Button.middle)
            return# mouse.press('middle')
        #마우스 모드일때
        if(self.isMouse==True):
            #움직임
            if(key == self.left):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.mouse.move(-speed,0)
            elif(key==self.up):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.mouse.move(0,-speed)
            elif(key==self.down):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.mouse.move(0,speed)
            elif(key==self.right):
                speed = self.speedSlow
                if(self.isSlow==False):
                    speed = self.speedFast
                self.mouse.move(speed,0)
            #언맵드
        #방향키 모드일때 
        elif(self.isMouse==False):
            if(key == self.left or key==self.shiftleft):
                keyboard.press('left')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('left') 
                        # print('left')
            elif(key==self.up or key==self.shiftup):
                keyboard.press('up')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('up') 
                        # print('up')
            elif(key==self.down or key==self.shiftdown):
                keyboard.press('down')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('down') 
                        # print('down')
            elif(key==self.right or key==self.shiftright):
                keyboard.press('right')
                if(self.isSlow==False):
                    for each in range(self.arrowSize):
                        keyboard.press('right') 
                        # print('right')

    #키 릴리즈
    def alter_keys_release(self,key):
        key = str(key).replace('KeyboardEvent(','').replace(' up)','')
        #조합키
        if(key=='space'): 
            keyboard.release('space')
            return
        if(key=='shift' or key=='right shift'):
            keyboard.release('shift')
            keyboard.release('right shift')
            self.shift = False
            return
        if(key=='ctrl' or key=='right ctrl'):
            keyboard.release('ctrl')
            self.ctrl = False
            return
        if(key=='alt'):
            keyboard.release('alt')
            self.alt = False
            return
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
        keyboard.release('shift')
        keyboard.release('right shift')
        keyboard.release('ctrl')
        # keyboard.release('right ctrl')
        keyboard.release('alt')
        keyboard.release('space')
        
        self.mouse.release(pynput.mouse.Button.left)
        self.mouse.release(pynput.mouse.Button.right)
        self.mouse.release(pynput.mouse.Button.middle)
        
        mouse.release(pynput.mouse.Button.left)
        mouse.release(pynput.mouse.Button.right)
        mouse.release(pynput.mouse.Button.middle)
        return


Shortcut = Shortcut()
# 무한 루프를 돌면서 이벤트를 감지합니다.
# keyboard.wait()
keyboard.wait()