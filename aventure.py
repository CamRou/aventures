#!/usr/bin/python

def perso_nom():
    print("Bienvenue aventurier! Je suis Patapé, l'aide de camp qui vous suivra à travers les nombreuses péripéties"""
          """à venir.""")
    nom = input("Comment dois-je vous appeler?\n")
    return(nom)
nom = perso_nom()
print(nom+" , plutôt joli. Entrons dans le vif du sujet: ce pourquoi vous êtes ici!")
print("""Le seigneur local vous a engagé pour lui apporter une potion. Après des jours de voyages à travers la région"""
      """à la recherche de ladite potion, vous êtes enfin à l'auberge qui se trouve à l'entrée de la forêt entourant"""
      """le château.""")
print("Après une bonne nuit de sommeil, il est temps de livrer la potion du seigneur.")

def choix_depart():
    choix_depart =  input("On y va?(oui/non)\n")
    return(choix_depart)
reponse1 = choix_depart()
if reponse1 == "oui":
    print("C'est parti!\n")
else:
    print("Bon bah tant pis restez à l'auberge, moi je vais livrer la potion et la récompense sera à moi.")
    raise Exception("Peut-être la prochaine fois...")

class Node(object):
    """
        Concrete class for elements of the storyline.

        This class implemtents all the data strutures and the
        methods useful to implement a tree of narrative elements
        such as the ones that can be found in gamebooks.

        :param description: Describe the situation.
        :param question: How to resolve the situation.
        :param answer: The various resolutions to the question.
        :type description: str
        :type question: str
        :type alternatives: list
        :type answer: list
    """
    
    def __init__(self, description, question, alternatives, answer):
        self.description = description
        self.question = question
        self.alternatives = alternatives
        self.answer = answer
        self.choice = None
        self.children = []
    def __call__(self):
        print(self.description)
        input_line = self.question
        i = 0
        for alternative in self.alternatives:
            i += 1
            input_line = input_line+'\n'+str(i)+") "+alternative+'\n'
        self.choice = int(input(input_line))
        self.choice -= 1
        print(self.answer[self.choice])
        self.children[self.choice]()
        
auberge = Node("""En sortant de l'auberge, vous vous trouvez face à la vaste forêt qu'il vous faudra"""
             """traverser pour vous rendre au château du seigneur. Rien d'affreux, mais j'espère que"""
             """vous avez pris un bon petit-déjeuner. Deux chemins s'offrent à vous. Tous deux sont"""
             """bordés de buissons, tous les deux s'enfoncent dans la forêt. Rien ne les différencie"""
             """vraiment, il va falloir faire appel à votre instinct d'aventurier.""",
             "Vous préférez aller à droite ou à gauche?",
             ["droite","gauche"],
             ["À droite toute!","À gauche alors."])
noeud_1 = Node("""Après un moment sur le chemin qui partait de l'auberge, vous arrivez à un nouvel"""
               """embranchement. Deux voies possibles, et au milieu un poteau portant le nom de ce qui"""
               """semble être le nom des voies. La première se dirige vers l'est et s'appelle P. Pair,"""
               """l'autre continue vers le sud et porte le nom de Tugh Alère.""",
               nom+", vous préférez aller vers l'est ou vers le sud?",
               ["Est","Sud"],
               ["Suivons donc le chemin P. Pair.","Suivons donc le chemin Tugh Alère."])
noeud_2 = Node("""Le chemin que vous suiviez s'est transformé en route de briques jaunes. Vous continuez"""
               """pendant quelques minutes avant de vous trouver face à un nouvel embranchement. D'un côté"""
               """un éventail usé par les intempéries vous pointe la direction du sud, de l'autre une statuette"""
               """en forme de singe ailé vous invite à suivre l'ouest.""",
               nom+"vous préférez l'éventail ou le singe ailé?",
               ["Éventail","Singe ailé"],
               ["Suivons donc l'avis de l'homme de paille.","Suivons donc l'avis de cette belle statuette."])
noeud_3 = Node(nom+""", attention! Des sables mouvants! Forcément à regarder les petits oiseaux et pas où"""
               """on va, ce genre de choses arrive! Heureusement ça ne devrait pas être difficile de vous en sortir."""
               """Vous pouvez agripper la racine qui est sur votre gauche, essayer d'atteindre les branches basses du"""
               """buisson à votre droite, ou vous laisser flotter en espérant que ça fasse quelque chose.""",
               """Donc? La racine, le buisson ou se laisser flotter?""",
               ["Racine","Buisson","Flotte"],
               ["""Elle a l'air de tenir... Accrochez vous, vous êtes presque sorti.""",
                """Je crois que j'ai entendu quelque chose craquer""",
                """Ça marche, qui l'aurait cru. Bon vous avez du sable partout, mais on peut continuer."""])
noeud_4 = Node("""Un fumet familier chatouille votre nez... Ça sent la bouffe! Vous pouvez même distinguer quoi exactement,"""
               """tellement l'odeur est puissante: en face ça sent la viande rouge cuite à la perfection, à droite c'est le"""
               """parfum inimitable de votre gâteau préféré. """+nom+""" , c'est votre ventre que j'entends gargouiller?""",
               """Bon du coup, vous préférez aller voir du côté de la viande ou du gâteau?""",
               ["Viande","Gâteau"],
               ["""Vous croyez qu'il y en aura pour moi?""",
                """J'espère qu'il y aura aussi des cupcakes."""])
noeud_5 = Node("""Vos pieds se bloquent soudainement et vous ne pouvez plus avancer, pour une bonne raison: des racines se"""
               """sont enroulées autour de vos chevilles!""",
               """Pour vous dégager, vous arrachez les racines, vous les brûlez ou vous essayez de les démêler doucement?""",
               ["On arrache","On crâme tout","On y va en douceur"],
               ["""La sève qui s'échappe des racines vous brûle un peu la peau mais rien de bien grave. Malheureusement"""
                """les autres racines barrent un passage et vous devez suivre l'autre chemin.""",
                """Ça n'a pas l'air de lui plaire et les racines se resserent un peu plus, remontant sur vos jambes. Heureusement"""
                """elles finissent par céder et vous pouvez continuer.""",
                """Les racines finissent par se tasser d'elles-mêmes d'un côté et vous laissent l'accès à un passage."""])
noeud_6 = Node("""Vous arrivez devant un grand panneau, mais le temps et le manque d'entretien font qu'il est presque illisible."""
               """Vous arrivez à distinguer les directions, mais pas ce à quoi elles mènent.""",
               """Nord, sud, est ou ouest?""",
               ["Nord","Sud","Est","Ouest"],
               ["""Pourquoi pas! Allons-y!""",
                """Ce chemin a l'air sympa, en espérant qu'il vous emmènera au bon endroit.""",
                """Il y a un peu de boue par terre, mais rien de très grave.""",
                """Une petite pause le temps de reprendre votre souffle et vous reprenez la route."""])
noeud_7 = Node("""Vous arrivez dans une clairière d'où partent plusieurs chemins, mais impossible de savoir lequel vous amènera"""
               """le plus rapidement au château du seigneur. Vous décidez de laisser la chance choisir: vous tendez le bras, fermez"""
               """les yeux et faites plusieurs tours sur vous-même pour désigner une direction.""",
               """Combien de tours vous faites exactement?""",
               ["Trois","Cinq","Neuf","Douze"],
               ["""Vous avez un peu le tournis mais ça va, et vous continuez votre chemin.""",
                """Un peu chancelant, vous avancez dans la direction désignée.""",
                """Vous vous sentez un peu mal, peut-être à cause des tours... Mais vous avez un chemin et une destination à atteindre.""",
                """Vous vous vautrez lamentablement et n'arrivez pas à vous remettre debout tout de suite. Après quelques minutes vous"""
                """reprenez la route, mais vous avez un peu mal au coeur."""])
noeud_8 = Node("""Vous entendez un râle étrange suivi de bruits de raclements, comme si on trainait quelque chose par terre. Un rayon de"""
               """soleil transperce la frondaison et vous vouyez devant vous un cadavre...sauf qu'il bouge et s'approche de vous. À quelques"""
               """pas de vous, il se met à geindre un mot: cerveau.""",
               """Vous décidez de lui mettre un bon coup dans le crâne, vous fuyez vite avant qu'il ne s'approche trop ou vous essayez"""
               """d'entamer la discussion?""",
               ["Combat","Fuite","Discussion"],
               ["""Le cadavre essaie vaguement d'esquiver mais ne fait que se ruer sur votre poing avant de s'effondrer par terre.""",
                """L'avantage c'est qu'il ne va pas bien vite et mettra du temps à vous rattraper.""",
                """Après vous avoir lancé un regard vide de toute expression, il vous demande si vous n'avez pas de la ficelle pour son"""
                """cerf-volant."""])
noeud_9 = Node("""Vous arrivez dans une petite clairière et la première chose que vous remarquez"""
               """est une marmite. L'odeur de viande vient de ce qui se trouve dedans, mais maintenant"""
               """que vous êtes plus prêt, elle a quelque chose de...dérangeant. Vous vous rapprochez"""
               """pour voir ce qui s'y trouve quand une vieille dame apparait. Elle dit s'appeler Annie"""
               """Bhal et vous propose un plein bol de ce qui se trouve dans la marmite avec un sourire un"""
               """peu inquiétant.""",
               "Vous l'acceptez?",
               ["Oui","Non"],
               ["""Ça a vraiment un goût bizarre, même si ce n'est pas mauvais non plus... Jusqu'à ce qu'elle"""
                """vous dise qu'il s'agit du dernier aventurier passé dans le coin. Vous fuyez vite et loin"""
                """d'elle, peu importe la direction.""",
                """Vraiment ça ne vous dit rien qui vaille. Vous vous éloignez lentement d'elle et, une fois assez"""
                """loin, retournez dans la forêt."""])
noeud_10 = Node("""Hum... Il semble que les fans d'un auteur à succès soient passés par là. Le carrefour où vous vous êtes"""
                """arrêté est rempli d'objets divers et variés, mais tous sur le même thème, chacune des issues est gardée"""
                """par une personne à l'air sévère et tous ont le regard rivé sur un trône fait d'épées au centre du carrefour."""
                """Quand vous approchez, leurs voix résonnent à l'unisson pour quelques mots: L'hiver vient.""",
                """Vous répondez quoi à ça """+nom+"""? Vous savez comment ces gens peuvent être... D'un côté il y a une réponse"""
                """basique et passe-partout - CMB - mais vous pouvez aussi avoir un avis, à savoir: lions, dragons, loups ou démons.""",
                ["CMB, évidemment","Lions","Dragons","Loups","Démons"],
                ["""Ouais j'aurais dit pareil, éventuellement complété d'un DTC... Ça a pas l'air de leur plaire, mais ils décident"""
                 """de vous ignorer pour partir dans un énième débat sur qui est le plus fort.""",
                 """Celui qui tient l'étendard rouge et or vous fait un grand sourire et vous laisse passer.""",
                 """Une jolie blonde platine vous fait un sourire un poil aguicheur et vous laisse passer.""",
                 """Un vent froid s'engouffre soudainement dans vos cheveux et le brun qui tient l'étendard à la tête de loup vous"""
                 """laisse passer.""",
                 """Le silence tombe brutalement, avant que tous se mettent à chuchoter en vous jetant des regards suspicieux. Du"""
                 """coup vous prenez le premier chemin qui vient et partez vite."""])
noeud_11 = Node("""Une créature immense vous barre la route et brandit sa massue dans votre direction! """+nom+""", c'est un"""
               """troll, et pas un petit en plus! Vous pourriez passer entre ses jambes, ou profiter de sa lenteur pour vite"""
               """le contourner.""",
               """Que faites-vous?""",
               ["Passer en dessous","Le contourner"],
               ["""C'est passé de justesse, mais vous aurez du mal à effacer de votre esprit ce que vous avez vu sous son pagne.""",
                """C'était juste, vous sentez l'air déplacé par sa massue secouer vos cheveux mais vous ne vous attardez pas."""])
noeud_12 = Node("""Alors que vous vous demandiez quelle direction choisir à un nouveau croisement, une licorne sort des fourrés"""
                """et s'arrête au milieu du chemin. Une licorne oui, d'un blanc immaculé, et vous avez même l'impression qu'un"""
                """arc-en-ciel la surplombe. C'est pas tout les jours qu'on voit une créature légendaire, vous devez avoir une bonne"""
                """étoile au dessus de votre tête """+nom+""". Mais faut pas oublier que ça vaut une petite fortune les cornes de ces"""
                """machins.""",
                """Vous l'attaquez pour récupérer sa corne et la revendre plus tard ou vous vous approchez doucement pour lui"""
                """faire un calin?""",
                ["Attaque","Calin"],
                ["""Je crois que ça lui a pas plu, elle vous charge! Vite, courrez!""",
                 """Oh c'est mignon! Et elle a l'air d'aimer en plus! Du coup elle vous dirige du museau vers un chemin et vous fait"""
                 """un bisou pailleté avant de disparaitre."""])
noeud_13 = Node("""Au détour du chemin, vous vous retrouvez face à une boite bleue avec une porte, qui est entrouverte. N'écoutant"""
                """que votre courage, vous entrez, pour vous apercevoir qu'elle est beaucoup plus grande à l'intérieur qu'à"""
                """l'extérieur. Vous vous approchez de la console centrale, et l'envie vous prend d'actionner l'un des bidules s'y"""
                """trouvant pour voir ce que ça fait.""",
                """Il y a un bouton qui clignotte, un levier rouge, une manette qui tourne, un genre de tableau avec des étoiles,"""
                """et un bitoniau bizarre. Vous touchez à quoi?""",
                ["Bouton","Levier","Manette","Tableau","Bitoniau"],
                ["""Tout se met à trembler...""","""Il y a un bruit bizarre, comme si on aspirait l'air.""",
                 """La colonne centrale se met à radier.""","""Les étoiles bougent et prennent la forme d'une baguette.""",
                 """Vous avez l'impression qu'un courant traverse votre corps quand vous y touchez."""])
noeud_14 = Node("""Au détour du chemin, vous entendez quelqu'un vous appeler. Il s'agit d'un petit garçon et il a l'air perdu. Il"""
                """vous demande votre aide pour retrouver son chemin vers l'auberge, en échange il vous indiquera celui qui sera le"""
                """plus simple vers le château du seigneur.""",
                """Vous l'aidez?""",
                ["Oui, évidemment","Bon allez, soyons sympa avec le mioche","Vous lui montrez vaguement une direction","Non, qu'il se débrouille"],
                ["""Vous lui pointez du doigt le chemin d'où vous venez, en lui disant de faire attention, et il vous montre un sentier"""
                 """qui a l'air assez sûr.""",
                 """Vous désignez un chemin un peu à contre-coeur, mais il parait qu'il faut aider son prochain, surtout les gamins.""",
                 """Vous faites un bref signe de tête qui ne doit pas beaucoup l'aider et il vous lance un regard mauvais avant de partir. """,
                 """Vous le dépassez sans même un regard en arrière et il vous lance un caillou. Pas fort, mais c'est pas agréable non plus."""])
noeud_15 = Node("""Vous alliez faire un pas de plus quand une flèche se plante à vos pieds. À quelques mètres à peine une archère"""
                """elfe vous défie du regard et vous bloque le passage. Elle est très belle, comme tous ceux de sa race, mais semble"""
                """aussi assez douée avec son arc.""",
                """Là c'est comme vous le sentez"""+nom+""". Vous pouvez lui faire un peu de gringue pour qu'elle vous laisse passer"""
                """, lui demander directement son aide, la provoquer en duel ou laisser libre cours à votre haine des elfes.""",
                ["Drague","Aide","Provocation","Insultes"],
                ["""Pas sûr que ce soit la bonne option, elle a l'air de le prendre assez mal et dégaine une nouvelle flèche. Vous"""
                 """partez vite avant de vous la prendre dans la tronche.""",
                 """Un bref sourire et elle vous montre un chemin dissimulé dans la verdure.""",
                 """Euh...Depuis quand elle a une épée? Vite, prenez à gauche avant que ça tourne mal.""",
                 """C'était pas une bonne idée, mais alors pas du tout! Elle se rue sur vous avec un cri guerrier et manque de vous"""
                 """embrocher, mais vous évitez de justesse et vous mettez à courir."""])
noeud_16 = Node("""Une chanson s'élève et vous vous rendez compte que ce sont les fleurs tout autour de vous qui chantent. Vous écoutez"""
                """donc et attendez qu'elles aient terminé pour leur demander votre chemin. Chacune y va de son conseil, mais les avis"""
                """d'une rose, un lys, une pâquerette et un chrysanthème sortent du lot.""",
                """Qui préférez-vous écouter?""",
                ["Rose","Lys","Pâquerette","Chrysanthème"],
                ["""Elle vous conseille un chemin un peu à l'écart.""",
                 """Il vous indique un passage entre deux arbres que vous n'aviez pas remarqué.""",
                 """Elle vous désigne un chemin qui serpente à travers les buissons.""",
                 """Il vous montre un chemin discret mais qui a l'air sûr."""])
noeud_17 = Node("""Un petit lapin blanc surgit des bois et s'arrête au milieu du chemin. Il est mignon à remuer son petit nez"""
                """, mais vous avez aussi entendu parlé d'une légende parlant d'une terrible créature prenant un aspect innofensif.""",
                """Vous vous approchez ou vous utilisez la Sainte Grenade que vous avez eu la présence d'esprit d'emporter avec vous?""",
                ["Approche","Sainte Grenade"],
                ["""Tout va bien, c'est un lapin normal. Vous en profitez pour faire quelques papouilles dans sa fourrure duveteuse"""
                 """avant de continuer.""",
                 """Un, deux trois et.... BOOM! Plus de lapin, plein de morceaux éparpillés partout, et une armée de lapins surgit"""
                 """des fourrés pour venger leur congénère."""])
noeud_18 = Node("""Depuis le temps que vous errez dans cette forêt, vous voulez pas faire une petite pause? Installez vous contre un arbre"""
                """, posez-vous, fermez les yeux, je vous réveillerais. * une heure plus tard * Euh...Patron? Vous allez rire, je me suis"""
                """endormi aussi et j'ai oublié d'où on était venu. Et vu qu'il y a plusieurs chemins possibles...""",
                """À gauche, à droite ou en face?""",
                ["Gauche","Droite","En face"],
                ["""Vraiment désolé patron, promis ça se reproduira plus.""",
                 """Vraiment désolé patron, promis ça se reproduira plus.""",
                 """Vraiment désolé patron, promis ça se reproduira plus."""])
noeud_19 = Node("""Vous avez l'impression que la forêt se fait moins dense, peut-être parce que le château n'est pas loin. Mais c'est"""
                """peut-être aussi à cause de la réunion des Ents de la région, vous avez vu une affiche il y a quelques temps. Vous"""
                """remarquez des trâces de roues dans le sol.""",
                """Vous pensez qu'on peut mieux suivre dans la boue, là où c'est sec, ou vous voulez voir les Ents?""",
                ["Boue","Sec","Ents"],
                ["""Il a plu récement et les traces sont bien nettes, ce sera facile à suivre.""",
                 """Vous suivez ce qui ressemble à une route, la boue a bien gardé la trace des roues.""",
                 """Les traces attendront, c'est pas tous les jours qu'on peut voir des Ents."""])
noeud_20 = Node("""Des tours, des douves, un pont-levis... Vous êtes arrivé au château du seigneur! Bravo! Vous vous présentez à la porte"""
                """et un serviteur vous emmène jusqu'au seigneur qui vous remercie et vous donne un sac de pièces d'or.""",
                """Content d'avoir terminé cette quête?""",
                ["Oui","Non"],
                ["""C'était vraiment sympa, il faudra se refaire ça un de ces jours """+nom+"""!""",
                 """On s'en refera une autre plus tard, promis!"""])

auberge.children = [noeud_1, noeud_2]
noeud_1.children = [noeud_4, noeud_3]
noeud_2.children = [noeud_3, noeud_5]
noeud_3.children = [noeud_4, noeud_6, noeud_2]
noeud_4.children = [noeud_8, noeud_3]
noeud_5.children = [noeud_2, noeud_6, noeud_7]
noeud_6.children = [noeud_3, noeud_8, noeud_10, noeud_7]
noeud_7.children = [noeud_5, noeud_6, noeud_10, noeud_11]
noeud_8.children = [noeud_6, noeud_9, noeud_12]
noeud_9.children = [noeud_10, noeud_13]
noeud_10.children = [noeud_9, noeud_13, noeud_14, noeud_7, noeud_6]
noeud_11.children = [noeud_7, noeud_14]
noeud_12.children = [noeud_13, noeud_15]
noeud_13.children = [noeud_9, noeud_12, noeud_10, noeud_16, noeud_15]
noeud_14.children = [noeud_11, noeud_10, noeud_16, noeud_17]
noeud_15.children = [noeud_12, noeud_13, noeud_18, noeud_19]
noeud_16.children = [noeud_13, noeud_18, noeud_14, noeud_17]
noeud_17.children = [noeud_16, noeud_20]
noeud_18.children = [noeud_16, noeud_19, noeud_20]
noeud_19.children = [noeud_15, noeud_18, noeud_20]

auberge()
