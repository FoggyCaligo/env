from pynput import keyboard, mouse
import os

class Shortcut:
    def __init__(self):
        self.mode_flag = False
        self.isMouse = False
        self.isSlow = True
        self.speedSlow = 15
        self.speedFast = 50
        self.speed = self.speedSlow
        self.arrowSize = 5

        self.mouse = mouse.Controller()
        self.keyboard = keyboard.Controller()
        self.pressed_keys = set()

        self.cmds = 'jkil ou w asdf JKIL'
        self.left = self.cmds[0]
        self.down = self.cmds[1]
        self.up = self.cmds[2]
        self.right = self.cmds[3]
        self.pgDn = self.cmds[5]
        self.pgUp = self.cmds[6]
        self.mouseSlow = self.cmds[8]
        self.mouseChange = self.cmds[10]
        self.mouseMiddle = self.cmds[11]
        self.mouseRight = self.cmds[12]
        self.mouseLeft = self.cmds[13]
        self.shiftleft = self.cmds[15]
        self.shiftdown = self.cmds[16]
        self.shiftup = self.cmds[17]
        self.shiftright = self.cmds[18]

        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        self.pressed_keys.add(key)

        # Shift + Space → 모드 전환
        if key == keyboard.Key.space and (
            keyboard.Key.shift in self.pressed_keys or keyboard.Key.shift_r in self.pressed_keys
        ):
            self.mode_flag = not self.mode_flag
            self.isMouse = False
            print("\n🔁 모드 전환됨:", "🖱 마우스 모드" if self.isMouse else "🧭 방향키 모드")
            return

        # Shift + Tab → 종료
        if keyboard.Key.shift in self.pressed_keys and key == keyboard.Key.tab:
            print("⛔ 종료 단축키 입력됨")
            os._exit(0)

        # 일반 모드에서는 아무것도 하지 않음
        if not self.mode_flag:
            return

        try:
            k = key.char.lower()
        except AttributeError:
            return

        if k == self.mouseSlow:
            self.isSlow = False
            self.speed = self.speedFast
            return
        elif k == self.mouseChange:
            self.isMouse = not self.isMouse
            print("🖱 마우스 조작 모드" if self.isMouse else "🧭 방향키 모드")
            return
        elif k == self.pgUp:
            self.keyboard.press(keyboard.Key.page_up)
        elif k == self.pgDn:
            self.keyboard.press(keyboard.Key.page_down)
        elif k == self.mouseLeft:
            self.mouse.press(mouse.Button.left)
        elif k == self.mouseRight:
            self.mouse.press(mouse.Button.right)
        elif k == self.mouseMiddle:
            self.mouse.press(mouse.Button.middle)
        elif self.isMouse:
            move = self.speedFast if not self.isSlow else self.speedSlow
            if k == self.left:
                self.mouse.move(-move, 0)
            elif k == self.right:
                self.mouse.move(move, 0)
            elif k == self.up:
                self.mouse.move(0, -move)
            elif k == self.down:
                self.mouse.move(0, move)
        else:
            direction = {
                self.left: keyboard.Key.left,
                self.right: keyboard.Key.right,
                self.up: keyboard.Key.up,
                self.down: keyboard.Key.down,
                self.shiftleft: keyboard.Key.left,
                self.shiftright: keyboard.Key.right,
                self.shiftup: keyboard.Key.up,
                self.shiftdown: keyboard.Key.down,
            }
            if k in direction:
                self.keyboard.press(direction[k])
                if not self.isSlow:
                    for _ in range(self.arrowSize):
                        self.keyboard.press(direction[k])

        # ✅ 방향/마우스 모드에서 키 입력 제거 (IME 대응)
        if self.mode_flag:
            try:
                if key.char and key.char.lower() in self.cmds:
                    self.keyboard.press(keyboard.Key.backspace)
                    self.keyboard.release(keyboard.Key.backspace)
            except:
                pass

    def on_release(self, key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)

        # Shift + Space 시 space 무시
        if key == keyboard.Key.space:
            if keyboard.Key.shift in self.pressed_keys or keyboard.Key.shift_r in self.pressed_keys:
                return

        if not self.mode_flag:
            return

        try:
            k = key.char.lower()
        except AttributeError:
            return

        if k == self.mouseSlow:
            self.isSlow = True
            self.speed = self.speedSlow
        elif self.isMouse:
            if k == self.mouseLeft:
                self.mouse.release(mouse.Button.left)
            elif k == self.mouseRight:
                self.mouse.release(mouse.Button.right)
            elif k == self.mouseMiddle:
                self.mouse.release(mouse.Button.middle)
        else:
            direction_keys = [self.left, self.right, self.up, self.down,
                              self.shiftleft, self.shiftright, self.shiftup, self.shiftdown]
            if k in direction_keys:
                direction = {
                    self.left: keyboard.Key.left,
                    self.right: keyboard.Key.right,
                    self.up: keyboard.Key.up,
                    self.down: keyboard.Key.down,
                    self.shiftleft: keyboard.Key.left,
                    self.shiftright: keyboard.Key.right,
                    self.shiftup: keyboard.Key.up,
                    self.shiftdown: keyboard.Key.down,
                }
                self.keyboard.release(direction[k])


# 실행 유지
Shortcut().listener.join()
