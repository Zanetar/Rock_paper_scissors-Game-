from random import *
import random

class Game:
    def __int__(self,name,level):
        self.name=name
        self.level=level


class Rock_paper_scissors(Game):
    def __int__(self, name,level):
        super().__init__(name,level)

    def __repr__(self):
        return('Gra znajdź liczbę. Dowiedz się jaką cyfrę wylosował komputer')


    def rules(self):
        print('Witaj w grze KAMIEŃ,NOŻYCZKI,PAPIER')
        print('W każdej turze gracz wybiera jeden z symboli:' 
              'kamień '
              'nozyczki '
              'papier. ')
        print('Nastepnie komputer dokonuje własnego wyboru. '
              'Nastepuje konfrontacja symboli. ')
        print('Gracz, który pokazał silniejszy symbol otrzymuje punkt. '
              'W przypadku dwóch tych samych symboli mastępuje remis. ')
        print('Wygrywa gracz, który jako pierwszy zdobędzie 3 punktyt.'
              'Powodzenia!')


    def exit(self):
        exit=int(input('Czy chcesz zagrać w grę? 1-T,0-N'))
        return exit

    def game(self):
        user_points=[]
        comp_points=[]
        while True:
            sum_user=sum(user_points)
            sum_comp=sum(comp_points)
            if sum_user==3 and sum_comp<3:
                print('Wygrałeś grę GRATULACJE')
                break
            elif sum_comp==3 and sum_user<3:
                print('Przegrałeś grę. Zagraj jeszcze raz!')
                break
            elif sum_comp==3 and sum_user==3:
                print('REMIS!')
                break
            print('Wybierz właściwy symobl:')
            try:
                choose=int(input('dla nożyczek wybierz 1, dla kamienia wybierz 2, dla papieru wybierz 3'))
                if choose == 1:
                    print('Wybrałeś nożyczki')
                elif choose == 2:
                    print('Wybrałeś kamień')
                elif choose == 3:
                    print('Wybrałeś papier')
                else:
                    print ('Wybrałeś zły znak!')
                    break
                print('Następuje losowanie przez komputer...')
                choose_comp = randint(1, 3)
                if choose_comp == 1:
                    print('Komputer wylosował nożyczki')
                    if choose==choose_comp:
                        print('REMIS')
                        user_points.append(1)
                        comp_points.append(1)
                    elif choose==3:
                        print('PRZEGRAŁEŚ')
                        comp_points.append(1)
                    elif choose==2:
                        print('WYGRAŁEŚ')
                        user_points.append(1)
                elif choose_comp==2:
                    print('Komputer wylosował kamień')
                    if choose==choose_comp:
                        print('REMIS')
                        user_points.append(1)
                        comp_points.append(1)
                    elif choose==3:
                        print('WYGRAŁEŚ')
                        user_points.append(1)
                    elif choose==1:
                        print('PRZEGRAŁEŚ')
                        comp_points.append(1)
                elif choose_comp==3:
                    print('Komputer wylosował papier')
                    if choose==choose_comp:
                        print('REMIS')
                        user_points.append(1)
                        comp_points.append(1)
                    elif choose==1:
                        print('WYGRAŁEŚ')
                        user_points.append(1)
                    elif choose==2:
                        print('PRZEGRAŁEŚ')
                        comp_points.append(1)
                else:
                    print('WYBRAŁEŚ ZŁY ZNAK')
            except: print('WYBRAŁEŚ ZŁY ZNAK')

def menu_rock(object):
    try:
        while True:
            object.rules()
            object.game()
            a=object.exit()
            if a==0:
                print('Dziękujemy za grę')
                break
            elif a==1:
                pass
            elif a !=1 and a !=0:
                print('Wybrałeś zły znak.Jeżeli chcesz zagrać, to ponownie uruchom grę!!')
                break
    except: print('Wybrałeś zły znak. Jeżeli chcesz zagrać, to ponownie uruchom grę!!')

first_game=Rock_paper_scissors()

menu_rock(first_game) #wywołanie programu




