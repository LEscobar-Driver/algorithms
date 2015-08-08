import unittest
from ..data_structure import stack,queue,union_find,union_find_by_rank,union_find_with_path_compression, digraph

class TestStack(unittest.TestCase):
    """
    Test Stack Implementation
    """
    def test_stack(self):
        self.sta = stack.stack()
        self.sta.add(5)
        self.sta.add(8)
        self.sta.add(10)
        self.sta.add(2)

        self.assertEqual(self.sta.remove(),2)
        self.assertEqual(self.sta.is_empty(),False)
        self.assertEqual(self.sta.size(),3)
        
class TestQueue(unittest.TestCase):
    """
    Test Queue Implementation
    """
    def test_queue(self):
        self.que = queue.queue()
        self.que.add(1)
        self.que.add(2)
        self.que.add(8)
        self.que.add(5)
        self.que.add(6)

        self.assertEqual(self.que.remove(),1)
        self.assertEqual(self.que.size(),4)
        self.assertEqual(self.que.remove(),2)
        self.assertEqual(self.que.remove(),8)
        self.assertEqual(self.que.remove(),5)
        self.assertEqual(self.que.remove(),6)
        self.assertEqual(self.que.is_empty(),True)

class TestUnionFind(unittest.TestCase):
    """
    Test Union Find Implementation
    """
    def test_union_find(self):
        self.uf = union_find.UnionFind(4)
        self.uf.make_set(4)
        self.uf.union(1, 0)
        self.uf.union(3, 4)

        self.assertEqual(self.uf.find(1), 0)
        self.assertEqual(self.uf.find(3), 4)
        self.assertEqual(self.uf.is_connected(0, 1), True)
        self.assertEqual(self.uf.is_connected(3, 4), True)

class TestUnionFindByRank(unittest.TestCase):
    """
    Test Union Find Implementation
    """
    def test_union_find_by_rank(self):
        self.uf = union_find_by_rank.UnionFindByRank(6)
        self.uf.make_set(6)
        self.uf.union(1, 0)
        self.uf.union(3, 4)
        self.uf.union(2, 4)
        self.uf.union(5, 2)
        self.uf.union(6, 5)

        self.assertEqual(self.uf.find(1), 1)
        self.assertEqual(self.uf.find(3), 3)
        # test tree is created by rank
        self.uf.union(5, 0)
        self.assertEqual(self.uf.find(2), 3)
        self.assertEqual(self.uf.find(5), 3)
        self.assertEqual(self.uf.find(6), 3)
        self.assertEqual(self.uf.find(0), 3)

        self.assertEqual(self.uf.is_connected(0, 1), True)
        self.assertEqual(self.uf.is_connected(3, 4), True)
        self.assertEqual(self.uf.is_connected(5, 3), True)

class TestUnionFindWithPathCompression(unittest.TestCase):
    """
    Test Union Find Implementation
    """
    def test_union_find_with_path_compression(self):
        self.uf = union_find_with_path_compression.UnionFindWithPathCompression(5)
        self.uf.make_set(5)
        self.uf.union(0, 1)
        self.uf.union(2, 3)
        self.uf.union(1, 3)
        self.uf.union(4, 5)
        self.assertEqual(self.uf.find(1), 0)
        self.assertEqual(self.uf.find(3), 0)
        self.assertEqual(self.uf.parent(3), 2)
        self.assertEqual(self.uf.parent(5), 4)
        self.assertEqual(self.uf.is_connected(3, 5), False)
        self.assertEqual(self.uf.is_connected(4, 5), True)
        self.assertEqual(self.uf.is_connected(2, 3), True)
        # test tree is created by path compression
        self.uf.union(5, 3)
        self.assertEqual(self.uf.parent(3), 0)

        self.assertEqual(self.uf.is_connected(3, 5), True)


class TestDirectedGraph(unittest.TestCase):
    """
    Test Undirected Graph Implementation
    """
    def test_directed_graph(self):

        # init
        self.dg0 = digraph.Digraph()
        self.dg1 = digraph.Digraph()
        self.dg2 = digraph.Digraph()
        self.dg3 = digraph.Digraph()

        # populating
        self.dg1.add_edge(1, 2)
        
        self.dg2.add_edge(1,2)
        self.dg2.add_edge(1,2)

        self.dg3.add_edge(1,2)
        self.dg3.add_edge(1,2)
        self.dg3.add_edge(3,1)
         
        # test adj
        self.assertTrue(2 in self.dg1.adj(1))
        self.assertEqual(len(self.dg1.adj(1)), 1)
        self.assertTrue(1 not in self.dg1.adj(2))
        self.assertEqual(len(self.dg1.adj(2)), 0)

        self.assertTrue(2 in self.dg2.adj(1))
        self.assertEqual(len(self.dg2.adj(1)), 2)
        self.assertTrue(1 not in self.dg2.adj(2))
        self.assertEqual(len(self.dg2.adj(2)), 0)

        self.assertTrue(2 in self.dg3.adj(1))
        self.assertTrue(1 in self.dg3.adj(3))
        self.assertEqual(len(self.dg3.adj(1)), 2)
        self.assertTrue(1 not in self.dg3.adj(2))
        self.assertEqual(len(self.dg3.adj(2)), 0)
        self.assertTrue(3 not in self.dg3.adj(1))
        self.assertEqual(len(self.dg3.adj(3)), 1)

        # test degree
        self.assertEqual(self.dg1.outdegree(1), 1)
        self.assertEqual(self.dg1.outdegree(2), 0)
        self.assertEqual(self.dg2.outdegree(1), 2)
        self.assertEqual(self.dg2.outdegree(2), 0)
        self.assertEqual(self.dg3.outdegree(1), 2)
        self.assertEqual(self.dg3.outdegree(2), 0)
        self.assertEqual(self.dg3.outdegree(3), 1)
        
        # test vertices
        self.assertEqual(self.dg0.vertices(), [])
        self.assertEqual(len(self.dg0.vertices()), 0)

        self.assertTrue(1 in self.dg1.vertices())
        self.assertTrue(2 in self.dg1.vertices())
        self.assertEqual(len(self.dg1.vertices()), 2)

        self.assertTrue(1 in self.dg2.vertices())
        self.assertTrue(2 in self.dg2.vertices())
        self.assertEqual(len(self.dg2.vertices()), 2)

        self.assertTrue(1 in self.dg3.vertices())
        self.assertTrue(2 in self.dg3.vertices())
        self.assertTrue(3 in self.dg3.vertices())
        self.assertEqual(len(self.dg3.vertices()), 3)

        # test vertex_count
        self.assertEqual(self.dg0.vertex_count(), 0)
        self.assertEqual(self.dg1.vertex_count(), 2)
        self.assertEqual(self.dg2.vertex_count(), 2)
        self.assertEqual(self.dg3.vertex_count(), 3)
        
        # test edge_count
        self.assertEqual(self.dg0.edge_count(), 0)
        self.assertEqual(self.dg1.edge_count(), 1)
        self.assertEqual(self.dg2.edge_count(), 2)
        self.assertEqual(self.dg3.edge_count(), 3)

        print(self.dg1)


