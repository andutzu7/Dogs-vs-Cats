cat_counter = 0
dog_counter = 0
for file in os.listdir(path):
    if cat_counter <= 100:
        if file.startswith('cat'):
            os.rename(path + '/' + file, f'{destination}cats/cat.{cat_counter}.jpg')
            cat_counter = cat_counter + 1

    if dog_counter <= 100:
        if file.startswith('dog'):
            os.rename(path + '/' + file, f'{destination}dogs/dog.{dog_counter}.jpg')
            dog_counter = dog_counter + 1
    if cat_counter >= 100 and dog_counter >= 100:
        break


# makin the file datastructure

def move_photos(path, destination):
    print(path + destination)
    """""
    for i in range(1001):
        for j in range(1, 3):
            if j % 2 == 1:
                animal = 'dog'
            else:
                animal = 'cat'
            filename = f'{animal}.{i}.jpg'
            shutil.move(path + filename, f'{destination}{animal}s/{filename}')
        x = f'{destination}animal/{filename}'
    """



def resize_photos(path):
    animal = ''
    for i in range(12500):
        for j in range(1, 3):
            if j % 2 == 1:
                animal = 'dog'
            else:
                animal = 'cat'
            filename = f'{animal}.{i}.jpg'
            img = cv2.imread(path + filename)
            resized_image = cv2.resize(img, (200, 200))
            cv2.imwrite(output_path + filename, resized_image)
        if i % 1000 == 0:
            print('normalized another 1k photos')


def load_cache_photos_narray(path):
    photos_array = []  # 200 w 200 h 3 canale de culoare
    animal = ''
    for i in range(12501):
        if i % 1000 == 0:
            print(i)
        for j in range(1, 3):
            if j % 2 == 1:
                animal = 'dog'
            else:
                animal = 'cat'
            filename = f'{animal}.{i}.jpg'
            img = cv2.imread(path + '/' + filename)
            photos_array.append(img)
    photos_array = np.asarray(photos_array)
    save('photos.npy', photos_array)  # caching the photos


def load_cache_labels_narray():
    print('todo')



path = './train'  # needs to be added a slash/do a path join for resize_photos
output_path = './ntrain'

datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

img = load_img('data/train/cats/cat.0.jpg')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)
i = 0
for batch in datagen.flow(x, batch_size=1,
                          save_to_dir='preview', save_prefix='cat', save_format='jpeg'):
    i += 1
    if i > 20:
        break


#makin the file datastructure


def move_photos(path, destination):
    cat_counter = 1000
    dog_counter = 1000
    for file in os.listdir(path):
        if cat_counter <= 1501:
            if file.startswith('cat'):
                os.rename(path + '/' + file, f'{destination}cats/cat.{cat_counter}.jpg')
                cat_counter = cat_counter + 1

        if dog_counter <= 1501:
            if file.startswith('dog'):
                os.rename(path + '/' + file, f'{destination}dogs/dog.{dog_counter}.jpg')
                dog_counter = dog_counter + 1
        if cat_counter >= 1501 and dog_counter >= 1501:
            break

move_photos('./ntrain','./data/train/')



def resize_photos(path):
    animal = ''
    for i in range(12500):
        for j in range(1, 3):
            if j % 2 == 1:
                animal = 'dog'
            else:
                animal = 'cat'
            filename = f'{animal}.{i}.jpg'
            img = cv2.imread(path + filename)
            resized_image = cv2.resize(img, (200, 200))
            cv2.imwrite(output_path + filename, resized_image)
        if i % 1000 == 0:
            print('normalized another 1k photos')


def load_cache_photos_narray(path):
    photos_array = []  # 200 w 200 h 3 canale de culoare
    animal = ''
    for i in range(12501):
        if i % 1000 == 0:
            print(i)
        for j in range(1, 3):
            if j % 2 == 1:
                animal = 'dog'
            else:
                animal = 'cat'
            filename = f'{animal}.{i}.jpg'
            img = cv2.imread(path + '/' + filename)
            photos_array.append(img)
    photos_array = np.asarray(photos_array)
    save('photos.npy', photos_array)  # caching the photos


path = './train'  # needs to be added a slash/do a path join for resize_photos
output_path = './ntrain'
