<p align="center">
  <img width ="200" height="200" src='https://github.com/matteo-concas/Grand-Projet/blob/master/Images/Logo%20Numerix.jpg'>
</p>
 
# Interface et créateur d'executable

Le code et le guide que vous trouverez ici permet de pouvoir créer une interface assez facilement puis de transformer votre script python en executable qui marchera sur n'importe quel ordi (même ceux sans Python).

## Installation 

Pour commencer télécharger ce GitHub dans un dossier de votre choix. Une fois ceci fait, créer un dossier Python où vous installerez Python 3.6 (et **seulement** 3.6) qui est téléchargeable [ici](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe "Python 3.6.0").

Nous allons maintenant devoir installer toutes les librairies **obligatoires**, vous pourrez toujours rajouter des librairies spécifique à votre code plus tard. Pour commencer ouvrez votre invite de commande (Command Prompt en anglais) et naviguez vers le dossier où vous avez téléchargé le GitHub à l'aide de la commande `cd`. Notez que dans le cas où votre dossier ce trouve sur un autre disque dur que C: vous devrez changer de disque dur avec la commande `[Lettre de votre disque dur]:`. Par exemple dans mon cas je ferais :
```Bash
d:
cd D:\Cours\Interface
``` 
Une fois que vous êtes dans votre dossier vous éxécuterez (toujours depuis l'invite de commande) les commandes suivantes :
```Bash
Python\Scripts\pip.exe install -r requirements.txt
```
Qui aura l'effet d'installer toutes les librairies se trouvant dans le fichier `requirements.txt`. Les librairies sont les suivantes :
* PyQt5 

  La librairie qui nous permettra d'avoir une interface.

* PyQt5-Tools
  
  La librairie qui nous permettra d'utiliser pyqt5designer, un logiciel permettrant de créer une interface de manière très simple puis    de l'importer dans un code Python.

* PyQtGraph

  Une librairie équivalente à Matplotlib mais qui gère les animations de manière plus efficace et est plus facile à implémenter dans une interface graphique.
 
* Numpy

  Librairie mathématique permettant de faire de l'algèbre linéaire dans Python.

* PyInstaller

  La librairie qui nous permettra de transformer le code Python en éxécutable.
 
Nous allons maintenant vérifier que tout est bien installé.

Dans le dossier ce trouvent deux scripts, `PyQt Designer.bat` et `Py_to_exe.bat`. Lancer le premier en double-cliquant dessus et la fenêtre de pyqt5designer devrait normalement s'ouvrir et ressembler à ça :
![alt text](https://github.com/matteo-concas/Grand-Projet/blob/master/Images/image.png)

Ci celui marche vous pouvez alors lancer le second script qui créera un éxécutable à partir du ficher `GUI_Transport.py`. Si tout c'est bien passé vous pourrez alors retrouver le .exe dans le dossier **dist** qui aura été créer durant la création de l'éxécutable.

## Création de votre propre éxécutable

Je ne ferai pas de guide sur PyQt5 et PyQt5designer car il en existe déjà plusieurs sur internet. Nous allons donc nous interésser à comment passer d'un fichier Python à une application. Si l'on ouvre le fichier `Py_to_exe.bat` dans le bloc-note nous pouvons voir ces trois lignes :

```Bash
@ECHO OFF
Python\Scripts\pyinstaller.exe GUI_Transport.py --onefile --noconsole  --icon Icon.ico
PAUSE
```
Celle qui nous interesse est celle du milieu, la commande
```Bash
Python\Scripts\pyinstaller.exe GUI_Transport.py --onefile --noconsole  --icon Icon.ico
```
On peut voir qu'on lance `pyinstaller.exe`, un éxécutable que l'on a installé avec la librairie PyInstaller. Nous donnons ensuite en argument notre fichier Python, `GUI_Transport.py`, puis trois autres paramètres.

1. `--onefile`

  Ce paramètre permet de rassembler tous les fichiers produits dans un seul fichier éxécutable, l'éxécutable sera plus gros mais il sera plus facile à distribuer et ne nécessitera pas la création d'un installateur.

2. `--noconsole`

  Ce paramètre permet simplement de cacher la console à chaque fois que vous lancez votre éxécutable.

3. `--icon Icon.ico`

  Ce paramètre assigne une icone à votre application, ici `Icon.ico` se trouve dans le GitHub et est simplement le logo du GP.
