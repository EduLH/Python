from depth_first_search.graph import Vertex
from depth_first_search.graph import DirectedAdjList
from depth_first_search.depth_first_search import DepthFirstSearch
from depth_first_search.utils import GraphReader
from depth_first_search.utils import OutputWriter

import sys
import threading

def main():

    fname_read = input("Entre o caminho: ")
    fname_read = fname_read.strip()
    if len(fname_read) < 1: fname_read = "files/input/input.txt"

    fname_write = input("Entre com o caminho para o output: ")
    fname_write = fname_write.strip()
    if len(fname_write) < 1: fname_write = "files/output/output.txt"

    adj_list = DirectedAdjList()
    graph_reader = GraphReader(adj_list, fname_read)
    graph_reader.read()

    output_before_dfs = str(adj_list)

    dfs = DepthFirstSearch(adj_list)

    # metodo recursivo
    dfs.dfs_recursive()
    output_res_recursion = str(adj_list)


    adj_list.initialize_vertices()

    # metodo iterativo
    dfs.dfs_iterative()
    output_res_iteration = str(adj_list)

    output_writer = OutputWriter(fname_write)

    output_writer.write("Grafo antes da busca:\n")
    output_writer.write(output_before_dfs)
    output_writer.write("\n")

    output_writer.write("Grafo depois da busca:\n")
    output_writer.write(output_res_recursion)
    output_writer.write("\n")

    output_writer.write("Grafo depois da busca interativa:\n")
    output_writer.write(output_res_iteration)
    output_writer.write("\n")

    print("")
    print("Completo!")
    output_str = "Veja o output no arquivo \"{_path_to_file}\"".format(_path_to_file = fname_write)
    print(output_str)

if __name__ == "__main__":
    main()
