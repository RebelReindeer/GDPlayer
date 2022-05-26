import random
from cv2 import threshold
from pynput.mouse import Button, Controller
import keyboard
import torch
import pyautogui
import numpy as np
#region=(int(2879/3.5), 0, 2879, 1800)

def capture_screen_and_resize(region):
    img = pyautogui.screenshot(region=region)
    img = img.resize((80, 80))
    img = torch.tensor(img.getdata()).flatten()
    return img

#int(2879/3.5), 0, 2879, 1800)
class env:
    def __init__(self, num_frames, img_shape = (int(2879/3.5), 0, 2050, 1800)):
        self.num_frames = num_frames
        self.frame_mem = [torch.zeros(25600).flatten()] * num_frames
        self.mouse = Controller()
        self.frame_mem_counter = 0
        self.img_shape = img_shape
        self.__past_similiarities = np.array([])

    def reset(self):
        #press esc
        #move mouse to menu button and click
        #take a frame
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
         
        return self.frame_mem, 1, self.__is_done()

    def __is_done(self) -> bool:
        #compare to a dead screen
        screen = capture_screen_and_resize(self.img_shape)
        end_screen = torch.load("endscreen.pt")
        #see similiarity index of how similiar they are
        similiarity = (screen.numpy() == end_screen.numpy()).sum()
        self.__past_similiarities = np.append(self.__past_similiarities, similiarity)
        print(similiarity > self.__past_similiarities.mean() * 1.5)
        print(similiarity, self.__past_similiarities.mean() * 1.5)
        return similiarity > self.__past_similiarities.mean() * 1.5




gd = env(3)

state = [torch.zeros(25600)] * 3

done = False 
while not done:
    action = 0 #random.randint(0, 1)
    print(f'action: {action}')
    next_state, reward, done = gd.step(action)

    state = next_state
