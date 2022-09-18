# FuzzyHosts
A tool to parse Ffuf json data for virtual hosts and add it to your hosts file.

Please note:
- This works best when you have filtered your Ffuf output.
- Changing your hosts file can be dangerous (KNOW WHAT YOU ARE DOING AND HOW TO FIX ANY MISTAKES).
  - I made one mistake while writing the original code for this and emptied out both my hosts and resolv.conf files!
- This was written for use on linux. No thought was put into making this work on either Mac or Windows.
  - You may have to make some minor changes in the source code. ¯\\\_(ツ)_/¯ 
