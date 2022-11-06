export const get_full_site_path = () => {
    return location.protocol + '//' + location.host;
}

const headers = {
    'Content-Type': 'application/json'
};

const site_path = get_full_site_path();

// products

export const create_new_product = async (item) => {
    return await fetch(`${site_path}/api/products/`, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(item)
    });
}

export const get_all_products = async () => {
    return await fetch(`${site_path}/api/products/`, {
        method: 'GET',
        headers: headers,
    });
}

export const get_product_by_id = async (item_id) => {
    return await fetch(`${site_path}/api/products/` + item_id, {
        method: 'GET',
        headers: headers
    });
}

export const update_product_by_id = async (item, item_id) => {
    return await fetch(`${site_path}/api/products/` + item_id, {
        method: 'PUT',
        headers: headers,
        body: JSON.stringify(item)
    });
}

export const delete_product_by_id = async (item_id) => {
    return await fetch(`${site_path}/api/products/` + item_id, {
        method: 'DELETE',
        headers: headers,
    });
}

export const generate_new_upc_13 = async () => {
    return await fetch(`${site_path}/api/products/generate_upc/`, {
        method: 'GET',
        headers: headers,
        body: JSON.stringify(item)
    });
}

// orders
export const get_all_orders = async () => {
    return await fetch(`${site_path}/api/orders/`, {
        method: 'GET',
        headers: headers
    });
}

export const create_new_order = async (products) => {
    return await fetch(`${site_path}/api/orders/`, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(products)
    });
}

export const update_order_by_id = async (order_id, updated_order) => {
    return await fetch(`${site_path}/api/orders/` + order_id, {
        method: 'PUT',
        headers: headers,
        body: JSON.stringify(updated_order)
    });
}

// stripe
export const create_checkout_session = async (checkout_items) => {
    return await fetch(`${site_path}/stripe/create-checkout-session`, {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(checkout_items)
    });
}



