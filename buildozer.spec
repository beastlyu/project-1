[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) Entry point to main Python file
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
source.exclude_patterns = license.txt

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = kivy

# (str) Custom source folders for requirements
# Sets custom source for any module names matching the source key
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
#android.permissions = INTERNET

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

