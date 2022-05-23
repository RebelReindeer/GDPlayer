import random
from pynput.mouse import Button, Controller
import keyboard
import torch
import pyautogui
#region=(int(2879/3.5), 0, 2879, 1800)

def capture_screen_and_resize(region):
    img = pyautogui.screenshot(region=region)
    img = img.resize((80, 80))
    img.show()
    img = torch.tensor(img.getdata()).flatten()
    return img

class env:
    def __init__(self, num_frames, img_shape = (int(2879/3.5), 0, 2879, 1800)):
        self.num_frames = num_frames
        self.frame_mem = [torch.zeros(25600).flatten()] * num_frames
        self.mouse = Controller()
        self.frame_mem_counter = 0
        self.img_shape = img_shape

    def reset(self):
        #take 3 frames
        #return 3 frames
        pass

    def step(self, action):

        #missing a function to figure out if done or not
        #need a function to get how far into the level we are, return that as result
        if action == 1:
            keyboard.press_and_release('space')
            next_frame = capture_screen_and_resize(region = self.img_shape)
            self.frame_mem[self.frame_mem_counter] = next_frame
            self.frame_mem_counter += 1 if self.frame_mem_counter < 2 else 0
        else:          
            next_frame = capture_screen_and_resize(region = self.img_shape)          
            self.frame_mem[self.frame_mem_counter] = next_frame
            self.frame_mem_counter += 1 if self.frame_mem_counter < 2 else 0
         
        return self.frame_mem, 1, False  

    def done(self):
        #check if gd lvl is over
        #return true or false           
        pass 

gd = env(3)

state = [torch.zeros(25600)] * 3

done = False
while not done:
    action = random.randint(0, 1)
    print(f'action: {action}')
    next_state, reward, done = gd.step(action)

    state = next_state
