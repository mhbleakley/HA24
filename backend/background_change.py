import os
import shutil

class BackgroundManager:
    def __init__(self, image_dir):
        self.image_dir = image_dir
        self.images = os.listdir(image_dir)
        self.num_images = len(self.images)
        self.current_index = 0
        self.random = False

    def rotate(self):
        self.current_index = self.current_index + 1 if self.current_index < self.num_images - 1 else 0
        im = self.images[self.current_index]
        if im == 'background.jpg':
            self.current_index = self.current_index + 1 if self.current_index < self.num_images - 1 else 0
            im = self.images[self.current_index]
        shutil.copyfile(self.image_dir + im, self.image_dir + 'background.jpg')
        print(f'background changed to {im}')