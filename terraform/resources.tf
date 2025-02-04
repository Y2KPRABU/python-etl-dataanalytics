resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "East US"
}

resource "azurerm_storage_account" "example" {
  name                     = "sunadls"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  enable_https_traffic_only = true
  is_hns_enabled            = true

  tags = {
    environment = "staging"
  }
}

resource "azurerm_storage_data_lake_gen2_filesystem" "example" {
  name               = "sunfs"
  storage_account_id = azurerm_storage_account.example.id
}

resource "azurerm_storage_container" "example" {
  name                  = "sunfs"
  storage_account_name  = azurerm_storage_account.example.name
  container_access_type = "private"
}

resource "azurerm_storage_account_network_rules" "example" {
  storage_account_id = azurerm_storage_account.example.id
  default_action     = "Allow"
  bypass             = ["AzureServices"]
}