from myhdl import block, instance, Signal, intbv, delay
import random

from _74HC138 import _74HC138

random.seed(5)
randrange = random.randrange


@block
def test_74HC138():
    E1_N, E2_N, E3, A0, A1, A2, Y_N0, Y_N1, Y_N2, Y_N3, Y_N4, Y_N5, Y_N6, Y_N7 = [
        Signal(intbv(0)) for i in range(14)]
    # The initialization process of the three inputs, the eight outputs and the three activation lines.
    _74HC138_1 = _74HC138(E1_N, E2_N, E3, A0, A1, A2, Y_N0,
                          Y_N1, Y_N2, Y_N3, Y_N4, Y_N5, Y_N6, Y_N7)
    # the previously declared function is used in blocul test _74HC138

    @instance
    def stimulus():
        print("E1_N E2_N E3 A0 A1 A2 Y_N0 Y_N1 Y_N2 Y_N3 Y_N4 Y_N5 Y_N6 Y_N7")
        for i in range(9):  # the interval in which the inputs, outputs, selection and activation lines are calculated
            A0.next, A1.next, A2.next, E1_N.next, E2_N.next, E3.next = randrange(2), randrange(2), randrange(2), \
                randrange(2), randrange(2), randrange(2)
            # signals A0,A1,A2,E1_N,E2_N,E3 change their values ​​depending on the random values
            yield delay(10)
            print(" %s     %s  %s  %s  %s   %s   %s    %s    %s    %s    %s    %s    %s    %s" %
                  (E1_N, E2_N, E3, A0, A1, A2, Y_N0, Y_N1, Y_N2, Y_N3, Y_N4, Y_N5, Y_N6, Y_N7))
            # displaying the final values ​​of activation, input and output signals specific to the decoder/demultiplexer

    return _74HC138_1, stimulus


'''we return the previously declared function in the test_74HC138 block for the decoder/demultiplexer, 
where all the possible combinations of input signals, activation and output lines, having random values'''

# test bench
tb = test_74HC138()
tb.config_sim(trace=True)
tb.run_sim()
