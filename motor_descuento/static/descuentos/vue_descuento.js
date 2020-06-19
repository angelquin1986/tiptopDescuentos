vueDescuento = {
    vuetify: new Vuetify({
        theme: {
            themes: {
                light: {
                    primary: '#e2993a',
                    secondary: '#b0bec5',
                    accent: '#8c9eff',
                    error: '#b71c1c',
                },
            },
        },
    }),
    el: "#frm-descuento",
    data: {
        usuario: null,
        listConfDesc: [],


    },
    delimiters: ['${', '}'],
    methods: {
        ejemplo(file) {
            this.formData.append("file", file, file.name);
            this.cargarArchivoServer();
        },
        cargarConfDescuentos() {
            let _this = this;
            rest_get_configuracion_descuentos().then(rest => {
                _this.listConfDesc = rest.data;
                console.log("descuentos", rest);
            });
        },

    },
    computed: {},
    created: function () {
    },
    mounted: function () {
    },
    updated: function () {
        //Materialize.updateTextFields();
    },
}
;
