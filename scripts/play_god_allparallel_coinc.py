# +
from grb_shader import GodMultiverse
from dask.distributed import LocalCluster, Client

from cosmogrb.instruments.gbm import GBM_CPL_Constant_Universe


if __name__ == '__main__':

    # path where simulations are stored
    sim_path = "/data/eschoe/grb_shader/sims/20231120_t90ghirlanda2016_wideralphadistr_newcosmogrb_inc/spatial_coinc/"
    # path of parameter file
    #param_file = "ghirlanda2016_c_normal.yml"
    param_file = "ghirlanda2016_c_normal_inc.yml"

    n_cores = 10
    n_sims = 1000
    #n_sims = 500

    constant_temporal_profile = True
    catalog_selec = True
    internal_parallelization = True
    hard_flux_selec = False
    save_det_grbs_as_fits = True

    with LocalCluster(n_workers=n_cores,threads_per_worker=1,dashboard_address=':8792') as cluster:
        with Client(cluster) as client:
            print(client)
            
            print('Create population')

            multiverse = GodMultiverse(n_sims)
            #multiverse.process_surveys(surveys_path = sim_path,client=client)
            print('go')
            multiverse.go(
                param_file=param_file,
                pops_dir=sim_path,
                constant_temporal_profile=constant_temporal_profile,
                client=client,
                catalog_selec=catalog_selec,
                hard_flux_selec=hard_flux_selec,
                internal_parallelization=internal_parallelization
                )

    print('Successfully done')
