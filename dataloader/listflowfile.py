import torch.utils.data as data

from PIL import Image
import os
import os.path

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def dataloader(filepath):

    classes = [d for d in os.listdir(filepath) if os.path.isdir(os.path.join(filepath, d))]
    image1 = [img for img in classes][0] + '/frames_cleanpass/' #if img.find('frames_cleanpass') > 0]
    disp1 = [dsp for dsp in classes][0] + '/disparity/'  #if dsp.find('disparity') > 0]

    all_left_img = []
    all_right_img = []
    all_left_disp = []
    test_left_img = []
    test_right_img = []
    test_left_disp = []

   # d_path = filepath +'Driving/'

    driving_dir = filepath + image1 #[x for x in image][0] + '/'
    driving_disp = filepath + disp1 #[x for x in disp][0]

    subdir1 = ['35mm_focallength', '15mm_focallength']
    subdir2 = ['scene_backwards', 'scene_forwards']
    subdir3 = ['fast', 'slow']

    for i in subdir1:
      for j in subdir2:
        for k in subdir3:
            imm_l = os.listdir(driving_dir+i+'/'+j+'/'+k+'/left/')
            for im in imm_l:
              if is_image_file(driving_dir+i+'/'+j+'/'+k+'/left/'+im):
                all_left_img.append(driving_dir+i+'/'+j+'/'+k+'/left/'+im)

              all_left_disp.append(driving_disp+'/'+i+'/'+j+'/'+k+'/left/'+im.split(".")[0]+'.pfm')

              if is_image_file(driving_dir+i+'/'+j+'/'+k+'/right/'+im):
                all_right_img.append(driving_dir+i+'/'+j+'/'+k+'/right/'+im)

    image2 = [img for img in classes][1] + '/frames_cleanpass/' #if img.find('frames_cleanpass') > 0]
    disp2 = [dsp for dsp in classes][1] + '/disparity/'  #if dsp.find('disparity') > 0]

    flying_path = filepath + image2#[x for x in image if 'FlyingThings3D' in x][0]
    flying_disp = filepath + disp2 #[x for x in disp if 'FlyingThings3D' in x][0]
    flying_dir = flying_path#+'/TRAIN/'
    subdir = ['A','B','C']


    for ss in subdir:
      flying = os.listdir(flying_dir+ss)

      for ff in flying:
        imm_l = os.listdir(flying_path+ss+'/'+ff+'/left/')
        for im in imm_l:
          if is_image_file(flying_path+ss+'/'+ff+'/left/'+im):
            all_left_img.append(flying_path+ss+'/'+ff+'/left/'+im)
          
          all_left_disp.append(flying_disp+ss+'/'+ff+'/left/'+im.split(".")[0]+'.pfm')

          if is_image_file(flying_path+ss+'/'+ff+'/right/'+im):
            all_right_img.append(flying_dir+ss+'/'+ff+'/right/'+im)

   # flying_dir = flying_path#+'/TEST/'

    subdir = ['A','B','C']

    for ss in subdir:
      flying = os.listdir(flying_dir+ss)

      for ff in flying:
        imm_l = os.listdir(flying_dir+ss+'/'+ff+'/left/')
        for im in imm_l:
          if is_image_file(flying_dir+ss+'/'+ff+'/left/'+im):
            test_left_img.append(flying_dir+ss+'/'+ff+'/left/'+im)
          
          test_left_disp.append(flying_disp+ss+'/'+ff+'/left/'+im.split(".")[0]+'.pfm')

          if is_image_file(flying_dir+ss+'/'+ff+'/right/'+im):
            test_right_img.append(flying_dir+ss+'/'+ff+'/right/'+im)


    image3 = [img for img in classes][2] + '/frames_cleanpass/' #if img.find('frames_cleanpass') > 0]
    disp3 = [dsp for dsp in classes][2] + '/disparity/'  #if dsp.find('disparity') > 0]

    monkaa_path = filepath + image3 # [x for x in image if 'Monkaa' in x][0]
    monkaa_disp = filepath + disp3  #[x for x in disp if 'Monkaa' in x][0]
    #monkaa_dir  = os.listdir(monkaa_path)

    subdir = ['0', '1', '2', '3']#, '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16','17', '18', '19', '20', '21']


    #for zz in monkaa_dir:
       # monkaa = os.listdir(monkaa_path + zz)
    for dd in subdir:
        for im in os.listdir(monkaa_path + '/left/' + dd + '/'):
            if is_image_file(monkaa_path + '/left/' + dd + '/' + im):
                    all_left_img.append(monkaa_path + '/left/' + dd + '/' + im)
                    all_left_disp.append(monkaa_disp + '/left/' + dd + '/' + im.split(".")[0]+'.pfm')

        for im in os.listdir(monkaa_path + '/right/' + dd + '/'):
            if is_image_file(monkaa_path + '/right/' + dd + '/' + im):
                all_right_img.append(monkaa_path + '/right/' + dd + '/' + im)



    return all_left_img, all_right_img, all_left_disp, test_left_img, test_right_img, test_left_disp


