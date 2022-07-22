import pandas as pd
import pygal
from sklearn.cluster import DBSCAN
import numpy as np

#from IPython.display import display, HTML


class MLCode(object):
    """
    def testing(self):

        dataFrame = pd.read_json("MOCK_DATA.json")
        dataFrame.head()

        disp_dict = {}
        for index, row in dataFrame.iterrows():
            if row['User'] not in disp_dict.keys():
                disp_dict[row['User']] = [(row['Latitude'], row['Longitude'])]
            else:
                disp_dict[row['User']].append((row['Latitude'], row['Longitude']))

        xy_chart = pygal.XY(stroke=False)
        [xy_chart.add(k,v) for k,v in sorted(disp_dict.items())]
        display(HTML(base_html.format(rendered_chart=xy_chart.render(is_unicode=True))))

        #formula 3281 feet=1 kilometre
        safe_distance =0.0018288 

        model = DBSCAN(eps=safe_distance, min_samples=2, metric='haversine').fit(dataFrame[['Latitude', 'Longitude']])
        core_samples_mask = np.zeros_like(model.labels_, dtype=bool)
        core_samples_mask[model.core_sample_indices_] = True
        labels = model.labels_
        dataFrame['Cluster'] = model.labels_.tolist()


        disp_dict_clust = {}
        for index, row in dataFrame.iterrows():
            if row['Cluster'] not in disp_dict_clust.keys():
                disp_dict_clust[row['Cluster']] = [(row['Latitude'], row['Longitude'])]
            else:
                disp_dict_clust[row['Cluster']].append((row['Latitude'], row['Longitude']))

        #print(len(disp_dict_clust.keys()))
        from pygal.style import LightenStyle
        dark_lighten_style = LightenStyle('#F35548')
        xy_chart = pygal.XY(stroke=False, style=dark_lighten_style)
        [xy_chart.add(str(k),v) for k,v in disp_dict_clust.items()]
        display(HTML(base_html.format(rendered_chart=xy_chart.render(is_unicode=True))))


        inputName = "William"
        inputNameClusters = set()
        for i in range(len(dataFrame)):
            if dataFrame['User'][i] == inputName:
                inputNameClusters.add(dataFrame['Cluster'][i])
        #print(inputNameClusters)



        infected = set()
        for cluster in inputNameClusters:
            if cluster != -1:
                namesInCluster = dataFrame.loc[dataFrame['Cluster'] == cluster, 'User']
                for i in range(len(namesInCluster)):
                    name = namesInCluster.iloc[i]
                    if name != inputName:
                        infected.add(name)
        #print(infected)

"""
    def contactTracing(self, user, file):
        #Check if name is valid

        dataFrame = pd.read_json(file)
        dataFrame.head()
        inputName=user
        
        assert (inputName in dataFrame['User'].tolist()), "User Doesn't exist"
        
        #Social distance
        safe_distance = 0.0018288 #6 feets in kilometers
        
        #Apply model, in case of larger dataset or noisy one, increase min_samples
        model = DBSCAN(eps=safe_distance, min_samples=2, metric='haversine').fit(dataFrame[['Latitude', 'Longitude']])
        
        #Get clusters found bt the algorithm 
        labels = model.labels_
        
        #Add the clusters to the dataframe
        dataFrame['Cluster'] = model.labels_.tolist()
        
        #Get the clusters the inputName is a part of
        inputNameClusters = set()
        for i in range(len(dataFrame)):
            if dataFrame['User'][i] == inputName:
                inputNameClusters.add(dataFrame['Cluster'][i])
        #print(inputName," is a part of clusters:")
        #print(inputNameClusters)
    #Get people who are in the same cluster as the inputName              
        infected = set()
        for cluster in inputNameClusters:
            if cluster != -1: #as long as it is not the -1 cluster
                namesInCluster = dataFrame.loc[dataFrame['Cluster'] == cluster, 'User'] #Get all names in the cluster
                for i in range(len(namesInCluster)):
                #locate each name on the cluster
                    name = namesInCluster.iloc[i]
                    if name != inputName: #Don't want to add the input to the results
                        infected.add(name)
        #print("Potential infections are:",*infected,sep="\n" )

        return inputNameClusters,*infected


