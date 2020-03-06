def random_jitter(image):
  # resizing to 286 x 286 x 3
  image = tf.image.resize(image, [286, 286],method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
  
  image = random_crop(image)# randomly cropping to 256 x 256 x 3

  image = tf.image.random_flip_left_right(image)# random mirroring

  return image