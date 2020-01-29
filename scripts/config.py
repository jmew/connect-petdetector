
class AMLConfig:
    pass

AMLConfig.workspace_name           = 'jemew-workspace'
AMLConfig.experiment_name          = 'jemew-experiment'
AMLConfig.resource_group           = 'jemew-rg'
AMLConfig.compute_name             = 'jemew-compute'
AMLConfig.training_script_filename = 'train.py'
AMLConfig.scoring_script_filename  = 'score.py'
AMLConfig.subscription_id          = 'b856ff87-00d1-4205-af56-3af5435ae401'
AMLConfig.storage_account_name     = 'jemewstorage'
AMLConfig.storage_account_key      = 'DVAu3B1/BrNblhJ2PAhfUCWzWpSZPh+HG1/pBCOoelvSiVKYkrk2bBSjzuldjVU9UTLQF1KwW/DA69dsYK0eBg=='
AMLConfig.datastore_name           = 'jemewdatastore'
AMLConfig.container_name           = 'default'
AMLConfig.images_dir               = 'images'

AML = AMLConfig()
