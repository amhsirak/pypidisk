import os
import pkg_resources
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--size", help="Get size of package in KB or MB", type=str, default="KB", required=False, choices=["KB", "MB"])
args = vars(ap.parse_args())

def get_package_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

dists = [d for d in pkg_resources.working_set]

for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = get_package_size(path)
        if size/1000 > 1.0:
            if args["size"] == "KB":
                print (f"{dist}: {size/1000} KB")
            elif args["size"] == "MB":
                print (f"{dist}: {size/1000000:.2f} MB")
            print("-"*40)
    except OSError:
        '{} does not exist. Please check and try again later.'.format(dist.project_name)