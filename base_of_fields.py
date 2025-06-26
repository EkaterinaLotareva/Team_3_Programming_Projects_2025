hex1 = {(0, 0): ['mountain', 'jaguar', None], (1, 0): ['forest', None, None], (2, 0): ['forest', None, None],
            (3, 0): ['swamp', None, None], (4, 0): ['swamp', None, None], (5, 0): ['mountain', None, None],
            (6, 0): ['mountain', None, None], (0, 1): ['swamp', 'jaguar', None], (0, 2): ['forest', None, None],
            (0, 3): ['forest', None, None], (0, 4): ['forest', None, None], (0, 5): ['water', None, None],
            (0, -1): ['forest', None, None], (1, -1): ['water', None, None], (2, -1): ['swamp', None, None],
            (3, -1): ['swamp', None, None], (4, -1): ['desert', None, None], (5, -1): ['desert', 'bear', None],
            (1, -2): ['water', None, None], (2, -2): ['water', None, None], (3, -2): ['mountain', None, None],
            (4, -2): ['mountain', 'bear', None], (2, -3): ['water', None, ['blue', 'monument']],
            (3, -3): ['mountain', None, None], (-1, 0): ['mountain', None, None], (-1, 1): ['mountain', None, None],
            (-1, 2): ['mountain', None, None], (-1, 3): ['water', None, None], (-1, 4): ['water', None, None],
            (-2, 1): ['mountain', None, None], (-2, 2): ['water', None, ['white', 'hut']], (-2, 3): ['water', None, None],
            (-3, 2): ['water', None, None], (1, 1): ['swamp', 'jaguar', None], (2, 1): ['forest', None, None],
            (3, 1): ['swamp', None, None], (4, 1): ['mountain', None, None], (5, 1): ['mountain', None, None],
            (6, 1): ['water', None, None], (7, 1): ['water', 'jaguar', None], (1, 2): ['swamp', None, None],
            (1, 3): ['forest', None, None], (1, 4): ['water', None, None], (1, 5): ['water', None, None],
            (1, 6): ['swamp', None, None], (2, 2): ['swamp', None, ['green', 'monument']], (3, 2): ['desert', None, None],
            (4, 2): ['desert', None, None], (5, 2): ['mountain', None, None], (6, 2): ['water', None, None],
            (7, 2): ['forest', None, None], (8, 2): ['forest', 'jaguar', None], (2, 3): ['forest', None, None],
            (2, 4): ['water', None, None], (2, 5): ['water', None, None], (2, 6): ['swamp', None, None],
            (2, 7): ['swamp', None, None], (3, 3): ['forest', None, None], (4, 3): ['desert', None, None],
            (5, 3): ['desert', None, None], (6, 3): ['desert', None, None], (7, 3): ['forest', None, None],
            (8, 3): ['mountain', None, None], (9, 3): ['swamp', None, None], (3, 4): ['forest', None, None],
            (3, 5): ['desert', None, None], (3, 6): ['desert', None, None], (3, 7): ['swamp', None, None],
            (3, 8): ['water', 'bear', None], (4, 4): ['forest', None, None], (5, 4): ['desert', None, None],
            (6, 4): ['desert', None, ['green', 'hut']], (7, 4): ['mountain', None, None],
            (8, 4): ['mountain', None, ['white', 'monument']], (9, 4): ['swamp', None, None],
            (10, 4): ['swamp', None, None], (4, 5): ['desert', 'bear', ['blue', 'hut']], (4, 6): ['desert', 'bear', None],
            (4, 7): ['water', None, None], (4, 8): ['water', 'bear', None], (4, 9): ['mountain', 'bear', None],
            (5, 5): ['forest', 'bear', None], (6, 5): ['desert', None, None], (7, 5): ['mountain', None, None],
            (8, 5): ['desert', None, None], (9, 5): ['forest', None, None], (10, 5): ['forest', 'jaguar', None],
            (11, 5): ['swamp', 'jaguar', None], (5, 6): ['desert', None, None], (5, 7): ['water', None, None],
            (5, 8): ['water', None, None], (5, 9): ['mountain', None, None], (5, 10): ['mountain', None, None],
            (6, 6): ['desert', None, None], (7, 6): ['desert', None, None], (8, 6): ['desert', None, None],
            (9, 6): ['forest', None, None], (10, 6): ['forest', 'jaguar', None], (6, 7): ['desert', None, None],
            (6, 8): ['desert', None, None], (6, 9): ['mountain', None, None], (6, 10): ['mountain', None, None],
            (7, 7): ['swamp', None, None], (8, 7): ['forest', None, None], (9, 7): ['forest', None, None],
            (7, 8): ['swamp', None, None], (7, 9): ['swamp', None, None], (8, 8): ['swamp', None, None]}

hex2 = { (0, 0) : ['swamp', None, None], (0, 1): ['swamp', None, None], (0,2): ['water', None, None], (0,3):['water', None, None],
            (0,4): ['forest', None, None], (0,5): ['desert', 'bear', None], (-1, 0) : ['swamp', None, None], (-1, 1): ['desert', None, None],
            (-1,2): ['desert', None, None], (-1,3): ['forest', None, ['green','hut']], (-1,4): ['forest', None None], (-2,1):['desert', 'bear', None], (-2,2):['desert','bear',['white','hut']],(-2,3):['forest',None,None],(-3,2):['forest',None,None],
            (1, -2):['forest', None, None], (1, -1):['forest', None, None], (1,0):['water', 'jaguar', None], (1,1):['swamp', None, None], (1,2):['water', None, None], 
            (1,3):['water', None, None], (1,4):['swamp', None, None], (1,5):['desert', None, None], (1,6):['mountain', 'bear', None],
            (2,-3):['desert', None, None], (2, -2):['desert',None, None],(2,-1):['water', None, None], (2,0):['water', None, None],
            (2,1):['mountain', None, None], (2,2):['water', None, None], (2,3):['swamp', None, None],(2,4):['swamp',None, None], 
            (2,5):['swamp',None, None], (2,6):['mountain', None, None],(2,7):['mountain', None, None],(3,-3):['desert', None, None], (3, -2):['desert', None, None],
            (3, -1):['mountain', None, None],(3,0):['mountain', None, ['blue', 'monument']],(3,1):['mountain', None, None],(3,2):['water', None, None],
            (3,3):['forest', None, None], (3,4):['forest', None, None],(3,5):['swamp', None, None], (3,6):['water', None, None], 
            (3,7):['water', None, None], (3,8):['swamp', 'jaguar', None] , (4,-2):['desert', None, None], (4, -1):['desert', None, None],
            (4,0):['mountain', None, None],(4,1):['mountain', None, None],(4,2):['water', None, None], (4,3):['water', None, None],
            (4,4):['forest', None, None], (4,5):['water', None, None], (4,6):['water', None, None],(4,7):['forest','jaguar', None],
            (4,8):['forest', 'jaguar', None],(4,9):['swamp', None, None],(5,-1)['desert', None, None],(5,0):['mountain', None, None], (5,1):['mountain', None, None], (5,2):['mountain', None, None],
            (5,3):['water', None, None], (5,4):['water', None, None],(5,5):['forest', None, None],(5,6):['forest', None, None],
            (5,7):['forest', None, None],(5,8):['forest', None, None], (5,9):['swamp', None, None], (5,10):['swamp', None, None],
            (6,0):['mountain', 'jaguar', None],(6,1):['swamp', 'jaguar',None],(6,2):['forest', None, None],(6,3):['forest',None, None],
            (6,4):['forest', None, None],(6,5):['water','bear',None],(6,6):['forest',None,None],(6,7):['desert',None,None],(6,8):['desert',None, ['blue','hut']],
            (6,9):['mountain',None,None],(6,10):['mountain',None,None], (7,1):['swamp','jaguar',None],(7,2):['swamp',None,None],(7,3):['forest',None,None],
            (7,4):['water',None,None],(7,5):['water','bear',None],(7,6):['mountain','bear',None],(7,7):['desert',None,None],
            (7,8):['mountain',None,None],(7,9):['mountain',None,None],(8,2):['swamp',None,None],(8,3):['desert',None,None],
            (8,4):['water',None,None],(8,5):['water',None,None],(8,6):['mountain',None,None],(8,7):['mountain',None,None],(8,8):['desert',None,None],
            (9,3):['desert',None,None],(9,4):['desert',None,None],(9,5):['desert',None,None],(9,6):['mountain',None,['white','monument']],(9,7):['mountain',None,['green','monument']],
            (10,4):['swamp',None,None],(10,5):['swamp',None,None],(10,6):['swamp',None, None],(11,5):['swamp',None,None]}

hex3 = { (0,0):['mountain',None, None], (0,1):['montain', None, None],(0,2):['swamp', None, None], (0,3):['swamp', None, ['blue','hut']], (0,4)['swamp',None,None],
        (0,5):['water','bear',None],(-1,0):['water',None,None],(-1,1):['water',None,None],(-1,2):['swamp',None,None],(-1,3):['forest',None,None],(-1,4):['forest',None, None],
        (-2,1):['water',None, None],(-2,2):['water',None,None],(-2,3):['forest',None,None],(-3,2):['forest',None,None], (0,-1):['forest','jaguar',None],
        (1,-2):['forest',None,['blue','monument']],(1,-1):['forest',None,['white','monument']],(1,0):['water','jaguar',None],(1,1):['mountain','bear',None],(1,2):['desert',None,None],
        (1,3):['swamp',None,None],(1,4):['water',None,None], (1,5):['water','bear',None],(1,6):['mountain','bear',None],
        (2,-3):['desert',None,None],(2,-2):['desert',None,None],(2,-1):['water',None,None],(2,0):['water',None,None],
        (2,1):['mountain',None,None],(2,2):['desert','bear',None],(2,3):['desert',None,None],(2,4):['water',None,None],(2,5):['water',None,None],
        (2,6):['mountain',None,None],(2,7):['mountain',None,None],(3,-3):['desert',None,None],(3,-2):['desert',None,None],
        (3,-1):['mountain',None,None],(3,0):['mountain',None,None],(3,1):['mountain',None,None],(3,2):['forest','bear',None],
        (3,3):['desert',None,None],(3,4):['desert',None,None],(3,5):['desert',None,None],(3,6):['mountain',None,None],(3,7):['mountain',None,None],(3,8):['desert',None,None],
        (4,-2):['desert',None,['green','monument']],(4,-1):['desert',None,None],(4,0):['mountain',None,None],(4,1):['desert','bear',None],
        (4,2):['desert','bear',None],(4,3):['forest',None,None],(4,4):['swamp',None,None],(4,5):['swamp',None,None],(4,6):['swamp',None,None],
        (4,7):['mountain',None,None],(4,8):['mountain',None,None],(4,9):['desert',None,None],(5,-1):['desert',None,None],
        (5,0):['swamp',None,None],(5,1):['desert',None,None],(5,2):['desert',None,None],(5,3):['forest',None,None],(5,4):['forest',None,None],
        (5,5):['swamp',None,None],(5,6):['mountain',None,['green','hut']],(5,7):['mountain',None,None],(5,8):['desert',None,None],(5,9):['desert',None,None],
        (5,10):['forest',None,None],(6,0):['swamp',None,None],(6,1):['swamp',None,None],(6,2):['water',None,None],(6,3):['water',None,None],(6,4):['forest',None,None],
        (6,5):['swamp',None,None],(6,6):['swamp',None,None],(6,7):['swamp',None,None],(6,8):['forest',None,None],(6,9):['forest',None,None],(6,10):['forest',None,None],
        (7,1):['swamp',None,None],(7,2):['water',None,None],(7,3):['water',None,None],(7,4):['forest',None,None],(7,5):['swamp',None,None],(7,6):['swamp','jaguar',None],
        (7,7):['swamp',None,None],(7,8):['forest','jaguar',['white','hut']],(7,9):['forest','jaguar',None],(8,2):['water',None,None],(8,3):['forest',None,None],
        (8,4):['forest',None,None],(8,5):['forest',None,None],(8,6):['swamp','jaguar',None],(8,7):['mountain','jaguar',None],(8,8):['swamp','jaguar',None],
        (9,3):['water',None,None],(9,4):['water',None,None],(9,5):['mountain',None,None],(9,6):['mountain',None,None],(9,7):['mountain',None,None],
        (10,4):['mountain',None,None],(10,5):['mountain',None,None],(10,6):['mountain',None,None],(11,5):['water',None,None]}

hex4 = {(0,0):['forest', None, None],(0,-1):['water',None,None],(0,1):['desert',None,None],(0,2):['desert',None,None],(0,3):['mountain',None,None],(0,4):['mountain',None,None],(0,5):['swamp',None,None],
        (-1,0):['forest',None,None],(-1,1):['forest',None,None],(-1,2):['forest',None,None],(-1,3):['swamp',None,None],(-1,4):['swamp',None,None],
        (-2,1):['forest','jaguar',None],(-2,2):['forest','jaguar',None],(-2,3):['swamp',None,None],(-3,2):['swamp','jaguar',None],
        (1,-2):['water',None,None],(1,-1):['water',None,None],(1,0):['swamp',None,None],(1,1):['desert',None,['white','hut']],(1,2):['mountain',None,None],(1,3):['mountain',None,None],(1,4):['swamp',None,None],(1,5):['swamp',None,None],(1,6):['swamp',None,None],
        (2,-3):['forest',None,None],(2,-2):['water',None,None],(2,-1):['water',None,None],(2,0):['swamp',None,['green','hut']],(2,1):['swamp',None,None],(2,2):['desert',None,None],(2,3):['mountain',None,None],(2,4):['mountain',None,None],(2,5):['desert',None,None],(2,6):['desert',None,None],(2,7):['desert',None,None],
        (3,-3):['forest',None,None],(3,-2):['forest',None,None],(3,-2):['desert',None,None],(3,-1):['desert',None,None],(3,0):['swamp',None,['green','monument']],(3,1):['forest',None,['blue','monument']],(3,2):['mountain',None,None],(3,3):['mountain',None,None],(3,4):['water',None,None],(3,5):['water',None,None],(3,6):['desert',None,None],(3,7):['water',None,None],
        (4,-2):['forest',None,None],(4,-1):['desert','bear',None],(4,0):['desert','bear',None],(4,1):['water',None,None],(4,2):['water',None,None],(4,3):['forest',None,None],(4,4):['mountain','bear',['white','mountain']],(4,5):['water','bear',None],(4,6):['water',None,None],(4,7):['mountain',None,None],(4,8):['water',None,None],(4,9):['water',None,None],
        (5,-1):['forest','bear',None],(5,0):['water',None,None],(5,1):['water',None,None],(5,2):['swamp',None,None],(5,3):['forest',None,None],(5,4):['forest',None,None],(5,5):['water','bear',None],(5,6):['mountain',None,None],(5,7):['mountain',None,None],(5,8):['mountain',None,None],(5,9):['water',None,None],(5,10):['water',None,None],
        (6,0):['mountain',None,None],(6,1):['mountain',None,None],(6,2):['swamp',None,None],(6,3):['swamp',None,None],(6,4):['swamp',None,None],(6,5):['forest','jaguar',None],(6,6):['mountain','jaguar',None],(6,7):['swamp','jaguar',None],(6,8):['forest',None,None],(6,9):['forest',None,None],(6,10):['forest',None,None],
        (7,1):['mountain','bear',None],(7,2):['desert',None,['blue','hut']],(7,3):['swamp',None,None],(7,4):['forest',None,None],(7,5):['forest',None,None],(7,6):['water','jaguar',None],(7,7):['swamp','jaguar',None],(7,8):['swamp',None,None],(7,9):['forest',None,None],
        (8,2):['desert','bear',None],(8,3):['desert',None,None],(8,4):['desert',None,None],(8,5):['water',None,None],(8,6):['water',None,None],(8,7):['mountain',None,None],(8,8):['swamp',None,None],
        (9,3):['desert',None,None],(9,4):['desert',None,None],(9,5):['mountain',None,None],(9,6):['mountain',None,None],(9,7):['mountain',None,None],
        (10,4):['desert',None,None],(10,5):['desert',None,None],(10,6):['mountain',None,None],(11,5):['desert',None,None]}


hints1_3 = (('building color', 'white', 3), ('two zones', ('swamp', 'desert')), ('zone', 'water', 1))
'''пример для животных: ('animal', 'bear', 2)
   пример для типа строения: ('building type', 'hut', 3)'''

hints1_4 = (('two zones', ('forest', 'mountain')), ('two zones', ('mountain', 'water')), ('zone', 'forest', 1), ('zone', 'water', 1))

hints1_5 = (('zone', 'water', 1), ('zone', 'swamp', 1), ('two zones', ('desert', 'mountain')),
            ('two zones', ('water', 'mountain')), ('building color', 'green', 3))

hints2_3 = (('building color','white', 3),('building color','blue',3),('two zones', ('water','swamp')))
hints2_4 = (('zone', 'swamp', 1),('two zones', ('desert','mountain')),('zone','forest',1),('animal', 'bear',2))
hints2_5 = (('building color', 'white', 3),('two zones',('forest','water')),('two zones',('desert','water')),('zone','deser',1),('zone','mountain',1))

hints3_3 = (('zone','water',1),('building type', 'hut',2),('animal','jaguar',2))
hints3_4 = (('zone','mountain',1),('two zones','swamp','desert'),('zone','forest',1),('zone','water',1))
hints3_5 = (('zone','mountain',1),('two zones', ('desert','forest')),('zone','forest',1),('zone','water',1),('zone','desert',1))

hints4_3 = (('zone','desert',1),('two zones',('water','swamp')),('animal','jaguar',2))
hints4_4 = (('zone','desert',1),('animal','jaguar',2),('two zones',('desert','mountain') ),('zone','swamp',1))
hints4_5 = (('zone','mountain',1),('zone','desert',1),('two zones',('swamp','desert')),('zone','water',1),('building type','white',3))