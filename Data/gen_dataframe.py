from init_params import gen_bool_tup, gen_cat_dict, gen_list_dict
from gen_clusters import return_bool_cluster, \
                         return_cat_cluster, \
                         return_list_cluster, \
                         return_ord_cluster, \
                         return_date_cluster
from pandas import Series

# Initialize consistent parameters
bool_tup = gen_bool_tup()
cat_dict = gen_cat_dict()
list_dict = gen_list_dict()

# Merge all dicts to series for one sample
dating_series = Series({
    **return_bool_cluster(bool_tup),
    **return_cat_cluster(cat_dict),
    **return_list_cluster(list_dict),
    **return_ord_cluster(),
    **return_date_cluster()
})
