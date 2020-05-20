import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.axes_grid1 import make_axes_locatable
from gpsearch.core import latexify, Arrow3D


matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.size'] = 10


def plot_observable(t, x, ylabel=None, filename=None,
                    xticks=None, yticks=None, close=True):

    fig = plt.figure(figsize=(3.0,1.6), constrained_layout=True)
    fig.set_constrained_layout_pads(w_pad=0, h_pad=0)
    ax = plt.axes()
    plt.plot(t, x, color='k', lw=1)
    plt.xlabel("$t$")
    if ylabel is None:
        plt.ylabel("$g$")
    else:
        plt.ylabel("$" + ylabel + "$")
    if xticks is not None:
        plt.xlim(xticks[0], xticks[-1])
        ax.set_xticks(xticks)
        ax.set_xticklabels(latexify(xticks))
    if yticks is not None:
        plt.ylim(yticks[0], yticks[-1])
        ax.set_yticks(yticks)
        ax.set_yticklabels(latexify(yticks))
    ax.yaxis.set_label_coords(-0.12,0.5)
    ax.tick_params(direction='in', length=2)
    if filename is None:
        filename = "obs.pdf"
    plt.savefig(filename)
    if close:
        plt.close()


def plot_indicator(t_o, x_o, t_i, x_i, ylabel=None, filename=None,
                   xticks=None, yticks=None, close=True):

    fig = plt.figure(figsize=(1.8,1.4), constrained_layout=True)
    fig.set_constrained_layout_pads(w_pad=0, h_pad=0)
    ax = plt.axes()
    plt.plot(t_o, x_o, color="k", lw=0.75)
    plt.plot(t_i, x_i, color="#e41a1c", lw=0.75)
    plt.xlabel("$t$")
    if ylabel is None:
        plt.ylabel("$g$")
    else:
        plt.ylabel("$" + ylabel + "$")
    if xticks is not None:
        plt.xlim(xticks[0], xticks[-1])
        ax.set_xticks(xticks)
        ax.set_xticklabels(latexify(xticks))
    if yticks is not None:
        plt.ylim(yticks[0], yticks[-1])
        ax.set_yticks(yticks)
        ax.set_yticklabels(latexify(yticks))
    ax.yaxis.set_label_coords(-0.23,0.5)
    ax.tick_params(direction='in', length=2)
    if filename is None:
        filename = "ind.pdf"
    plt.savefig(filename)
    if close:
        plt.close()



def plot_trajectory(t, u, filename=None, close=True):

    fig = plt.figure(figsize=(1.7,1.6))
    ax = fig.add_axes([0.03, -0.02, 1.0, 1.0], projection="3d")
    ax.grid(False)
    ax.axis("off")
    ax.view_init(elev=15, azim=45)
    ax.plot(u[:,0], u[:,1], u[:,2], color="C0", lw=0.2)
    for aa in [ax.xaxis, ax.yaxis, ax.zaxis]:
        aa.pane.set_edgecolor("black")
        aa.pane.set_alpha(0)
        aa.pane.fill = False
    arrow_prop_dict = dict(mutation_scale=10, arrowstyle="->", \
                           shrinkA=0, shrinkB=0, color="k")
    arx = Arrow3D([0, 2.5], [0, 0], [0, 0], **arrow_prop_dict)
    ary = Arrow3D([0, 0], [0, 2.5], [0, 0], **arrow_prop_dict)
    arz = Arrow3D([0, 0], [0, 0], [0, 1.1], **arrow_prop_dict)
    for a in [arx, ary, arz]:
        ax.add_artist(a)
    ax.add_artist(a)
    ax.set_xlim(-1.5, 1.0)
    ax.set_ylim(-1.25, 1.25)
    ax.set_zlim(0, 0.85)
    ax.text(2.75, 0, 0, r"$x$", ha="center", va="center")
    ax.text(0, 2.75, 0, r"$y$", ha="center", va="center")
    ax.text(0, 0, 1.18, r"$z$", ha="center", va="center")
    if filename is None:
        filename = "traj.pdf"
    plt.savefig(filename)
    if close:
        plt.close()


def plot_dangermap(u, mu, cmapticks=None, filename=None, close=True):

    fig = plt.figure(figsize=(1.7,2.0))
    ax = fig.add_axes([0.03, 0.1, 1.0, 0.88], projection="3d")
    ax.grid(False)
    ax.axis("off")
    ax.view_init(elev=15, azim=45)
    cax = fig.add_axes([0.1, 0.12, 0.8, 0.03])
    if cmapticks is not None:
        im = ax.scatter3D(u[:,0], u[:,1], u[:,2], marker='o', linewidths=0,
                          s=0.3, c=mu, alpha=1, cmap="plasma", 
                          vmin=cmapticks[0], vmax=cmapticks[-1])
        cbar = plt.colorbar(im, cax=cax, orientation="horizontal", 
                            ticks=cmapticks)
        cbar.ax.set_xticklabels(latexify(cmapticks))
    else:
        im = ax.scatter3D(u[:,0], u[:,1], u[:,2], marker='o', linewidths=0,
                          s=0.3, c=mu, alpha=1, cmap="plasma")
        cbar = plt.colorbar(im, cax=cax, orientation="horizontal")
    cbar.ax.tick_params(length=2)
    for aa in [ax.xaxis, ax.yaxis, ax.zaxis]:
        aa.pane.set_edgecolor("black")
        aa.pane.set_alpha(0)
        aa.pane.fill = False
    arrow_prop_dict = dict(mutation_scale=10, arrowstyle="->", \
                           shrinkA=0, shrinkB=0, color="k")
    arx = Arrow3D([0, 2.5], [0, 0], [0, 0], **arrow_prop_dict)
    ary = Arrow3D([0, 0], [0, 2.5], [0, 0], **arrow_prop_dict)
    arz = Arrow3D([0, 0], [0, 0], [0, 1.1], **arrow_prop_dict)
    for a in [arx, ary, arz]:
        ax.add_artist(a)
    ax.add_artist(a)
    ax.set_xlim(-1.5, 1.0)
    ax.set_ylim(-1.25, 1.25)
    ax.set_zlim(0, 0.85)
    ax.text(2.75, 0, 0, r"$x$", ha="center", va="center")
    ax.text(0, 2.75, 0, r"$y$", ha="center", va="center")
    ax.text(0, 0, 1.18, r"$z$", ha="center", va="center")
    if filename is None:
        filename = "dngr.pdf"
    plt.savefig(filename)
    if close:
        plt.close()


