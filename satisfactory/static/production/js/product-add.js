console.log("Add-product.js loaded");

function update_resource_field(resource_id, resource_product_id, resource_amount_id) {
  setFormInputValue(resource_id, getFormInputValue(resource_product_id) + ';'+ getFormInputValue(resource_amount_id))
}