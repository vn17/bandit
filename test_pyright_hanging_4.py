import scipy.optimize

res = scipy.optimize.minimize(
            distanceToPlane, 0, args=(), method="CG", bounds=[[0.01, 1], [-0.2, 0.2], [-0.05, 0.05]]
        )

def distanceToPlane(params):
        return 0
