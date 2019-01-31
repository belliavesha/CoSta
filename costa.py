from numpy import exp, log, sin, cos, pi, zeros
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
ax.set_title( 'scale: {:<.2e}'.format(1.0) )
plt.subplots_adjust(left=0.25, bottom=0.25)
l, = plt.plot([1], [0], 'r.')
plt.axis([-1, 1, -1, 1])

axrlz = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='gray')
axilz = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='grey')
axN = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='green')
slrlz =  Slider(axrlz, 'Re(ln(z))', -pi, pi, valinit=0.)
slilz =  Slider(axilz, 'Im(ln(z))', -pi, pi, valinit=0.)
slN =  Slider(axN, 'lg(N)', 0., 4, valinit=2.)


def update(val):
    rlz = slrlz.val
    ilz = slilz.val
    N = int(exp(slN.val*log(1e1)))
    tr, ti = .0,0.
    m = 0.
    xd, yd = zeros((N,)),  zeros((N,))
    for i in range(N):
        tre = exp(tr)
        tic, tis = cos(ti), sin(ti)
        tr = rlz*tre*tic-ilz*tre*tis 
        if tr>m: m = tr
        ti = (ilz*tre*tic+rlz*tre*tis)%(2*pi)
        xd[i]=tre*tic
        yd[i]=tre*tis 
    sc = exp(m)
    l.set_data(xd/sc, yd/sc)
    ax.set_title( 'scale: {:<.2e}'.format(sc) )
    fig.canvas.draw_idle()
slrlz.on_changed(update)
slilz.on_changed(update)
slN.on_changed(update)

plt.show()
