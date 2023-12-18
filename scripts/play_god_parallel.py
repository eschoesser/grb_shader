# +
from grb_shader import GodMultiverse
from dask.distributed import LocalCluster, Client

from cosmogrb.instruments.gbm import GBM_CPL_Constant_Universe
# -

if __name__ == '__main__':

    # path where simulations are stored
    sim_path = "/ptmp/eschoe/sims/20231218_test/"
    # path of parameter file
    param_file = "ghirlanda2016_c_normal.yml"

    n_cores = 40
    n_sims = 10

    constant_temporal_profile = True
    catalog_selec = False
    internal_parallelization = True
    hard_flux_selec = False

    with LocalCluster(n_workers=n_cores,threads_per_worker=1) as cluster:
        with Client(cluster) as client:
            print(client)
            
            print('Start simulations')

            multiverse = GodMultiverse(n_sims)
            #multiverse.process_surveys(surveys_path = sim_path,client=client)

            multiverse.go(
                param_file=param_file,
                pops_dir=sim_path,
                client=client,
                constant_temporal_profile=constant_temporal_profile,
                catalog_selec=catalog_selec,
                hard_flux_selec = hard_flux_selec,
                internal_parallelization=internal_parallelization
                )

            print('Successfully done')
