import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import random
import os


def print_image(image_path, image_title):
  image = mpimg.imread(image_path)
  plt.imshow(image)
  plt.title(image_title)
  plt.axis("off")
  print(f"Image shape: {image.shape}") 

  return image


def print_random_image(folder_path):
  random_class = random.sample(os.listdir(folder_path), 1)[0]
  class_path = folder_path + random_class + '/'
  random_image = random.sample(os.listdir(class_path), 1)[0]
  image_path = class_path + random_image + '/'

  image = mpimg.imread(image_path)
  plt.imshow(image)
  plt.title(random_class)
  plt.axis("off")
  print(f"Image shape: {image.shape}")

  return image


def print_n_random_image(folder_path, n, columns):
  random_classes = random.sample(os.listdir(folder_path), n)
  random_images = []

  for random_class in random_classes:
    class_path = folder_path + random_class + '/'
    random_image = random.sample(os.listdir(class_path), 1)[0]
    image_path = class_path + random_image + '/'
    random_images.append(image_path)

  fig = plt.figure(figsize=(15, 15))
  rows = math.ceil(n/columns)

  for i in range(len(random_images)):
    image = mpimg.imread(random_images[i])
    sub_index = i + 1
    fig.add_subplot(rows, columns, sub_index)
    plt.imshow(image)
    plt.title(random_classes[i])
    plt.axis("off")

  return image
