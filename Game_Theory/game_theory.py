import math
import numpy as np


class game_theory_analisys():
    """Class that makes Game Theory analysis """

    def pay_off_matrix(self,a,g,m,c,i,o,e,k,q,
                                b,h,n,d,j,p,f,l,r):

        """Fills the empty matrix with game conditions"""

        player_one = np.array([[a, b, c],
                               [d, e, f],
                               [g, h, i]])

        player_two = np.array([[j, k, l],
                               [m, n, o],
                               [p, q, r]])

        pay_off_matrix = np.stack((x, y), axis=2)

        return pay_off_matrix

    def Iesde(self, pay_off_matrix):

        """Implements Elimination of Strickly Dominated Strategies"""

        for i in pay_off_matrix:

            if pay_off_matrix[0][0][i] > pay_off_matrix[0][0][i+1]:
                new_pay_off = np.delete(pay_off_matrix,0,i) #TODO:->TEST
            if pay_off_matrix[i][0][0] > pay_off_matrix[i+1][0][0]:
                new_pay_off = np.delete(new_pay_off,i,0) #-TODO:->TEST

        return new_pay_off


    def best_response(self,pay_off_matrix):


        return best_tuples


    def nash_equilibrium(self,pay_off_matrix):

        return nashed_tuples


if __name__ == '__main__':
    MyClass():
    MyClass.method(matrix)
