/**
 *  Metodos JS para manejar lo necesario para las validaciones
 * @author aquingaluisa
 **/
/**
 * dependiendo el tipo solo existen correcto=1,error =2
 * @param tipo
 * @returns {string}
 */
function plantilla(tipo, parameter) {
    icono = '';
    cabecera = '';
    showText = '';
    classType = '';

    switch (tipo) {
        case 1:
            icono = 'check';
            cabecera = 'Correcto';
            classType = 'ui-messages-success';
            break;
        case 2:
            icono = 'clear';
            cabecera = 'Error';
            classType = 'ui-messages-error';
            break;
        case 3:
            icono = 'check';
            cabecera = 'Informaci&oacute;n';
            classType = 'ui-messages-info';
            break;
        case 4:
            icono = 'settings';
            cabecera = 'Configuraci&oacute;n';
            classType = 'ui-messages-warn';
            break;
        case 5:
            icono = 'warning';
            cabecera = 'Advertencia';
            classType = 'ui-messages-warn';
            break;
    }

    if (Array.isArray(parameter)) {
        parameter.forEach(function (element) {
            showText = showText + '<li>' +
                '<span class="ui-messages-detail ng-tns-c3-25 ng-star-inserted">' + element + '</span>' +
                '</li>';
        })
    } else {
        showText = '<li>' +
            '<span class="ui-messages-detail ng-tns-c3-25 ng-star-inserted">' + parameter + '</span>' +
            '</li>';

    }
    return '<div  class="toast-ishida ui-messages ui-widget ui-corner-all ng-tns-c3-25 ' + classType + ' ng-trigger ng-trigger-messageAnimation ng-star-inserted" style="display: block; transform: translateY(0px); opacity: 1;">' +
        '<div class="row">' +
        '<div class="row" style="margin-bottom: 7px;height: 0">' +
        '<a style="float:right; text-align:right;color: black" onclick="removerToast(this)">' +
        '<i class="material-icons tiny " style="cursor: pointer" >clear</i>' +
        '</a>' +
        '</div>' +
        '<ul class="ng-tns-c3-25">' +
        '<li class="ng-tns-c3-25 ng-star-inserted" style="">' +
        '<span class="material-icons">' + icono + '</span>' +
        '<span class="ui-messages-summary ng-tns-c3-25 ng-star-inserted">' + cabecera + ':</span>' +
        '</li>' +
        showText +
        '</ul>' +
        '</div>' +
        '</div>';
}

var showToast = (function () {
    return {
        success: function (parametro) {
            showToast.show_toast(plantilla(1, parametro));
        },
        error: function (parametro) {
            showToast.show_toast(plantilla(2, parametro));
        },
        info: function (parametro) {
            showToast.show_toast(plantilla(3, parametro));
        },
        configuracion: function (parametro) {
            showToast.show_toast(plantilla(4, parametro));
        },
        advertencia: function (parametro) {
            showToast.show_toast(plantilla(5, parametro));
        },

        show_toast: function (html) {
            let toast = M.toast({html: html,} );
            //displayLength:40000
        }
    };
})(showToast || {});

function removerToast(element) {
    element.parentElement.parentElement.parentElement.remove();

}