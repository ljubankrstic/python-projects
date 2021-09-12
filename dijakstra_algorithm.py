# Moja primjena Dijakstrinog algoritma
'''To je algoritam za nalazenje najkraceg puta izmedju dva cvora u tezinskom grafu
Primjenjuje se u raznim oblicima u drugacije svrhe. Najbolji primjer je opcija nalazenja udaljenosti u Google mapama'''

'''Prvo napravimo klasu za cvor liste
   value - Vrijednost koju cvor sadrzi
   travel - Najkraci put do datog cvora ( dole vidi objasnjenje kako njime manipulisemo )
'''


class Node:
    def __init__(self, val, trav):
        self.value = val
        self.travel = trav


'''Ovdje cemo definisati cvorove ( primjeti beskonacne vrijednosti )'''
nodeA = Node("A", float("inf"))
nodeB = Node("B", float("inf"))
nodeC = Node("C", float("inf"))
nodeD = Node("D", float("inf"))
nodeE = Node("E", float("inf"))

'''
   Graf predstavimo pomocu liste susjeda ( dict gdje su cvorovi kljucevi, a susjedi vrijednosti)
   Imaj na umu da je ovo tezinski usmjereni graf
'''
adj_list = {
    nodeA: [(nodeB, 4), (nodeC, 1)],
    nodeB: [(nodeD, 1)],
    nodeC: [(nodeB, 2), (nodeD, 5)],
    nodeD: [(nodeE, 3)],
    nodeE: []
}

'''Da ne bismo stvorili infinite loop error koristimo rjecnik koji pazi da li je cvor posjecen'''

reconstruct_dict = {
    nodeA: False,
    nodeB: False,
    nodeC: False,
    nodeD: False,
    nodeE: False
}


'''
    Nakon sto nadjemo duzinu najkraceg puta izmedju dva cvora, trebamo da rekonstruisemo put kojim smo se kretali.
    U tu svrhu pravimo rjecnik gdje su kljucevi cvorovi a vrijednosti cvor koji smo zadnje presli na najkracem putu to tog cvora.
    Inicijaliziramo sa None
'''
reconstruct_dict = {
    nodeA: None,
    nodeB: None,
    nodeC: None,
    nodeD: None,
    nodeE: None
}

'''
    Funkcija koja ce sa zadanim pocetkom i krajem da rekonstruise najkraci put nakon sto glavna funkcija odradi svoj deo
'''


def reconstruct(start, end):
    t = []
    curr = end
    while curr:
        t.append(curr)
        curr = reconstruct_dict[curr]
    t.reverse()
    for i in range(len(t)):
        # NAPOMENA: kondicional sam postavio samo da bi rezultat bio citko ispisan( da ne bude uznemirujuca strelica na kraju)
        if i < len(t)-1:
            print(t[i].value, end="->")
        else:
            print(t[i].value)


'''Funkcija koja primjenjuje algoritam'''


def solve(start, end, adj_list):
    # udaljenost startnog cvora od samog sebe je 0, pa je i postavimo na 0
    start.travel = 0
    # za iterovanje kroz sve cvorove ja cu koristiti BFS prilaz problemu, tako moramo da kreiramo kju ( queue)
    queue = [start]
    while len(queue) > 0:
        # trenutni cvor na kome radimo je uzet za pocetka liste( u listi je uklonjen)
        curr = queue.pop(0)
        for i in adj_list[curr]:
            queue.append(i[0])
            if curr.travel+i[1] < i[0].travel:
                i[0].travel = curr.travel+i[1]
                reconstruct_dict[i[0]] = curr
        '''NAPOMENA: mozda sam mogao da u while loop postavim break condition tako da izadjemo iz loopa kada odredimo najkraci put do
           kraja, ali posto je ovo samo demonstracija, ostavio sam ovako'''
    reconstruct(start, end)


solve(nodeA, nodeE, adj_list)
'''----------------------------------------ZAVRSNA NAPOMENA---------------------------------------------------
   Ovo nije najefikasniji nacin da se primjeni algoritam ( npr. kada na gugl mapi trazis udaljenost izmedju Broca i Tuzle,
   ne zanima te udaljenost izmedju Broca i Konga), ali smatram da je dovoljno za ovu moju malu prezentaciju. Postoje i ostale varijante kao npr.
   A* algoritam.'''