f = open('./misc/fichier_questions_2.txt', "w", encoding='Utf-8')

banner = r"""
 ________  ________  _____ ______   ________  ___  __    _______   ________     
|\   __  \|\   ____\|\   _ \  _   \|\   __  \|\  \|\  \ |\  ___ \ |\   __  \    
\ \  \|\  \ \  \___|\ \  \\\__\ \  \ \  \|\  \ \  \/  /|\ \   __/|\ \  \|\  \   
 \ \  \\\  \ \  \    \ \  \\|__| \  \ \   __  \ \   ___  \ \  \_|/_\ \   _  _\  
  \ \  \\\  \ \  \____\ \  \    \ \  \ \  \ \  \ \  \\ \  \ \  \_|\ \ \  \\  \| 
   \ \_____  \ \_______\ \__\    \ \__\ \__\ \__\ \__\\ \__\ \_______\ \__\\ _\ 
    \|___| \__\|_______|\|__|     \|__|\|__|\|__|\|__| \|__|\|_______|\|__|\|__|
          \|__|                                              by Illian & Côme  """



running = True
while running:
    print(banner)
    print("Logiciel additionnel a QCM Maker pour ajouter des questions au Fichier de QCM")
    rep = {}
