"""
Parses a newick tree file, ladderizes it, and returns it as a string.
"""
import argparse
from dendropy import Tree

def parse_newick( tree_loc: str ) -> str:
    """
    Loads a newick tree, ladderizes it, and returns it as a newick string.
    Basically just a wrapper around dendropy.Tree.get() so that we get error handling, type checking, etc. for free
    """
    tree = Tree.get( path=tree_loc, preserve_underscores=True, schema="newick" )
    tree.ladderize()
    tree_string = tree.as_string( schema="newick" ).strip()
    tree_string = tree_string.replace( "'", "" )
    return tree_string

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse a newick file to string object')
    parser.add_argument('--tree', help='location of newick file')
    args = parser.parse_args()
    output = parse_newick( tree_loc=args.tree )
