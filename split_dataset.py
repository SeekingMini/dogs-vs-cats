import os
import shutil

BASE_DIR = './dataset'
# create train dataset, validation dataset and test dataset
train_dir = os.path.join(BASE_DIR, 'train')
os.mkdir(train_dir)
validation_dir = os.path.join(BASE_DIR, 'validation')
os.mkdir(validation_dir)
test_dir = os.path.join(BASE_DIR, 'test')
os.mkdir(test_dir)

# move cat images
fnames = ['cat.{}.jpg'.format(i) for i in range(9000)]
for fname in fnames:
    src = os.path.join(BASE_DIR, fname)
    dst = os.path.join(train_dir, fname)
    shutil.move(src, dst)
fnames = ['cat.{}.jpg'.format(i) for i in range(9000, 10000)]
for fname in fnames:
    src = os.path.join(BASE_DIR, fname)
    dst = os.path.join(validation_dir, fname)
    shutil.move(src, dst)
fnames = ['cat.{}.jpg'.format(i) for i in range(10000, 12500)]
for fname in fnames:
    src = os.path.join(BASE_DIR, fname)
    dst = os.path.join(test_dir, fname)
    shutil.move(src, dst)

# move dog images
fnames = ['dog.{}.jpg'.format(i) for i in range(9000)]
for fname in fnames:
    src = os.path.join(BASE_DIR, fname)
    dst = os.path.join(train_dir, fname)
    shutil.move(src, dst)
fnames = ['dog.{}.jpg'.format(i) for i in range(9000, 10000)]
for fname in fnames:
    src = os.path.join(BASE_DIR, fname)
    dst = os.path.join(validation_dir, fname)
    shutil.move(src, dst)
fnames = ['dog.{}.jpg'.format(i) for i in range(10000, 12500)]
for fname in fnames:
    src = os.path.join(BASE_DIR, fname)
    dst = os.path.join(test_dir, fname)
    shutil.move(src, dst)
