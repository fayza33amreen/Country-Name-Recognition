#!/usr/bin/env python3

import sys
import python.aggregate_data
import python.cluster_data
import python.distance_calculate
import python.read_from_googlesheet
import python.write_to_googlesheet


# from aggregate_data import DataAggregator
# from cluster_data import DataCluster
# from distance_calculate import DistanceCalculator
# from read_from_googlesheet import GooglesheetReader
# from write_to_googlesheet import GooglesheetWritter


def main():
    reader = python.read_from_googlesheet.GooglesheetReader()
    reader.read()

    python.aggregate_data.DataAggregator()
    # DataAggregator()
    python.cluster_data.DataCluster()
    # DataCluster()
    python.distance_calculate.DistanceCalculator()
    # DistanceCalculator()
    python.write_to_googlesheet.GooglesheetWritter()
    # GooglesheetWritter()


if __name__ == '__main__':
    main()
