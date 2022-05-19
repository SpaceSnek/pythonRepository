def morse(txt):
    d = {'A':'owouwu','B':'uwuowoowoowo','C':'uwuowouwuowo','D':'uwuowoowo','E':'owo',
         'F':'owoowouwuowo','G':'uwuuwuowo','H':'owoowoowoowo','I':'owoowo','J':'owouwuuwuuwu',
         'K':'uwuowouwu','L':'owouwuowoowo','M':'uwuuwu','N':'uwuowo','O':'uwuuwuuwu',
         'P':'owouwuuwuowo','Q':'uwuuwuowouwu','R':'owouwuowo','S':'owoowoowo','T':'uwu',
         'U':'owoowouwu','V':'owoowoowouwu','W':'owouwuuwu','X':'uwuowoowouwu','Y':'uwuowouwuuwu',
         'Z':'uwuuwuowoowo', ' ':'owoowoowoowoowo'}
    translation = ''
    
    if txt.startswith('owo') or txt.startswith('uwu'):
        d_encrypt = dict([(v, k) for k, v in d.items()])
        txt = txt.split(' ')
        for x in txt:
            translation += d_encrypt.get(x)
        
    else:
        txt = txt.upper()
        for x in txt:
            translation += d.get(x) + ' '
    return translation.strip()
print("""⠀⠀⠀
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
⣠⣾⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣷⣄⠀
⣿⣿⡇⠀⠀⢸⣿⢰⣿⡆⠀⣾⣿⡆⠀⣾⣷⠀⣿⣿⡇⠀⠀⢸⣿⣿⠀
⣿⣿⡇⠀⠀⢸⣿⠘⣿⣿⣤⣿⣿⣿⣤⣿⡇⠀⢻⣿⡇⠀⠀⢸⣿⣿⠀
⣿⣿⡇⠀⠀⢸⡿⠀⢹⣿⣿⣿⣿⣿⣿⣿⠁⠀⢸⣿⣇⠀⠀⢸⣿⣿⠀
⠙⢿⣷⣶⣶⡿⠁⠀⠈⣿⣿⠟⠀⣿⣿⠇⠀⠀⠈⠻⣿⣿⣿⣿⡿⠋    Generator!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
morseSelect = input("Would you like to encode or decode a message?(e/d): ").lower()
if morseSelect == "e":
    morseInput = input("Please input what you would like to encrypt:")
    print("Encoded message:")
    print(morse(morseInput))
elif morseSelect =="d":
        morseInput = input("Please input what you would like to decrypt:")
        print("Decoded message:")
        print(morse(morseInput))