# tp_ros_dwijesh

1. cloner le projet dans votre workspace dans votre dossier src

`git clone https://github.com/dwijesh080200/tp_ros_dwijesh.git` 

2. faite une catkin build sur votre terminal

`catkin build`

3. sourcer votre setup.bash

`source ~/votre_workspace/devel/setup.bash`

**NOTER sourcer votre dossier a chaque fois vous ouvrez une terminal**

5. allumer roscore sur une autre terminal, pour cela

`roscore`

6. une fois cloner vous verez 2 dossier dans le dossier tp_ros_dwijesh

donc:
- src
    - pub.py
- launch
    - but.launch 

7. donner les droit d'execution au fichier dans src en cas il vous demande les droits

`chmod +x pub.py`

8. pour lancher les fichiers allez dans le dossier launch

9. faite une roslaunch

`roslaunch tp_ros_dwijesh but.launch`

vouz verez que une toggle ayant une bouton s'ouvrira donc le etat du bouton change a chaque presser du bouton

rviz aussi s'ouvrira

- clickez sur `add`

- clickez sur `by topic`

- clickez sur pose

** en cas vous verez pas le topic clickez sur le bouton du toggle apres re-essayer

vous devrez voir un PoseStamped qui fait la trajectoire d'un huit

a chaque fois vous appuyer sur le bouton l'etat du PoseStamped changera
- il fera immobile sur false
- il fera son trajectoire sur true

10. pour voir l'etat du bouton ouvrez un autre terminal et faite

`rostopic echo /button_state`










