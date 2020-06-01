<p align="center">
  <img width ="200" height="200" src='https://github.com/matteo-concas/Grand-Projet/blob/master/Images/Logo%20Numerix.jpg'>
</p>
 
# Interface et créateur d'exécutable

Le code et le guide que vous trouverez ici permet de pouvoir créer une interface assez facilement puis de transformer votre script python en exécutable qui marchera sur n'importe quel ordinateur (même ceux sans Python).

## Installation 

Pour commencer télécharger ce GitHub dans un dossier de votre choix, il se trouve personellement dans un dossier nommé 'Interface'. Une fois ceci fait, créer un dossier Python où vous installerez Python 3.6 (et **seulement** 3.6) qui est téléchargeable [ici](https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe "Python 3.6.0").

Votre dossier devrait donc ressembler à ça :

![alt text](https://github.com/matteo-concas/Grand-Projet/blob/master/Images/Dossier.png)

Nous allons maintenant devoir installer toutes les librairies **obligatoires**, vous pourrez toujours rajouter des librairies spécifique à votre code plus tard. Pour commencer ouvrez votre invite de commande (Command Prompt en anglais) et naviguez vers le dossier où vous avez téléchargé le GitHub à l'aide de la commande `cd`. Notez que dans le cas où votre dossier ce trouve sur un autre disque dur que C: vous devrez changer de disque dur avec la commande `[Lettre de votre disque dur]:`. Par exemple dans mon cas je ferais :
```Bash
d:
cd D:\Cours\Interface
``` 
Une fois que vous êtes dans votre dossier vous exécuterez (toujours depuis l'invite de commande) les commandes suivantes :
```Bash
Python\Scripts\pip install -r requirements.txt
```
Qui aura l'effet d'installer toutes les librairies se trouvant dans le fichier `requirements.txt`. Les librairies sont les suivantes :
* PyQt5 

  La librairie qui nous permettra d'avoir une interface.

* PyQt5-Tools
  
  La librairie qui nous permettra d'utiliser pyqt5designer, un logiciel permettrant de créer une interface de manière très simple puis    de l'importer dans un code Python.

* PyQtGraph

  Une librairie équivalente à Matplotlib mais qui gère les animations de manière plus efficace et est plus facile à implémenter dans une interface graphique.
 
* PyOpenGl

  Une librairie permettant de faire des graphiques 3D de manière efficace en utilisant l'API OpenGL.
 
* Numpy

  Librairie mathématique permettant de faire de l'algèbre linéaire dans Python.

* PyInstaller

  La librairie qui nous permettra de transformer le code Python en exécutable.
 
Nous allons maintenant vérifier que tout est bien installé.

Dans le dossier se trouvent deux scripts, `PyQt Designer.bat` et `Py_to_exe.bat`. Lancez le premier en double-cliquant dessus et la fenêtre de pyqt5designer devrait normalement s'ouvrir et ressembler à ça :
![alt text](https://github.com/matteo-concas/Grand-Projet/blob/master/Images/image.png)

Si celui marche vous pouvez alors lancer le second script qui créera un exécutable à partir du ficher `GUI_Transport.py`. Si tout c'est bien passé vous pourrez alors retrouver le .exe dans le dossier **dist** qui aura été crée durant la création de l'exécutable.


## Création de l'interface avec PyQt5

Après avoir lancé le premier script, `PyQt Designer.bat`, vous arrivez sur l'écran de création de l'interface où vous pouvez placer des boutons, champs de texte, images etc. Une fois ceci fait, si vous sauvegardez l'interface vous aurez un fichier .ui et non un fichier Python. Nous allons donc devoir exécuter une commande depuis l'invite de commande pour obtenir le fichier Python. Toujours dans le dossier principal où l'on a lancer toutes les commandes précédentes, remplacez `fichier` par le nom de votre fichier et tapez :
```Bash
Python\Scripts\pyuic5 fichier.ui -o fichier.py
```
Vous aurez ensuite votre fichier Python avec une classe. Pour pouvoir exécuter l'interface il faudra lancer la classe en rajoutant à la fin du fichier Python ces lignes :
```Python
class AppWindow(QDialog) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
```
Ici `Ui_Dialog()` est la classe que PyQt Designer a crée (celle qui contient votre interface et le reste de votre code), si vous renommez la première classe de votre script vous devrez aussi changer cette ligne. Généralement votre première classe pourra aussi s'appeler `Ui_MainWindow`, il faudra alors changer `QDialog` par `QMainWindow` tout en vérifiant bien que l'objet soit importé au début de votre code (ces deux objets peuvent être importés depuis `PyQt5.QtWidgets`).
Vous pouvez ensuite rajouter votre code dans la première classe sous forme de fonctions. Vous pouvez par exemple avoir une fonction où vous faites la résolution d'équation et une autre où vous affichez les résultats etc.

## Création de votre propre exécutable

Nous allons maintenant nous interésser à comment passer d'un fichier Python à une application. Si l'on ouvre le fichier `Py_to_exe.bat` dans le bloc-note nous pouvons voir ces trois lignes :

```Batch
@ECHO OFF
Python\Scripts\pyinstaller.exe GUI_Transport.py --onefile --noconsole  --icon Icon.ico
PAUSE
```
Celle qui nous interesse est celle du milieu, la commande
```Bash
Python\Scripts\pyinstaller.exe GUI_Transport.py --onefile --noconsole  --icon Icon.ico
```
On peut voir qu'on lance `pyinstaller.exe`, un exécutable que l'on a installé avec la librairie PyInstaller. Nous donnons ensuite en argument notre fichier Python, `GUI_Transport.py`, puis trois autres paramètres.

1. `--onefile`

  Ce paramètre permet de rassembler tous les fichiers produits dans un seul fichier exécutable, il sera plus gros mais aussi plus facile à distribuer et ne nécessitera pas la création d'un installateur.

2. `--noconsole`

  Ce paramètre permet simplement de cacher la console à chaque fois que vous lancez votre application.

3. `--icon Icon.ico`

  Ce paramètre assigne une icone à votre application, ici `Icon.ico` se trouve dans le GitHub et est simplement le logo du GP.

Si vous avez des questions n'hésitez à m'envoyer un mail à **matteo.concas@ipsa.fr**.
