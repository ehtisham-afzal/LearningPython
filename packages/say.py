# third party package availible on pypi.org and installed with command "pip install cowsay"
import cowsay

# python libraries module that comes prebuild with python
import sys


if len(sys.argv) >= 2:
    text = ""
    for string in sys.argv[1:]:
        text += string + " "
    cowsay.cow(text)
else:
    # cowsay.trex("Ehtisham")
    my_fish = r"""
    \
    \  
            /`·.¸
        /¸...¸`:·
    ¸.·´  ¸   `·.¸.·´)
    : © ):´;      ¸  {
    `·.¸ `·  ¸.·´\`·¸)
        `\\´´\¸.·´

    """
    cowsay.draw("fish are my favorit dish", my_fish)
