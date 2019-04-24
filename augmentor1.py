import Augmentor

p = Augmentor.Pipeline("C:\\Users\\PREDATOREL\\Desktop\\test")

# Add operations to the pipeline as normal:
p.rotate(probability=0.7, max_left_rotation=20, max_right_rotation=20)
p.zoom(probability=0.3, min_factor=0.85, max_factor=1.15)
p.random_brightness(probability=0.9, min_factor=0.7, max_factor=1.2)
p.flip_left_right(probability=0.8)
p.crop_random(probability=0.9, percentage_area=0.85, randomise_percentage_area=False)
# p.rotate_without_crop(probability=0.7, max_left_rotation=20, max_right_rotation=20)
# p.gaussian_distortion(probability=0.5, grid_width=1000, grid_height=1000, magnitude=20, corner="bell", method="in")

p.sample(600)