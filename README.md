# Gallery Tools
Collection of tools for manipulating a directory of images and files.<br>
@MostafaMDZH | mostafa.mDZH@gmail.com</br>

Put all your images(including subdirectories) into the "gallery" directory and use the tools below:</br></br>

# • Image Resizer
Resize all the images in a directory to a specific resolution based on the small side(depending on the image orientation), and resize the big side based on the original ratio.</br>
<b>Usage</b>: run the main file while passing the resolution(default is 1080):</br>
> python3 Resize.py 720

</br>

# • Thumbnail Maker
Create a thumbnail for all the images in a directory.</br>
<b>Usage</b>: run the main file while passing the resolution size(default is 300 pixels)</br>
> python3 MakeThumbnail.py 480

</br>

# • Watermark Adder
Add a watermark to all the images in a directory.</br>
<b>Usage</b>: run the main file with python 3 while passing the text you want to watermark(it ignores thumbnails with .min in their names)</br>
> python3 AddWatermark.py "Watermark Text"

</br>

# • PNG to JPG Convertor
Convert all the .png images in a directory into the .jpg format.</br>
<b>Usage</b>: just run the main file like:</br>
> python3 PngToJpg.py

</br>

# • Naming Statistics
Count the first letter of all the files in a directory.</br>
<b>Usage</b>: just run the main file like:</br>
> python3 Statistics.py

</br>

# • Name Corrector
Correct a list of file names based on a JSON file.</br>
<b>Usage</b>: fill the list.json file(like the sample) and run:</br>
> python3 CorrectNames.py

</br>

# • Rename Pixabay.com Images
Grab the actual image names and remove numbers and underlines from all the images in the directory downloaded from pixabay.com.</br>
<b>Usage</b>: just run the main file like:</br>
> python3 PixabayRename.py