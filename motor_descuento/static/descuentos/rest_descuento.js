function httpPost(url, data) {
    return fetch(url, {
        method: 'POST', body: data, headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        return response.json().then(data => {
            return Promise.resolve({data: data, status: response.status});
        });
    });

}

function httpGet(url) {
    return fetch(url, {
        method: 'GET', headers: {
            'Content-Type': 'application/json'
        }
    }).then(response => {
        return response.json().then(data => {
            return Promise.resolve({data: data, status: response.status});
        });
    });

}

/**
 * Retorna los datos de configuraciones de descuentos
 * @returns {Promise<unknown>}
 */
function rest_get_configuracion_descuentos() {
    return httpGet('descuentos/get/all');
}