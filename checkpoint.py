def checkpt():
	checkpoint_path = "./checkpoints/train"
	ckpt = tf.train.Checkpoint(generator_g=generator_g,
                           generator_f=generator_f,
                           discriminator_x=discriminator_x,
                           discriminator_y=discriminator_y,
                           generator_g_optimizer=generator_g_optimizer,
                           generator_f_optimizer=generator_f_optimizer,
                           discriminator_x_optimizer=discriminator_x_optimizer,
                           discriminator_y_optimizer=discriminator_y_optimizer)

	ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)
	# if a checkpoint exists, restore the latest checkpoint.
	if ckpt_manager.latest_checkpoint:
  		ckpt.restore(ckpt_manager.latest_checkpoint)
  		print ('Latest checkpoint restored!!')