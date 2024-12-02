# Plot your city’s Roads and Railways
### Video Demo:  https://youtu.be/LnOIQfZ6HUc
### Description:
The project is entitled “Plot you City’s Roads and Railways”, osmnx and networkx python libraries were used to plot a graph which contains the roads and railways of a provided address, the program takes an address, geocode it  to a geographic point and then plot a graph with the roads and railways in a radius of 10 Kilometers from the geocoded point.
The program contains 4 functions : 
#### verify_address() : 
verify if the provided address has a specific requirement, the address must contains at least the city and the country name seperated by a comma "," so in this function we split the provided address by a comma and count the length of the resulted list, it must be greater than or equal to 2.
#### download_data() : 
download the data required to plot the graphs, it uses osmnx library to download OSM data, we have used the osmnx function graph_from_address, this function takes the address provided by the user as an argument, it takes also the **distance** argument which we specified it to 10 kilometers, the **distance type** argument; we specified it to be "bbox" so all of the roads and railways will be included, the **custom filter** argument in which we specify the type of network we want to download **roads** and **railways**
#### make_graph() : 
uses the downloaded data to make the graph, we have used the networkx compose library to make a single graph from the downloaded data from the previous function
#### plot_graph() : 
uses the graph made in the make_graph function to plot it to the user
