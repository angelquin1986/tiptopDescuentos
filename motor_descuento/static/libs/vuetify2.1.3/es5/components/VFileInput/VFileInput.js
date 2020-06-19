"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports.default = void 0;

require("../../../src/components/VFileInput/VFileInput.sass");

var _VTextField = _interopRequireDefault(require("../VTextField"));

var _VChip = require("../VChip");

var _helpers = require("../../util/helpers");

var _console = require("../../util/console");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance"); }

function _iterableToArray(iter) { if (Symbol.iterator in Object(iter) || Object.prototype.toString.call(iter) === "[object Arguments]") return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) { for (var i = 0, arr2 = new Array(arr.length); i < arr.length; i++) { arr2[i] = arr[i]; } return arr2; } }

function ownKeys(object, enumerableOnly) { var keys = Object.keys(object); if (Object.getOwnPropertySymbols) { var symbols = Object.getOwnPropertySymbols(object); if (enumerableOnly) symbols = symbols.filter(function (sym) { return Object.getOwnPropertyDescriptor(object, sym).enumerable; }); keys.push.apply(keys, symbols); } return keys; }

function _objectSpread(target) { for (var i = 1; i < arguments.length; i++) { var source = arguments[i] != null ? arguments[i] : {}; if (i % 2) { ownKeys(source, true).forEach(function (key) { _defineProperty(target, key, source[key]); }); } else if (Object.getOwnPropertyDescriptors) { Object.defineProperties(target, Object.getOwnPropertyDescriptors(source)); } else { ownKeys(source).forEach(function (key) { Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key)); }); } } return target; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

var _default2 = _VTextField.default.extend({
  name: 'v-file-input',
  model: {
    prop: 'value',
    event: 'change'
  },
  props: {
    chips: Boolean,
    clearable: {
      type: Boolean,
      default: true
    },
    counterSizeString: {
      type: String,
      default: '$vuetify.fileInput.counterSize'
    },
    counterString: {
      type: String,
      default: '$vuetify.fileInput.counter'
    },
    placeholder: String,
    prependIcon: {
      type: String,
      default: '$file'
    },
    readonly: {
      type: Boolean,
      default: false
    },
    showSize: {
      type: [Boolean, Number],
      default: false,
      validator: function validator(v) {
        return typeof v === 'boolean' || [1000, 1024].includes(v);
      }
    },
    smallChips: Boolean,
    truncateLength: {
      type: [Number, String],
      default: 22
    },
    type: {
      type: String,
      default: 'file'
    },
    value: {
      default: function _default() {
        return [];
      },
      validator: function validator(val) {
        return _typeof(val) === 'object' || Array.isArray(val);
      }
    }
  },
  computed: {
    classes: function classes() {
      return _objectSpread({}, _VTextField.default.options.computed.classes.call(this), {
        'v-file-input': true
      });
    },
    counterValue: function counterValue() {
      var fileCount = this.isMultiple && this.lazyValue ? this.lazyValue.length : this.lazyValue instanceof File ? 1 : 0;
      if (!this.showSize) return this.$vuetify.lang.t(this.counterString, fileCount);
      var bytes = this.internalArrayValue.reduce(function (size, file) {
        return size + file.size;
      }, 0);
      return this.$vuetify.lang.t(this.counterSizeString, fileCount, (0, _helpers.humanReadableFileSize)(bytes, this.base === 1024));
    },
    internalArrayValue: function internalArrayValue() {
      return Array.isArray(this.internalValue) ? this.internalValue : (0, _helpers.wrapInArray)(this.internalValue);
    },
    internalValue: {
      get: function get() {
        return this.lazyValue;
      },
      set: function set(val) {
        this.lazyValue = val;
        this.$emit('change', this.lazyValue);
      }
    },
    isDirty: function isDirty() {
      return this.internalArrayValue.length > 0;
    },
    isLabelActive: function isLabelActive() {
      return this.isDirty;
    },
    isMultiple: function isMultiple() {
      return this.$attrs.hasOwnProperty('multiple');
    },
    text: function text() {
      var _this = this;

      if (!this.isDirty) return [this.placeholder];
      return this.internalArrayValue.map(function (file) {
        var name = _this.truncateText(file.name);

        return !_this.showSize ? name : "".concat(name, " (").concat((0, _helpers.humanReadableFileSize)(file.size, _this.base === 1024), ")");
      });
    },
    base: function base() {
      return typeof this.showSize !== 'boolean' ? this.showSize : undefined;
    },
    hasChips: function hasChips() {
      return this.chips || this.smallChips;
    }
  },
  watch: {
    readonly: {
      handler: function handler(v) {
        if (v === true) (0, _console.consoleError)('readonly is not supported on <v-file-input>', this);
      },
      immediate: true
    }
  },
  methods: {
    clearableCallback: function clearableCallback() {
      this.internalValue = this.isMultiple ? [] : null;
      this.$refs.input.value = '';
    },
    genChips: function genChips() {
      var _this2 = this;

      if (!this.isDirty) return [];
      return this.text.map(function (text, index) {
        return _this2.$createElement(_VChip.VChip, {
          props: {
            small: _this2.smallChips
          },
          on: {
            'click:close': function clickClose() {
              var internalValue = _this2.internalValue;
              internalValue.splice(index, 1);
              _this2.internalValue = internalValue; // Trigger the watcher
            }
          }
        }, [text]);
      });
    },
    genInput: function genInput() {
      var input = _VTextField.default.options.methods.genInput.call(this); // We should not be setting value
      // programmatically on the input
      // when it is using type="file"


      delete input.data.domProps.value; // This solves an issue in Safari where
      // nothing happens when adding a file
      // do to the input event not firing
      // https://github.com/vuetifyjs/vuetify/issues/7941

      delete input.data.on.input;
      input.data.on.change = this.onInput;
      return [this.genSelections(), input];
    },
    genPrependSlot: function genPrependSlot() {
      var _this3 = this;

      if (!this.prependIcon) return null;
      var icon = this.genIcon('prepend', function () {
        _this3.$refs.input.click();
      });
      return this.genSlot('prepend', 'outer', [icon]);
    },
    genSelectionText: function genSelectionText() {
      var length = this.text.length;
      if (length < 2) return this.text;
      if (this.showSize && !this.counter) return [this.counterValue];
      return [this.$vuetify.lang.t(this.counterString, length)];
    },
    genSelections: function genSelections() {
      var _this4 = this;

      var children = [];

      if (this.isDirty && this.$scopedSlots.selection) {
        this.internalArrayValue.forEach(function (file, index) {
          if (!_this4.$scopedSlots.selection) return;
          children.push(_this4.$scopedSlots.selection({
            text: _this4.text[index],
            file: file,
            index: index
          }));
        });
      } else {
        children.push(this.hasChips && this.isDirty ? this.genChips() : this.genSelectionText());
      }

      return this.$createElement('div', {
        staticClass: 'v-file-input__text',
        class: {
          'v-file-input__text--placeholder': this.placeholder && !this.isDirty,
          'v-file-input__text--chips': this.hasChips && !this.$scopedSlots.selection
        },
        on: {
          click: function click() {
            return _this4.$refs.input.click();
          }
        }
      }, children);
    },
    onInput: function onInput(e) {
      var files = _toConsumableArray(e.target.files || []);

      this.internalValue = this.isMultiple ? files : files[0]; // Set initialValue here otherwise isFocused
      // watcher in VTextField will emit a change
      // event whenever the component is blurred

      this.initialValue = this.internalValue;
    },
    onKeyDown: function onKeyDown(e) {
      this.$emit('keydown', e);
    },
    truncateText: function truncateText(str) {
      if (str.length < Number(this.truncateLength)) return str;
      var charsKeepOneSide = Math.floor((Number(this.truncateLength) - 1) / 2);
      return "".concat(str.slice(0, charsKeepOneSide), "\u2026").concat(str.slice(str.length - charsKeepOneSide));
    }
  }
});

exports.default = _default2;
//# sourceMappingURL=VFileInput.js.map