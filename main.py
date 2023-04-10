import os
from bs4 import BeautifulSoup
from tqdm import tqdm
import csv 

filename = "000002134416000050_a2015123110-k-t50"
filenames = [filename.split('.')[0] for filename in os.listdir('train_label')]

with open('spanning.csv', 'w') as f:
    csvwriter = csv.writer(f, delimiter=',')
    csvwriter.writerow(['filename','spanning_pct'])
    for filename in tqdm(filenames):
        img_filename = 'train_images/' + filename + ".png"
        label_filename = 'train_label/' + filename + ".xml"

        with open(label_filename, 'r') as file:
            text = file.read()
            bs4_text = BeautifulSoup(text, 'lxml')
            total_td = len(bs4_text.find_all('td'))
            total_spanning = 0
            for td in bs4_text.find_all('td'):
                try:
                    total_spanning += int(td['colspan']) - 1
                except:
                    pass
            spanning_pct = total_spanning / (total_spanning + total_td)
            csvwriter.writerow([filename, spanning_pct])