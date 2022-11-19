import os
import pkg_resources

def get_package_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
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
            print (f"{dist}: {size/1000} KB")
            print("-"*40)
    except OSError:
        '{} no longer exists'.format(dist.project_name)