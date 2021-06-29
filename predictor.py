import tensorflow as tf

def load_img(img):
  max_dim = 512
  # img = tf.image.decode_image(img, channels=3)
  img = tf.image.convert_image_dtype(img, tf.float32)

  shape = tf.cast(tf.shape(img)[:-1], tf.float32)
  long_dim = max(shape)
  scale = max_dim / long_dim

  new_shape = tf.cast(shape * scale, tf.int32)

  img = tf.image.resize(img, new_shape)
  img = img[tf.newaxis, :]
  return img

def init_model():
  model = tf.keras.applications.MobileNet(include_top=True,weights='imagenet')
  return model

def predict(image,model):
  x = tf.keras.applications.mobilenet.preprocess_input(image*255)
  x = tf.image.resize(x,(224,224))
  prediction_probabilities = model(x)
  predicted_top_5 = tf.keras.applications.mobilenet.decode_predictions(prediction_probabilities.numpy())[0]
  return predicted_top_5[0]
