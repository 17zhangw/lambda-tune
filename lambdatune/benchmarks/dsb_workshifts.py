from pkg_resources import resource_listdir, resource_filename


def get_dsb_queries(workshift):
    query_files = resource_listdir("lambdatune.benchmarks", f"resources/queries/dsb_workshifts/{workshift}")

    queries = [(d.replace(".sql", ""), open(resource_filename("lambdatune.benchmarks", f"resources/queries/dsb_workshifts/{workshift}/{d}")).read()) for d in query_files]
    queries = sorted(queries, key=lambda k: k[0])

    return queries
