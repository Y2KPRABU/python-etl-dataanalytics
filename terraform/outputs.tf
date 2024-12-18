output "storage_account_name" {
  value = azurerm_storage_account.example.name
}

output "datalake_filesystem_id" {
  value = azurerm_storage_data_lake_gen2_filesystem.example.id
}
