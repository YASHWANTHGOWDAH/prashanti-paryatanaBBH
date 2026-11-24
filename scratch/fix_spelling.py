import glob
import os

files = glob.glob(r'C:\Users\yashw\Desktop\TASN  PP\TASN\*.html')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Header & footer brand names
    content = content.replace('PRASANTHI <span>PARIYATANA</span>', 'PRASHANTI <span>PARYATANA</span>')
    content = content.replace('PRASANTHI PARIYATANA', 'PRASHANTI PARYATANA')
    content = content.replace('Prasanthi Pariyatana', 'Prashanti Paryatana')
    content = content.replace('prasanthi pariyatana', 'prashanti paryatana')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Fixed spelling in: {os.path.basename(fpath)}')

print('All spelling corrections completed!')
