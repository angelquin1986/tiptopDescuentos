"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

var _vue = _interopRequireDefault(require("vue"));

var _helpers = require("../../util/helpers");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

// Types
// Utils
var _default = _vue.default.extend({
  name: 'row',
  functional: true,
  props: {
    headers: Array,
    item: Object,
    rtl: Boolean
  },
  render: function render(h, _ref) {
    var props = _ref.props,
        slots = _ref.slots,
        data = _ref.data;
    var computedSlots = slots();
    var columns = props.headers.map(function (header) {
      var children = [];
      var value = (0, _helpers.getObjectValueByPath)(props.item, header.value);
      var slotName = header.value;
      var scopedSlot = data.scopedSlots && data.scopedSlots[slotName];
      var regularSlot = computedSlots[slotName];

      if (scopedSlot) {
        children.push(scopedSlot({
          item: props.item,
          header: header,
          value: value
        }));
      } else if (regularSlot) {
        children.push(regularSlot);
      } else {
        children.push(value);
      }

      return h('td', {
        class: "text-".concat(header.align || 'start')
      }, children);
    });
    return h('tr', data, columns);
  }
});

exports.default = _default;
//# sourceMappingURL=Row.js.map