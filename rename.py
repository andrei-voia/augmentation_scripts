import os

count = 0
for dirname in os.listdir("."):
	if dirname == "rename.py":
		print("parsing...")
	else:
		count += 1
		os.rename(dirname, "pic_" + str(count) + ".jpg")
