from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import numpy as np
import matplotlib.pyplot as plt

def get_image(path):
    img = image.load_img(path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return img, x

model = load_model('horse_or_human.h5')


img, x = get_image('img/predicao/cavalo.jpg')
x = x.astype('float32') / 255.
plt.imshow(img)
probabilities = model.predict([x])
if probabilities[0][0] < 0.5: 
  print(f'É um cavalo, com probabilidade de {probabilities[0][1]:.2f}')
else: 
  print(f'É um humano, com probabilidade de {probabilities[0][0]:.2f}')