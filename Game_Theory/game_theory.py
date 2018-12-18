import math 
import numpy as np



class game_theory_analisys:


    def create_payoff_matrix(self, list_1,list_2):

    """ Creates pay-off matrix

        player_one = np.array([[a,b,c],
                               [d,e,f],
                               [g,h,i]])

        player_two = np.array([[j,k,l],
                               [m,n,o],
                               [p,q,r]])

    """

        list_1 = [[a,b,c],[d,e,f],[g,h,i]]
        list_2 = [[j,k,l],[m,n,o],[p,q,r]]

        player_one = np.asarray(list_1)
        player_two = np.asarray(list_2)

        pay_off_matrix = np.stack((player_one,player_two), axis=2)

        return pay_off_matrix

    def IESD(self, player_one, player_two):

    """ Iterated elimination of strickly dominated environment """


        #PLAYER 1
        "Eliminate unecessary columns"
        if player_two[:,0].all() > player_two[:,1].all():
            np.delete(player_two[:,1])
        if player_two[:,1].all() > player_two[:,2].all():
            np.delete(player_two[:, 1])


        #PLAYER 2
        "Eliminate unecessary rows"
        if player_one[0].all() > player_two[1].all():
            np.delete(player_two[1])
        if player_one[1].all() > player_two[2].all():
            np.delete(player_two[2])

        np.stack((player_one,player_two), axis=2)


    def best_response(self,pay_off_matrix):

        """Isolate the player strategy and figure
        out what the other player responds to that strategy"""

        #BEST RESPONSE OF PLAYER ONE

        best_response_player_one = []
        for i in player_two[:,i]:
            if max(player_two[:,i]):
                best_response_player_one.append(i)

        #BEST RESPONSE OF PLAYER TWO

        best_response_player_two = []
        for i in player_one[i]:
            if max(player_one[i]):
                best_response_player_two.append(i)

        return best_tuples


    def nash_equilibrium(self,pay_off_matrix):

        return nashed_tuples


if __name__ == '__main__':
    MyClass():
    MyClass.method(matrix)
