import keyboard
import mouse

# import pynput
from pynput.mouse import Button, Controller

# from pynput.mouse import Button, Controller

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

        self.mouse = Controller()
        self.shift = False
        self.alt = False
        self.ctrl = False

        # self.x = mouse.get_position()[0]
        # self.y = mouse.get_position()[1]
        # self.y = 10
        self.scrollSpeed = 5
        
        self.isSlow = True
        self.speedFast = 70
        self.speedSlow = 15
        self.speed = self.speedSlow

        
        #키
        self.arrowSize = 5
        keyOrderArrow = "hjkl"
        self.left = keyOrderArrow[0]
        self.down =   keyOrderArrow[1]
        self.up = keyOrderArrow[2]
        self.right = keyOrderArrow[3]
        keyOrderPg = "ui"
        self.pgUp = keyOrderPg[0]
        self.pgDn = keyOrderPg[1]
        keyOrderMouse = "asdf"
        self.mouseChange = keyOrderMouse[0]
        self.mouseMiddle = keyOrderMouse[1]
        self.mouseRight = keyOrderMouse[2]
        self.mouseLeft = keyOrderMouse[3]
        
        self.mouseSlow = 'w'



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
        # keyboard.add_hotkey(self.left,lambda:  self.arrowAlter(arrow='left', key=self.left), suppress=True)
        # keyboard.add_hotkey(self.down,lambda:  self.arrowAlter(arrow='down',key=self.down), suppress=True)
        # keyboard.add_hotkey(self.up,lambda:  self.arrowAlter(arrow='up',key=self.up), suppress=True)
        # keyboard.add_hotkey(self.right,lambda:  self.arrowAlter(arrow='right',key=self.right), suppress=True)
        
        keyboard.on_press_key(self.left,lambda e:  self.arrowAlter(arrow='left', key=self.left), suppress=True)
        keyboard.on_press_key(self.down,lambda e:  self.arrowAlter(arrow='down',key=self.down), suppress=True)
        keyboard.on_press_key(self.up,lambda e:  self.arrowAlter(arrow='up',key=self.up), suppress=True)
        keyboard.on_press_key(self.right,lambda e:  self.arrowAlter(arrow='right',key=self.right), suppress=True)
         
         
        #페이지 스크클
        keyboard.add_hotkey(self.pgUp,lambda:  self.mouseScroll(mouse='pgUp',key=self.pgUp), suppress=True)
        keyboard.add_hotkey(self.pgDn,lambda:  self.mouseScroll(mouse='pgDown',key=self.pgDn), suppress=True)
        #마우스<->방향키 변경
        keyboard.add_hotkey(self.mouseChange,lambda: self.changeMouse(self.mouseChange), suppress=True)
        #마우스 속도 조절
        keyboard.on_press_key(self.mouseSlow, lambda e:  self.toggleSpeed('fast'), suppress=True)
        keyboard.on_release_key(self.mouseSlow, lambda e: self.toggleSpeed('slow'), suppress=True);
        #마우스 누르기
        keyboard.on_press_key(self.mouseLeft, lambda e: self.mousePress(mouse='left', key=self.mouseLeft), suppress=True)
        keyboard.on_press_key(self.mouseRight, lambda e:  self.mousePress(mouse='right', key=self.mouseRight), suppress=True)
        keyboard.on_press_key(self.mouseMiddle, lambda e: self.mousePress(mouse='middle', key=self.mouseMiddle), suppress=True)
        #마우스 떼기
        keyboard.on_release_key(self.mouseLeft, lambda e:  self.mouseRelease(mouse='left', key=self.mouseLeft), suppress=True)
        keyboard.on_release_key(self.mouseRight, lambda e: self.mouseRelease(mouse='right', key=self.mouseRight), suppress=True)
        keyboard.on_release_key(self.mouseMiddle, lambda e: self.mouseRelease(mouse='middle', key=self.mouseMiddle), suppress=True)






        # keyboard.on_press_key('shift', lambda _: True if self.shift==False else False)
        

        # keyboard.KEY_DOWN('h',lambda:  self.pressKey('shift'), suppress=True)

        
        # # keyboard.add_hotkey('shift+H',lambda:  self.arrowAlter('shift+left'), suppress=True)
        # # keyboard.add_hotkey('shift+J',lambda:  self.arrowAlter('shift+up'), suppress=True)
        # # keyboard.add_hotkey('shift+k',lambda:  self.arrowAlter('shift+down'), suppress=True)
        # # keyboard.add_hotkey('shift+l',lambda:  self.arrowAlter('shift+right'), suppress=True)
        
    #모드 변경 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ   
    def changeMode(self):
        try:
            if(self.mode_flag==True):
                self.mode_flag=False
                self.isMouse = False
                print("keyboard mode ")
            else:
                self.mode_flag=True
                # self.isMouse = False
                print("custom mode")
        except:
            print("change mod failed")
            
    
    #마우스<->방향키 변경
    def changeMouse(self,key):
        try:
            if(self.mode_flag==True):
                # afdsfdsaself.isMouse = not self.isMouse
                
                
                if(self.isMouse==True):
                    self.isMouse=False
                    print("changed 2 arrow")
                elif(self.isMouse==False):
                    self.isMouse=True
                    print("changed 2 mouse")    
            else:
                keyboard.press(key)        
        except:
            print("change mouse failed")
            keyboard.wait()
            
        
#방향키ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    #방향키 입력
    def arrowAlter(self,arrow,key):
        try:
            if(self.mode_flag==True): 
                if(self.isMouse==True):
                    # mouse.move (mougghsex,mousey)
                    if(arrow=='up'):
                        # mouse.move(0,self.speed,0.5)
                        self.x = mouse.get_position()[0]
                        self.y = mouse.get_position()[1]-self.speed
                        mouse.move(self.x,self.y, 0.5)
                        # self.mouse.move(0,self.speed,0.5)
                        return
                    elif(arrow=='down'):
                        self.x = mouse.get_position()[0]
                        self.y = mouse.get_position()[1]+self.speed
                        mouse.move(self.x,self.y, 0.5)
                        # self.mouse.move(0,-self.speed,0.5)
                        # mouse.move(0,-self.speed,0.5)
                        # mouse.move(self.x,self.y+self.speed, 0.5)
                        return
                    elif(arrow=='left'):
                        # mouse.move(-self.speed,0,0.5)
                        self.x = mouse.get_position()[0]-self.speed
                        self.y = mouse.get_position()[1]
                        mouse.move(self.x,self.y, 0.5)
                        # self.mouse.move(-self.speed,0,0.5)
                        # mouse.move(self.x-self.speed,self.y, 0.5)
                        return
                    elif(arrow=='right'):
                        # mouse.move(self.speed,0,0.5)
                        self.x = mouse.get_position()[0]+self.speed
                        self.y = mouse.get_position()[1]
                        mouse.move(self.x,self.y, 0.5)
                        # self.mouse.move(self.speed,0,0.5)
                        # mouse.move(self.x+self.speed,self.y, 0.5)
                        return
                    elif(key=='pgUp'):
                        keyboard.press('pgUp')
                        return
                    elif(key=='pgDown'):
                        keyboard.press('pgDown')
                        return
                    else:
                        print("unexpected input : ",key,arrow,self.isMouse)
                        return;
                    
                else:
                    # if(pos=='down'):
                    #     keyboard.press(arrow)
                    # elif(pos=='up'):
                    #     keyboard.release(arrow)

                    keyboard.press(arrow)
                    print(arrow)
                    return
            else:
                    keyboard.press(key)
                    return
        except:
            print("Arrow input failed")
            keyboard.wait()
            return


#마우스ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    def toggleSpeed(self,speed):
        if(self.mode_flag==False):
            keyboard.press(speed)
            return;
        else:
            if(speed=='fast'):
                self.speed = self.speedFast
                return
            elif(speed=='slow'):
                self.speed = self.speedSlow
                return
            else:
                self.speed = self.speedSlow
                return
        


        # if(self.isSlow==False):
        #     self.scrollSpeed = self.scrollSpeedFast
        #     self.isSlow = True
        #     print("slow mode")
        # else:
        #     self.scrollSpeed = self.scrollSpeedSlow
        #     self.isSlow = False
        #     print("fast mode")
        # return
    
        
    #좌수 입력
    def mousePress(self,mouse,key):
        try:
            if(self.mode_flag==True):
                if(mouse=='left'):
                    self.mouse.press(Button.left)
                    return
                elif(mouse=='right'):
                    self.mouse.press(Button.right)
                    return
                elif(mouse=='middle'):
                    self.mouse.press(Button.middle)
                    return
                else:
                    print("unexpected input : ",key,self.isMouse)
            else:
                keyboard.press(key)
        except:
            print("Mouse input failed")
            keyboard.wait()
            return
    #좌수 떼기
    def mouseRelease(self,mouse,key):
        try:
            if(self.mode_flag==True):
                if(mouse=='left'):
                    self.mouse.release(Button.left)
                    return
                elif(mouse=='right'):
                    self.mouse.release(Button.right)
                    return
                elif(mouse=='middle'):
                    self.mouse.release(Button.middle)
                    return
                else:
                    print("unexpected input : ",key,self.isMouse)
            # else:
                # keyboard.press(key)
        except:
            print("Mouse input failed")
            keyboard.wait()
            return
        
    def mouseScroll(self,mouse,key):
        try:
            if(self.mode_flag==True):
                if(mouse=='pgUp'):
                    self.mouse.scroll(0,self.scrollSpeed)
                    return
                elif(mouse=='pgDown'):
                    self.mouse.scroll(0,-self.scrollSpeed)
                    return
                else:
                    print("unexpected input : ",key,self.isMouse)
            else:
                keyboard.press(key)
        except:
            print("Mouse input failed")
            keyboard.wait()
            return    



    def mouseAlter(self,mouse,key):
        try:
            if(self.mode_flag==True):
                # mouse.click(mouse)
                if(mouse=='left'):
                    # mouse.click(button='left')
                    self.mouse.click(Button.left)
                    return
                elif(mouse=='right'):
                    mouse.click(button='right')
                    return
                elif(mouse=='middle'):
                    mouse.click(button='middle')
                    return
                elif(mouse=='pgUp'):
                    mouse.scroll(0,10)
                    return
                elif(mouse=='pgDown'):
                    mouse.scroll(0,-10)
                else:
                    print("unexpected input : ",key,mouse,self.isMouse)
                    return
            else:
                keyboard.press(key)
                return
        except:
            print("Mouse input failed")
            keyboard.wait()
                








                
    def __del__(self):
        # keyboard.unhook_all()
        keyboard.unhook_all_hotkeys()
        keyboard.unhook_all_word_listeners()
        mouse.unhook_all()

        return






Shortcut = Shortcut()
# 무한 루프를 돌면서 이벤트를 감지합니다.
keyboard.wait()