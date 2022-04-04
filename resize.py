from PIL import Image
import os

keyword = '아이시스 페트병'
raw_path = 'C:/Users/kangu/Documents/binary_test/data/'+keyword+'_img_download/' # 원본 이미지 경로
data_path = './data/resize'  # 저장할 이미지 경로

  # 저장할 경로 없으면 생성
if not os.path.exists(data_path+'_'+keyword+'/'):
  os.mkdir(data_path+'_'+keyword+'/')

  #원본 이미지 경로의 모든 이미지 list 지정
data_list = os.listdir(raw_path)
print(len(data_list))

  # 모든 이미지 resize 후 저장하기
for name in data_list:
      # 이미지 열기
  im = Image.open(raw_path + name)

      # 이미지 resize
  im = im.resize((416, 416),Image.LANCZOS)

      # 이미지 JPG로 저장
  im = im.convert('RGB')
  im.save(data_path+'_'+keyword+'/' + name)
print('end ::: ')