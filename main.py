from pyscript import display, document

glee_Club = {'Kaitlyn', 'Louise', 'Samantha', 'Hailey', 'Jade', 'Francesca', 'Sofia', 'Charlize'}
dance_Club = {'Sofia', 'Charlize', 'Francesca', 'Jade', 'Liana', 'Gabrielle', 'Frances', 'Geron'}


display(glee_Club, target='glee')
display(dance_Club, target='dance')

display(glee_Club & dance_Club, target='bothClubs')
display(glee_Club - dance_Club, target='onlyGlee')
display(dance_Club - glee_Club, target='onlyDance')
display(glee_Club ^ dance_Club, target='oneClub')

