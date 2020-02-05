# wonderMailTyper
A Python script that automatically types out Wonder Mail codes in Pokémon Red/Blue Rescue Team

Just copy and paste the wondermail generated by this website and remove the spaces: https://syphist.com/pmd/rt/wondermail.html
To run the .py file you need Python. I use 3.X. Once this is installed you need to do the following in cmd:

pip install pyautogui

pip install numpy

Soon I will compile this into an executable so you won't need to do this eventually. But this will do for now. Go into the .py file and set your bindings on the line where it says:
```autoTyper(string,movementKeys=('w','a','x','d'),selectKey = 'j')```

And then change your movement keys and your a button (which is selectKey, bad name but I also have x as my down button).

This program saves the hassle of many Wonder Mails.
