import math
import numpy as np
import json
from sklearn.decomposition import PCA

times = sum([[str(year) + "-" + month for month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]] for year in range(2003, 2022)], [])

def run(file, accuracy=0.9):
    data = json.load(open(file))
    rows = [(x, [float(data[x][i]) if i in data[x] else "NaN" for i in times]) for x in data.keys()]
    cols = [x[0] for x in rows]
    newr = []
    for i in range(len(rows[0][1])):
        point = []
        add = True
        for j in range(len(rows)):
            if rows[j][1][i] != "NaN" and not math.isnan(rows[j][1][i]):
                point.append(rows[j][1][i])
            else:
                add = False
                break
        if add:
            newr.append(point)
    rows = None
    inp = np.array(newr)
    pca = PCA(n_components=accuracy)
    pca.fit(inp)
    raw = pca.components_
    out = [[(cols[j], raw[i][j]) for j in range(len(raw[i]))] for i in range(len(raw))]
    visual = [sorted(outi, key=lambda x:-math.fabs(x[1])) for outi in out]
    out = [dict(x) for x in out]
    # Open a file with access mode 'a'
    file_object = open('axis.txt', 'a')
    for visuals in visual:
        # Append 'hello' at the end of file
        file_object.write(str(visuals))
        file_object.write("\n\n")
        print(visuals)
    # Close the file
    file_object.write("\n\n\n")
    file_object.close()
    print(pca.explained_variance_ratio_)
    print(sum(pca.explained_variance_ratio_))
    print(len(pca.explained_variance_ratio_))
    print("******")
    return out
