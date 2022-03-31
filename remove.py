import os
from PIL import Image
path='C:/Users/kangu/Documents/binary_test/data/다먹고 남은 과자봉지_img_download - 복사본'
print(os.listdir(path))
for i in os.listdir(path):
  sajin = i
  name_p = path+'/'+sajin
  image1 = Image.open(name_p)
  imag1_size = image1.size
  image1.close()
  if imag1_size < (416,416):
    os.remove(name_p)
    print(name_p)
  else:
    pass
