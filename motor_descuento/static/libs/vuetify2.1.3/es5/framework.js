"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _install = require("./install");

var services = _interopRequireWildcard(require("./services"));

require("../src/styles/main.sass");

function _interopRequireWildcard(obj) { if (obj && obj.__esModule) { return obj; } else { var newObj = {}; if (obj != null) { for (var key in obj) { if (Object.prototype.hasOwnProperty.call(obj, key)) { var desc = Object.defineProperty && Object.getOwnPropertyDescriptor ? Object.getOwnPropertyDescriptor(obj, key) : {}; if (desc.get || desc.set) { Object.defineProperty(newObj, key, desc); } else { newObj[key] = obj[key]; } } } } newObj.default = obj; return newObj; } }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

var Vuetify =
/*#__PURE__*/
function () {
  function Vuetify() {
    var preset = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : {};

    _classCallCheck(this, Vuetify);

    this.framework = {};
    this.installed = [];
    this.preset = {};
    this.preset = preset;
    this.use(services.Application);
    this.use(services.Breakpoint);
    this.use(services.Goto);
    this.use(services.Icons);
    this.use(services.Lang);
    this.use(services.Theme);
  } // Called on the new vuetify instance
  // bootstrap in install beforeCreate
  // Exposes ssrContext if available


  _createClass(Vuetify, [{
    key: "init",
    value: function init(root, ssrContext) {
      var _this = this;

      this.installed.forEach(function (property) {
        var service = _this.framework[property];
        service.framework = _this.framework;
        service.init(root, ssrContext);
      }); // rtl is not installed and
      // will never be called by
      // the init process

      this.framework.rtl = Boolean(this.preset.rtl);
    } // Instantiate a VuetifyService

  }, {
    key: "use",
    value: function use(Service) {
      var property = Service.property;
      if (this.installed.includes(property)) return;
      this.framework[property] = new Service(this.preset[property]);
      this.installed.push(property);
    }
  }]);

  return Vuetify;
}();

exports.default = Vuetify;
Vuetify.install = _install.install;
Vuetify.installed = false;
Vuetify.version = "2.1.3";
//# sourceMappingURL=framework.js.map