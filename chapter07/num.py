
class Number:

    def __init__(self, pre):
        self.pre = pre

    def succ(self):
        return Number(self)

    def __eq__(self, right):
        return (self - right) is zero

    def __sub__(self, right):
        r = self
        while 1:
            if right is zero:
                break
            if r is zero:
                if right is not zero:
                    raise ValueError("Nagive isn't support")
                break
            r = r.pre
            right = right.pre
        return r

    def __add__(self, right):
        r = self
        while 1:
            if right is zero:
                break
            r = r.succ()
            right = right.pre
        return r

    def __mul__(self, right):
        if right is zero:
            return zero
        if right.pre is zero:
            return self
        r = self
        while 1:
            if right.pre is zero:
                break
            r = r + self
            right = right.pre
        return r

    def __int__(self):
        i = 0
        r = self
        while 1:
            if r is zero:
                return i
            i += 1
            r = r.pre

    def __str__(self):
        return str(int(self))

    def __repr__(self):
        return 'Number(%d)' % int(self)


class Zero(Number):
    def __init__(self):
        pass
    def __str__(self):
        return 'zero'
    def __repr__(self):
        return 'zero'
    def __int__(self):
        return 0

zero = Zero()


if __name__ == '__main__':
    one = zero.succ()
    two = one + one
    three = one + two
    four = two * two
    five = three + two
    six = five.succ()
    ten = four + three * two

    print('one - one = %s' % (one - one))
    print('ten - one = %s' % (ten - one))
    print('ten == two * five ? %s' % (ten == two * five))
    print('six - one == ten - five ? %s' % (six - one == ten - five))
