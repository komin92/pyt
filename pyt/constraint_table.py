"""Global lookup table for constraints.

Uses cfg node as key and operates on bitvectors in the form of ints."""

constraint_table = dict()

from pyt.utils.log import enable_logger, logger
enable_logger(to_file='./pyt.log')


def initialize_constraint_table(cfg_list):
    """Collects all given cfg nodes and initializes the table with value 0."""
    for cfg in cfg_list:
        constraint_table.update(dict.fromkeys(cfg.nodes, 0))


def constraint_join(cfg_nodes):
    """Looks up all cfg_nodes and joins the bitvectors by using logical or."""
    r = 0
    for e in cfg_nodes:
        r = r | constraint_table[e]
    return r


def print_table(lattice):
    print('Constraint table:')
    for k, v in constraint_table.items():
        logger.debug("[Flux] k is %s and v is %s and bin(v) is %s", k, v, bin(v))
        # logger.debug("[Flux] k is %s", k)
        print(str(k) + ': ' + ','.join([str(n) for n in lattice.get_elements(v)]))
