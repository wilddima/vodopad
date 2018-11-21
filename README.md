# Vodopad

Manage your photographs with the power of deep learning! 📷

## Overview

A tool for finding people in photographs by one example of a photo with the person and grouping them into separate folders.

### Install

Using [pip](https://github.com/pypa/pip):

```
pip install vodopad
```

### Usage

The first parameter is a photo or a folder with photos, among which the utility will search for people.

Arguments:

* `--people`, `-p` - a photo or folder with photos of people to search

Example:
```
vodopad ./vacation_photos_folder --people=myphoto.jpg
```

* `--move`, `-m` - if this flag is set, photos will be deleted after copying. The default is copying without deletion

Example:
```
vodopad ./vacation_photos_folder --people=myphoto.jpg --move
```

* `--output`, `-o` - This argument specifies the folder in which to copy photos.

Example:
```
vodopad ./vacation_photos_folder --people=myphoto.jpg --output='./only_my_photos_from_vacation'
```

### Example

![Example](https://d2ddoduugvun08.cloudfront.net/items/0G0w1g1k060I150x2j24/render1542806024050.gif)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/wilddima/vodopad. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.
