"""
Copyright (c) 2008 Denis Bzowy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

http://code.activestate.com/recipes/576564-walkers-alias-method-for-random-objects-with-diffe/
"""
from __future__ import division
import random

__author__ = "Denis Bzowy"
__version__ = "16nov2008"

class Walkerrandom:
  """ Walker's alias method for random objects with different probablities
  """

  def __init__( self, weights, keys=None ):
    """ builds the Walker tables prob and inx for calls to random().
        The weights (a list or tuple or iterable) can be in any order;
        they need not sum to 1.
    """
    n = self.n = len(weights)
    self.keys = keys
    sumw = sum(weights)
    prob = [w * n / sumw for w in weights]  # av 1
    inx = [-1] * n
    short = [j for j, p in enumerate( prob ) if p < 1]
    long = [j for j, p in enumerate( prob ) if p > 1]
    while short and long:
        j = short.pop()
        k = long[-1]
        # assert prob[j] <= 1 <= prob[k]
        inx[j] = k
        prob[k] -= (1 - prob[j])  # -= residual weight
        if prob[k] < 1:
            short.append( k )
            long.pop()
    self.prob = prob
    self.inx = inx

  def __str__( self ):
    """ e.g. "Walkerrandom prob: 0.4 0.8 1 0.8  inx: 3 3 -1 2" """
    probstr = " ".join([ "%.2g" % x for x in self.prob ])
    inxstr = " ".join([ "%.2g" % x for x in self.inx ])
    return "Walkerrandom prob: %s  inx: %s" % (probstr, inxstr)

#...............................................................................
  def random( self ):
    """ each call -> a random int or key with the given probability
        fast: 1 randint(), 1 random.uniform(), table lookup
    """
    u = random.uniform( 0, 1 )
    j = random.randint( 0, self.n - 1 )  # or low bits of u
    randint = j if u <= self.prob[j] \
        else self.inx[j]
    return list(self.keys)[randint] if self.keys \
        else randint

