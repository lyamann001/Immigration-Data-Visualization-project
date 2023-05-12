# Immigration-Data-Visualization-project
Immigrant rates per year in Canada
Dataset: Immigration to Canada from 1980 to 2013 - International migration flows to and from selected countries - The 2015 revision from United Nation's website. The dataset contains annual data on the flows of international migrants as recorded by the countries of destination. The data presents both inflows and outflows according to the place of birth, citizenship or place of previous / next residence both for foreigners and nationals. The focus is on Canadian Immigration data.

The Result of Bar Graph

![cubukGrap](https://github.com/lyamann001/Immigration-Data-Visualization-project/assets/60852845/9dca2497-4fdd-45fb-9cb5-1920e37d3834)

The Result of Area Graph


![alan grafigi](https://github.com/lyamann001/Immigration-Data-Visualization-project/assets/60852845/2b0c7615-a7ed-4706-a9f9-bba5db481114)


The Results of HIstograms

#histogram
count, bin_edges = np.histogram(df_can["2013"])
print(count)
print(bin_edges)

df_can["2013"].plot(
    kind="hist",
    figsize=(10, 7),
    xticks=bin_edges,
    color='b'
)

plt.title("Histogram of Immigration from 195 Countries in 2013")
plt.ylabel("Number of Countries")
plt.xlabel("Number of Immigrant")
plt.grid(True)
plt.show()

![histogram_dataVS1](https://github.com/lyamann001/Immigration-Data-Visualization-project/assets/60852845/6c25ce41-e489-4e74-a3f3-de6f3a6e9d9e)

![Histogram_DataVs](https://github.com/lyamann001/Immigration-Data-Visualization-project/assets/60852845/aa46871e-550f-44e5-8e3b-9cec9bbd468d)

The Results of Pie Chart
![pie](https://github.com/lyamann001/Immigration-Data-Visualization-project/assets/60852845/9cfd2765-8bd1-4d8e-8eae-530ccbdf26a7)


The Result of Scatter Chat
![dagilim](https://github.com/lyamann001/Immigration-Data-Visualization-project/assets/60852845/baacd688-d664-4fd3-909f-49705f28cb0c)

