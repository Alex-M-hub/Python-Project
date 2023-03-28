from myhdl import block, always_comb


@block
def _74HC138(E1_N, E2_N, E3, A0, A1, A2, Y_N0, Y_N1, Y_N2, Y_N3, Y_N4, Y_N5, Y_N6, Y_N7):
    # Our function consists of three inputs, three activation lines and eight outputs, as we define it
    """Demultiplexer with 3 lines and 8 outputs

    E1_N,E2_N,E3 -- represent the activation lines; he notation is chosen E1_N because 
    the activation line is negated (N comes from negated), the language used, Python,
    it conditions us to change the notations in order to represent them.
    A0,A1,A2 -- represent the inputs of the decoder/demultiplexer
    Y_N0,Y_N1,Y_N2,Y_N3,Y_N4,Y_N5,Y_N6,Y_N7 - represent the outputs of the decoder/demultiplexer;
    the notation is chosen Y_N0 because the output is negated (N comes from negated), the language used, Python,
    it conditions us to change the notations in order to represent them.
    """
    A = [A0, A1, A2]
    Y_N = [Y_N0, Y_N1, Y_N2, Y_N3, Y_N4, Y_N5, Y_N6, Y_N7]

    @always_comb
    def comb():
        if E1_N == 0 and E2_N == 0 and E3 == 1:
            for i in range(3):
                for j in range(8):
                    Y_N[j].next = A[i]
        else:
            for j in range(8):
                Y_N[j].next = True

    return comb
