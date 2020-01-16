from butlersgrail.manage_cluster import ManageAuroraCluster as mc

from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description='Check setup and dependency init for RDS jobs')
    parser.add_argument('--list_clusters', action='store_true',
                        default=False, help='Skip creating snapshots')
    parser.add_argument('message', metavar='test_return_message', type=str, nargs='+')
    options = parser.parse_args()

    prod_clusters = mc.getClustersByTag(mc.getClusters(), "realm", "prod")

    if options.list_clusters:
        print("Iterating over prod clusters")
        for cluster in prod_clusters:
            print("Cluster {} present...".format(cluster))

    if options.message:
        print("Command line echo message provided, see:")
        print(options.message)
