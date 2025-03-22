Ventor Base
===========

|

**Base module that allow relation between Ventor modules**

Change Log
##########

|

* 13.0.2.1.0 (2025-xx-xx)
    - Added the settings "Show description from product" to the Warehouse Operations, Batch Picking, Cluster Picking menus

* 13.0.1.8.0 (2024-08-21)
    - Updated the description for the 'Set qty to zero' settings in the Inventory Adjustment menu and 'Show packages field' in the Instant Inventory menu

* 13.0.1.7.0 (2024-05-08)
    - Excluded associated Ventor access permissions for external users

* 13.0.1.6.0 (2022-12-23)
    - Added the setting 'Save transfer after exit' to the Internal Transfers menu
    - Added the setting 'Allow creating new packages' to menus Instant Inventory, Batch Picking, Cluster Picking, Internal Transfers, and all Operation Types
    - Added the ability to move pallets

* 13.0.1.5.0 (2022-10-10)
    - Added the setting 'Start inventory with 1' to Instant Inventory
    - Added the setting 'Hide Qty to receive ' to  Types of Operations is Receipt
    - Added ability to check Custom Build Name for all devices from Odoo side value
    - Added Ventor Settings menu with submenu:

        - Warehouse Opration
        - Package Management
        - Batch Picking
        - Cluster Picking
        - Internal Transfers
        - Putaway
        - Instant Inventory
        - Inventory Adjustments
        - Quick Info  

* 13.0.1.4.0 (2022-06-08)
    - Added group 'Validate Inventory'
    - Added warning note in user settings about field 'Allowed Warehouses'
    - Fixed uploading Custom Mobile Logo
    - Renamed name of fields in Ventor Configuration:

        - Apply default lots -> Apply default lots and serials
        - Transfer more items -> Move more than planned
        - Autocomplete the item quantity field -> Autocomplete item quantity
        - Manage packages -> Show packages fields
        - Scan destination package -> Force destination package scan
        - Manage product owner -> Show Product Owner field
    - Added the setting 'Confirm source package' to all Operation Types and dependency on the general 'Package' setting
    - Added 'Apply default lots and serials' dependency on the general 'Lots & Serial Numbers' setting
    - Added automatic switch on the 'Show Put in pack button' setting in all menus to default if setting "Package" is switched on
    - Added automatic switch on the 'Show Product Owner field“' setting in all menus to default if setting "Consignment" is switched on

* 13.0.1.3.9 (2022-04-27)
    - Added 'Operation Type' field and logic of validation to Batch Transfer
    - Changed name of the group from 'Manufacturing Menu' to 'MO and WO management'
    - Added updating warehouse_id for all locations to ventor base in post_hook and migration
    - Added record rules 'See Stock Quant Package from allowed warehouses' and 
      'See Stock Inventory Lines from allowed warehouses' for restricting access to warehouses for odoo users

* 13.0.1.3.8 (2022-02-03)
    - Added security group 'Warehouse Operations: Allow applying all qty of product'
    - Added automatic switch on the 'Manage package' setting in all menus to default if setting 'Package' is switched on
    - Added the setting “Scan destination location” to all Operation Types
    - Added dependency of settings 'Show next product' and 'Confirm product'
    - Added the settings 'Behavior on split operation' and 'Behavior on backorder creation' to all Operation Types
    - Added post init hook and migration for setup Allowed Warehouses to users

* 13.0.1.3.7 (2021-12-2)
    - Removed unused settings displayed in the Ventor Preferences tab on the user form
    - Removed 'Default inventory location' from the Inventory settings from the Ventor Configuration
    - Changed 'Ventor Configuration' menu, added 'User Settings' menu item
    - Removed 'Custom package name' field displayed in the Ventor Preferences tab on the user form
    - Added 'Custom Build Name' field in Ventor Configuration/Additional Settings
