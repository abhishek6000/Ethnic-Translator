to_black = generator_g(sample_white)
to_white = generator_f(sample_black)
plt.figure(figsize=(8, 8))
contrast = 8

imgs = [sample_white, to_black, sample_black, to_white]
title = ['White', 'To Black', 'Black', 'To White']

for i in range(len(imgs)):
  plt.subplot(2, 2, i+1)
  plt.title(title[i])
  if i % 2 == 0:
    plt.imshow(imgs[i][0] * 0.5 + 0.5)
  else:
    plt.imshow(imgs[i][0] * 0.5 * contrast + 0.5)
plt.show()