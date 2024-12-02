from project import verif_address
from project import download_data
from project import make_graph
import networkx as nx
import pytest


def test_verif_address():
    with pytest.raises(ValueError) as excinfo:
        verif_address("Manouba Tunisia")

def test_download_data():
    assert(len(download_data("Manouba, Tunisia")) == 2)
    assert(type(download_data("Manouba, Tunisia")[1]) == nx.classes.multidigraph.MultiDiGraph)


def test_make_graph():
    G1, G2 = download_data("Manouba, Tunisia")
    assert(type(make_graph(G1,G2)) == nx.classes.multidigraph.MultiDiGraph)