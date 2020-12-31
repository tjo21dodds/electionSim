import numpy as np
import matplotlib.pyplot as plt




def genPop(numVoters, numViews, conFactor):
    conBias = genConBias(numVoters, numViews)
    conBias = conBias * conFactor
    pop = genNormMat(numVoters, numViews)
    pop = pop + conBias
    return pop
def genNormMat(height, width, norms = 3):
    i = []
    r = []
    for q in range(norms):
        i.append(((np.random.rand(width, height) - (0.5 * np.ones((width, height))))))
    for x in i:
        if len(r) == 0:
            r = x
        else:
            r = r + x
    return r / norms
def genParties(numParties, numViews):
    return genNormMat(numParties, numViews)

def genConBias(numViews, numVoters):
    row = 2*(np.random.rand(numViews) - (0.5 * np.ones((numViews))))
    mat = np.repeat([row], numVoters, axis=0)
    return mat

def euclidOpinion(numVoters, numViews, pop, parties):
    result = []
    for party in parties:
        partyMat = np.repeat([party], numVoters, axis=0)
        unitPop = pop - partyMat
        unitPop = unitPop * unitPop
        pRes = []
        for i in unitPop:
            pRes.append(np.sum(i))
        result.append(pRes)
    result = np.rot90(np.fliplr(result))
    return result

def firstPastThePost(numParties, ops):
    r = np.zeros(numParties)
    for i in ops:
        a = np.argmax(i)
        r[a] = r[a] + 1
    return r


def run(numVoters, numCons, conFactor, numParties, numViews):
    parties = genParties(numViews,numParties)
    national = []
    cons = []
    for i in range(numCons):
        a = euclidOpinion(numVoters, numViews, genPop(numViews, numVoters, conFactor), parties)
        if len(national) == 0:
            national = a
        else:
            national = np.concatenate((national, a), axis=0)
        cons.append(firstPastThePost(numParties,a))
        print((i/numCons)*100)
    national = firstPastThePost(numParties,national)
    national = national / numVoters
    cons = firstPastThePost(numParties,cons)

    fig, ax = plt.subplots()

    bWidth = 0.4

    x = np.arange(numParties)

    print(national)
    print(cons)
    b1 = ax.bar(x, national, width=bWidth, label="Proportional")
    b2 = ax.bar(x + bWidth,cons, width=bWidth, label="Constituency")

    ax.set_xticks(x + bWidth / 2)
    ax.set_xticklabels(x+1)

    ax.legend()

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')

    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')

    ax.set_xlabel('Party')
    ax.set_ylabel('Seats')

    ax.axhline(numCons/2, ls='--', color='r')
    fig.tight_layout()
    # plt.hist(genPop(numVoters, numViews, conFactor)[:,0])
    plt.show()
run(1000, 100, 0.7, 5, 10)
