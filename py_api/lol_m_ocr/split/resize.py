from PIL import Image
import os
def resize(path,size=(1792,828)):
  image = Image.open(path)  # 创建图像实例
  print(image.format, image.size, image.mode)
  image=image.resize(size)
  image.save('./data/resize/xxx'+'.png','PNG')
  # image.show() # 显示图像


h=1792
w=828
# inPaht = './data/origin'
# outPath = '' 
# output_dir = "./data/resize"
# 获取输入文件夹中的所有文件
def resizeFiles(inPaht='./data/origin/',outPaht ="./data/resize/" ):
    files = os.listdir(inPaht)
    for file in files:
            if not file.startswith('.'):
              img = Image.open(inPaht+ file)
              if img.mode == "P":
                  img = img.convert('RGB')
              if img.mode == "RGBA":
                  img = img.convert('RGB')
              img = img.resize((h,w), Image.ANTIALIAS)
              img.save(os.path.join(outPaht, file))

# resize('./data/WechatIMG5030.jpeg')