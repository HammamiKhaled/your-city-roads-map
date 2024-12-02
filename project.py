import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx

ox.settings.use_cache=True
ox.settings.log_console=True

#print(ox.__version__)

def main():
    address = input("Where are you from ? (provide at least your district and country name)\n")
    verif_address(address)
    G1, G2 = download_data(address)
    G = make_graph(G1, G2)
    plot_graph(G, address)
    


def verif_address(adr):
    l = adr.split(", ")
    if (len(l)<2):
        raise ValueError
    return adr

def download_data(address):
    town_roads = ox.graph_from_address(address, dist =10000, dist_type="bbox", retain_all=True, custom_filter='["highway"]')
    town_rails = ox.graph_from_address(address, dist =10000, dist_type="bbox", retain_all=True, custom_filter='["railway"]')
    return (town_roads, town_rails)

def make_graph(G1, G2):
    return (nx.compose(G1, G2))

def plot_graph(G, address):
    ec = ['y' if 'highway' in d else 'r' for _, _, _, d in G.edges(keys=True, data=True)]
    fig, ax = ox.plot_graph(G, bgcolor='k', edge_color=ec, node_size=0, edge_linewidth=0.5, show=False, close=False)

    plt.title("Roads and Railways in "+address)
    plt.show()


if __name__ == "__main__":
    main()