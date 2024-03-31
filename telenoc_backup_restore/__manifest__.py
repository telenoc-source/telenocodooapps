# -*- coding: utf-8 -*-

{
  "name"                 :  "Tele Odoo Database Backup",
  "summary"              :  """Module provide feature to admin to take backups of his instance's database and later download them.""",  
  "category"             :  "Extra Tools",
  "version"              :  "1.0.1",
  "author"               :  "TeleNoc",
  "license"              :  "Other proprietary",
  "website"              :  "https://telenoc.org/",
  "description"          :  """Module provide feature to admin to take backups of his instance's database and later download them.""",
  "live_test_url"        :  "http://",
  "depends"              :  [
                             'base',
                            ],
  "data"                 :  [
                             'security/ir.model.access.csv',
                             'wizards/backup_deletion_confirmation_view.xml',
                             'data/backup_process_sequence.xml',
                             'views/backup_process.xml',
                             'data/backup_ignite_crone.xml',
                             'views/menuitems.xml',
                            ],
  "images"               :  ['static/description/banner.jpg'],
  "application"          :  True,
  "installable"          :  True,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
  "external_dependencies":  {'python': ['python-crontab', 'cssselect']},
}
