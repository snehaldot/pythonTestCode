def make_adder(addend):
    def adder(augend): return augend+addend
    return adder

p = make_adder(25)

print 'P : ', p(10) 
